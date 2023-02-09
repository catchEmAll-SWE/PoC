<?php

use utilities\Database;

require_once "lib/Database.php";

$db = new Database("127.0.0.1", "User", "Password", "poc_swe");

const BASE = "/CAPTCHA_DB/";