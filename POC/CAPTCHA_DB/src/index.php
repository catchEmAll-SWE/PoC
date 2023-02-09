<?php

use components\Database;
use components\Template;

require_once "lib/Database.php";
require_once "lib/Template.php";
require_once "lib/global.php";

$captcha = GenerateCaptcha($db);
