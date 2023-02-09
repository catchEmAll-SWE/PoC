<?php

use Exception;
use utilities\Database;
require_once "global.php";
require_once "Exception.php";

class UserNotFound extends Exception{
    public function __construct($user){
        parent::__construct("User: $user not found");
    }
}

class User{
    private string $username;
    private ?string $pw;

    public function __construct(string $username, string $pw = null){
        $this->username = $username;
        $this->pw = $pw;
    }

    public function loadFromDatabase(Database $db): void{
        $result = $db->executeStatement("SELECT * FROM user WHERE username = $this->username");
        if (count($result) == 0)
            throw new UserNotFound($this->username);
        $this->pw = $result[0]['pw'];
    }

    public function getPw(): string{
        if($this->pw != null){
            return $this->pw;
        } else {
            throw new FieldNotLoaded('pw');
        }
    }

    public function getUsername(): string{
        return $this->username;
    }
}