<?php 
$username = $_POST['name'];
$passwd = $_POST['passwdord'];
$nonce_found = $_POST['nonce'];
$difficulty = $_POST['difficulty'];

$hashcode = hash("sha256", $username.$passwd.$nonce_found);


?>