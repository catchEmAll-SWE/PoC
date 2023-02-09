<?php

use Exception;
use utilities\Database;
require_once "global.php";
require_once "Exception.php";
require_once "Captcha.php";
require_once "Image.php";

class CaptchaImage{
    private string $captcha;
    private ?array $images; 

    public function __construct(string $captcha, array $images = []){
        $this->captcha = $captcha;
        $this->images = $images;
    }

    public function loadFromDatabase(Database $db): void{
        $result = $db->executeStatement("SELECT * FROM captcha_image WHERE captcha = $this->captcha ORDER BY position ASC");
        for($i = 0; $i < count($result); $i++){
            array_push($this->images, $result[$i]['image']);
        }
    }

    public function insertIntoDatabase(Database $db): void{
        for ($i = 0; $i < count($this->images); $i++){
            $db->executeStatement("INSERT INTO captcha_image(captcha,image,position) VALUES ($this->captcha, $this->images[$i], $i");
        }
    }

    public function getCaptcha(): string{
        return $this->captcha;
    }

    public function getImages(): array{
        return $this->images;
    }
}