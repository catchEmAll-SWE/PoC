<?php

use utilities\Database;
require_once "lib/global.php";
require_once "app/Exception.php";

class CaptchaNotFound extends Exception{
    public function __construct($id){
        parent::__construct("Captcha with id: $id not found");
    }
}


class Captcha{
    private string $id;
    private static string $difficulty = "0000";
    private ?string $class_target;
    private ?string $solution;

    private ?int $moment;

    public function __construct(string $id, string $class_target = null, string $solution = null, int $moment = null){
        $this->id = $id;
        $this->class_target = $class_target;
        $this->solution = $solution;
        $this->moment = $moment;
    }

    public function loadFromDatabase(Database $db): void{
        $result = $db->executeStatement("SELECT * FROM captcha WHERE id = $this->id");
        if (count($result) == 0)
            throw new CaptchaNotFound($this->id);

        $this->class_target = $result[0]['class_target'];
        $this->solution = $result[0]['solution'];
        $this->moment = intval($result[0]['moment']);
    }

    public function insertIntoDatabase(Database $db): void{
        if ($this->id == null || $this->class_target == null || $this->solution == null || $this->moment == null)
            throw new UndefinedField();
        $db->executeStatement("INSERT INTO captcha(id,class_target,solution,moment) VALUES (\"$this->id\",\"$this->class_target\",\"$this->solution\",\"$this->moment\")");
    }

    public function getId(): string
    {
        if ($this->id != null) {
            return $this->id;
        } else {
            throw new FieldNotLoaded('id');
        }
    }

    public function getClassTarget(): string
    {
        if ($this->class_target != null) {
            return $this->class_target;
        } else {
            throw new FieldNotLoaded('Classe target');
        }
    }

    public function getSolution(): string
    {
        if ($this->solution != null) {
            return $this->solution;
        } else {
            throw new FieldNotLoaded('solution');
        }
    }

    public function getMoment(): int
    {
        if ($this->moment != null) {
            return $this->moment;
        } else {
            throw new FieldNotLoaded('moment');
        }
    }

    public function getHashcodeSha256(): string{
        return hash("sha256", $this->id);
    }

    public function getDifficulty(): string{
        return Captcha::$difficulty;
    }

    public function setClassTarget($class_target): void{
        $this->class_target = $class_target;
    }

    public function setSolution($solution): void{
        $this->solution = $solution;
    }

    public function setMoment(): void{
        $this->moment = time();
    }
}