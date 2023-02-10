<?php

use utilities\Template;
require_once "lib/Template.php";

if(!isset($_SESSION)) 
    { 
        session_start(); 
    }

if(!isset($_SESSION['is_human'])){
    header("location: /CAPTCHA_DB/src/index.php");
    exit();
}

unset($_SESSION["is_human"]);
unset($_SESSION["captcha"]);

$logged_in = new Template("template/logged_in.html");

echo $logged_in->build(array());
