<?php

use utilities\Database;
require_once "lib/global.php";
require_once "app/Exception.php";
require_once "app/Captcha.php";
require_once "app/Image.php";
require_once "app/CaptchaImage.php";
require_once "lib/Database.php";

function getClasses(Database $db) : array
{
    $result = $db->executeStatement("SELECT class FROM image GROUP BY class");
    $classes = [];
    for($i = 0; $i < count($result); $i++){
        array_push($classes, $result[$i]['class']);
    }
    return $classes;
}

# select a number of classes to use in the captcha (ex. cars, tables...)
# min 2, max 4 different classes
function choiceClasses(array $classes): array
{
    $number_of_classes = rand(2, 4); 
    $classes_wanted = [];
    for($i = 0; $i < $number_of_classes; $i++){
        shuffle($classes);
        array_push($classes_wanted, array_pop($classes));
    }
    return $classes_wanted;
}

function choiceNumberImage($number_of_classes){
    $image_for_classes = [];
    $remained = 9 - intval($number_of_classes);
    for($i = 0; $i < $number_of_classes - 1; $i++){
        $image_for_class = rand(1, $remained);
        $remained -= $image_for_class;
        array_push($image_for_classes, $image_for_class);
    }
    array_push($image_for_classes, $remained + 1);
    return $image_for_classes;
}

function choiceOfImages(array $classes_wanted, array $images_for_classes, Database $db){
    $selected_images = [];
    for($i = 0; $i < $classes_wanted; $i++){
        $secureImages = $db->executeStatement("SELECT * from image WHERE 'reliability' >= '100' and 'class' = ?", array($classes_wanted[$i]));
        $notSecureImages = $db->executeStatement("SELECT * from image WHERE 'reliability' < '100' and 'class' = ?", array($classes_wanted[$i]));

        $numberOfSecure = rand(1, $images_for_classes[$i]);
        $numberOfNotSecure = $images_for_classes[$i] - $numberOfSecure;

        $Taked = [];
        for($j = 0; $j < $numberOfSecure; $j++){
            $ok = false;
            while($ok == false){
                $x = rand(0, count($secureImages)-1);
                if(!(in_array($x, $Taked))){
                    $ok = true;
                    array_push($Taked, $x);
                    $id = $secureImages[$x]['id'];
                    $path = $secureImages[$x]['path'];
                    $reliability = $secureImages[$x]['reliability'];
                    $image = new Image($id, $classes_wanted[$i], $path, $reliability);
                    array_push($selected_images, $image);
                }
            }
        }

        $Taked = [];
        for($j = 0; $j < $numberOfNotSecure; $j++){
            $ok = false;
            while($ok == false){
                $x = rand(0, count($notSecureImages)-1);
                if(!(in_array($x, $Taked))){
                    $ok = true;
                    array_push($Taked, $x);
                    $id = $notSecureImages[$x]['id'];
                    $path = $notSecureImages[$x]['path'];
                    $reliability = $notSecureImages[$x]['reliability'];
                    $image = new Image($id, $classes_wanted[$i], $path, $reliability);
                    array_push($selected_images, $image);
                }
            }
        }
    }
    return $selected_images;
}

function hashCaptcha(array $selected_images){
    sort($selected_images);
    $id_captcha = "";
    foreach($selected_images as $image){
        $id_captcha .= $image->getId();
    }
    return $id_captcha;
}

function alreadyExisting($id, Database $db): bool{
    $result = $db->executeStatement("SELECT * FROM captcha WHERE id = $id");
    if (count($result) == 0)
        return false;
    return true;
}

# solution for the image:
# if the image have the class target:
#       if is secure (reliability >= 100) value = 0, 1 else
# else if is secure value = 2, 3 else
function solutionCaptcha(array $selected_images, string $class_target){
    $solution = "";
    foreach($selected_images as $image){
        if($image->getClass() == $class_target){
            if($image->getReliability() >= 100){
                $solution .= "0";
            } else {
                $solution .= "1";
            }
        } else {
            if($image->getReliability() >= 100){
                $solution .= "2";
            } else {
                $solution .= "3";
            }
        }
    }
    return $solution;
}

function GenerateCaptcha(Database $db): Captcha
{
    $classes = getClasses($db);
    $captcha = null;
    $ok = false;
    while($ok == false){
        $classes_wanted = choiceClasses($classes);
        $class_target = $classes_wanted[0];
        $images_for_classes = choiceNumberImage(count($classes_wanted));
        $selected_images = choiceOfImages($classes_wanted, $images_for_classes, $db);
        $id_captcha = hashCaptcha($selected_images);
        if(!alreadyExisting($id_captcha, $db)){
            $ok = true;
            shuffle($selected_images);
            $solution = solutionCaptcha($selected_images, $class_target);
            $captcha = new Captcha($id_captcha, $class_target, $solution, time());
            $captcha->insertIntoDatabase($db);
            $id_images = [];
            foreach($selected_images as $image){
                array_push($id_images, $image->getId());
            }
            $captcha_image = new CaptchaImage($id_captcha, $id_images);
            $captcha_image->insertIntoDatabase($db);
        } else {
            unset($selected_images);
        }
    }
    return $captcha;
}