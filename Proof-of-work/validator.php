<?php 
$ids = $_POST['ids'];
$nonce_found = $_POST['nonce'];
echo $nonce_found;
$difficulty = $_POST['difficulty'];
$pageHTML = file_get_contents('main.html');
$result = "";

$hashcode = hash("sha256", $ids.$nonce_found);
if (str_starts_with($hashcode, $difficulty))
    $result = "Work done";
else
    $result = "Do your work";
    
echo str_replace('<valid />', '<p>'.$result.'</p>', $pageHTML, );
?>