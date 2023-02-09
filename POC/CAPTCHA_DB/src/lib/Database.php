<?php
namespace utilities;
use Exception;
use mysqli;

class WrongParamType extends Exception {
    public function __construct($param) {
        parent::__construct("Wrong type for parameter $param, expected int, float or string, got ".gettype($param));
    }
}

class Database{

    private array $type_conversion = [
        'integer' => 'i',
        'double' => 'd',
        'string' => 's',
    ];

    private string $host;
    private string $user;
    private string $password;
    private string $database;
    private string $port;
    private ?mysqli $db_connection;

    public function __construct($host, $user, $password, $database, $port = 3306) {
        $this->host = $host;
        $this->user = $user;
        $this->password = $password;
        $this->database = $database;
        $this->port = $port;

        $this->db_connection = null;
    }

    public function __toString() {
        return "Database $this->database on $this->host:$this->port";
    }

    /**
     * @throws Exception
     */
    private function connection(): ?mysqli
    {
        if ($this->db_connection == null) {
            $this->db_connection = new mysqli($this->host, $this->user, $this->password, $this->database, $this->port);
        }

        if ($this->db_connection->connect_errno) {
            throw new Exception("Failed to connect to MySQL: (" . $this->db_connection->connect_errno . ") " . $this->db_connection->connect_error);
        }

        return $this->db_connection;
    }

    private function closeConnection(): void
    {
        if ($this->db_connection != null) {
            $this->db_connection->close();
            $this->db_connection = null;
        }
    }

    /**
     * @return string containing the param type used by mysqli to bind params
     * @throws WrongParamType
     */
    private function getParamType($param): string
    {
        if ($this->type_conversion[gettype($param)] == null) {
            throw new WrongParamType($param);
        }

        return $this->type_conversion[gettype($param)];
    }

    /**
     * @param string $statement contains the SQL statement with 0 or more "?" placeholders for parameters
     * @param array $params contains the parameters to be bound to the statement
     * @return array containing the result rows of a query
     * @throws WrongParamType if one or more parameters are not of type int, float or string
     * @throws Exception in case of errors with database communication
     */
    public function executeStatement(string $statement, array $params = array())
    {
        $this->connection();
        $stmt = $this->db_connection->prepare($statement);

        if($stmt) {
            if (count($params) > 0) {
                $param_type = "";
                foreach ($params as $param){
                    $param_type .= $this->getParamType($param);
                }
                $stmt->bind_param($param_type, ...$params);
            }

            $stmt->execute();
            $result = $stmt->get_result();

            if ($this->connection()->error) {
                throw new Exception("Could not execute query: " . $this->connection()->error);
            }

            if(!(gettype($result) == "boolean")) {
                $result_array = $result->fetch_all(MYSQLI_ASSOC);
                $result->free();
                $stmt->close();
                $this->closeConnection();
                return $result_array;
            }

            $stmt->close();
            $this->closeConnection();
            return $result;
        } else {
            $this->closeConnection();
            throw new Exception("Failed to execute query: " . $statement . " (" . $this->db_connection->errno . ") " . $this->db_connection->error);
        }
    }
}
?>