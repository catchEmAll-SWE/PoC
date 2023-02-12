<?php

use utilities\Template;

require_once "lib/Database.php";
require_once "lib/Template.php";
require_once "lib/global.php";
require_once "app/Captcha.php";
require_once "app/CaptchaImage.php";
require_once "app/Image.php";
require_once "lib/Generate.php";

if(!isset($_SESSION)) 
    { 
        session_start(); 
    }

$captcha = GenerateCaptcha($db);

$_SESSION['captcha'] = $captcha;

$captcha_image = new CaptchaImage($captcha->getId());
$captcha_image->loadFromDatabase($db);

$selected_images = [];
foreach($captcha_image->getImages() as $image){
    $Image = new Image($image);
    $Image->loadFromDatabase($db);
    array_push($selected_images, $Image);
}

$index = new Template("template/index.html");

echo $index->build(array(
    "ClassTarget" => $captcha->getClassTarget(),
    "img0" => $selected_images[0]->getPath(),
    "img1" => $selected_images[1]->getPath(),
    "img2" => $selected_images[2]->getPath(),
    "img3" => $selected_images[3]->getPath(),
    "img4" => $selected_images[4]->getPath(),
    "img5" => $selected_images[5]->getPath(),
    "img6" => $selected_images[6]->getPath(),
    "img7" => $selected_images[7]->getPath(),
    "img8" => $selected_images[8]->getPath(),
));


