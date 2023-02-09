<?php

use Exception;
use utilities\Database;

require_once "global.php";

class ImageNotFound extends Exception{
    public function __construct($id){
        parent::__construct("Image with id: $id not found");
    }
}

class Image{
    private string $id;
    private string $class;
    private int $reliability;
    private string $path;

    public function __construct(string $id, string $class, string $path, int $reliability = 500){
        $this->id = $id;
        $this->class = $class;
        $this->path = $path;
        $this->reliability = $reliability;
    }

    public function loadFromDatabase(Database $db): void{
        $result = $db->executeStatement("SELECT * FROM image WHERE id= $this->id");
        if (count($result) == 0)
            throw new ImageNotFound($this->id);
        
        $this->class = $result[0]['class'];
        $this->reliability = $result[0]['reliability'];
        $this->path = $result[0]['path'];
    }

    public function getId(): string
    {
        return $this->id;
    }

    public function getClass(): string
    {
        return $this->class;
    }

    public function getPath(): string
    {
        return $this->path;
    }

    public function getReliability(): int
    {
        return $this->reliability;
    }

    public function updateReliability(Database $db, $value): void{
        $this->reliability += $value;
        $db->executeStatement("UPDATE image SET reliability = $this->reliability WHERE id = $this->id");
    }
}