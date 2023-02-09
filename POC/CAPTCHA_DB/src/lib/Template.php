<?php
namespace utilities;
use Exception;

class ComponentNotFound extends Exception {
    public function __construct($component) {
        parent::__construct("Component $component not found");
    }
}
class RepeatedComponent extends Exception {
    public function __construct($component, $repetitions) {
        parent::__construct("Excepted only one $component found $repetitions");
    }
}
class UnreplacedComponent extends Exception {
    public function __construct() {
        parent::__construct("There are unreplaced components");
    }
}
class Template
{
    private const PATTERN_BEGIN = "<component>";
    private const PATTERN_END = "</component>";

    private string $file_content;

    /**
     * @param string $file_name The name of the file to load
     * @throws Exception if file not found
     */
    public function __construct(string $file_name)
    {
        try {
            $this->file_content = file_get_contents($file_name);
        } catch (Exception $e) {
            throw new Exception("File $file_name not found");
        }
    }

    /**
     * @param string $component_name The name of the unique component to replace
     * @param string $component_content The content to replace the component with
     * @throws ComponentNotFound
     * @throws RepeatedComponent
     */
    public function replaceComponent(string $component_name, string $component_content): void {
        $pattern = self::PATTERN_BEGIN . $component_name . self::PATTERN_END;

        $total_changes = 0;
        $this->file_content = str_replace($pattern, $component_content, $this->file_content, $total_changes);

        if ($total_changes == 0) {
            throw new ComponentNotFound($component_name);
        }
    }

    /**
     * @throws UnreplacedComponent if there are components that have not been replaced
     */
    private function checkForUnreplacedComponents(): void {
        $pattern = sprintf("~(%s)(.*)(%s)~", self::PATTERN_BEGIN, self::PATTERN_END);
        if (preg_match_all($pattern, $this->file_content)) {
            throw new UnreplacedComponent();
        }
    }

    /**
     * @param array $components An associative array of components to replace in which keys represent the component's
     * name and values represent the content to replace the component with
     * @return string the content of the template with all the components replaced
     * @throws UnreplacedComponent if there are components that have not been replaced
     */
    public function build(array $components = array()): string {
        if (count($components) > 0) {
            foreach ($components as $component_name => $component_content) {
                try {
                    $this->replaceComponent($component_name, $component_content);
                } catch (Exception $e) {
                    echo "Unable to build template. Error: ".$e->getMessage();
                }
            }
        }

        $this->checkForUnreplacedComponents();

        return $this->file_content;
    }
}