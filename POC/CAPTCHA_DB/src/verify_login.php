<?php

require_once "lib/Database.php";
require_once "lib/global.php";
require_once "app/Captcha.php";
require_once "app/CaptchaImage.php";
require_once "app/Image.php";


if(!isset($_SESSION)){ 
    session_start(); 
}


if(!isset($_SESSION['captcha']) || !isset($_POST['username']) || !isset($_POST['password']) || !isset($_POST['image']) || empty($_POST['image'])){
    header("location: index.php");
    exit();
}

if($_POST['username'] != "User" || $_POST['password' != "Password"]){
    header("location: index.php");
    exit();
}

$captcha = $_SESSION['captcha'];

$solution_given = "";
$images = $_POST['image'];


foreach($images as $checked){
    $solution_given .= $checked;
}


if((time()-600) > $captcha->getMoment()){
    header("location: index.php");
    exit();
}


$i = 0;
$ok= true;
foreach(str_split($captcha->getSolution()) as $char){
    if($char == "0"){
        if (!str_contains($solution_given,strval($i)))
            $ok = false;
    } else if($char == "2"){
        if (str_contains($solution_given, strval($i)))
            $ok = false;
    }
    $i++;
}


if($ok == false){
    header("location: index.php");
    exit();
}

$captcha_image = new CaptchaImage($captcha->getId());
$captcha_image->loadFromDatabase($db);

$images = [];
foreach($captcha_image->getImages() as $image){
    $Image = new Image($image);
    $Image->loadFromDatabase($db);
    array_push($images, $Image);
}

$i = 0;
foreach(str_split($captcha->getSolution()) as $char){
    if($char == "1"){
        if (str_contains($solution_given, strval($i)))
            $images[$i]->updateReliability($db, +1);
        else $images[$i]->updateReliability($db, -1);
    } else if($char == "3"){
        if (str_contains($solution_given, strval($i)))
            $images[$i]->updateReliability($db, -1);
    }
    $i++;
}

$_SESSION['is_human'] = true;

header("location: logged_in.php");
exit();

