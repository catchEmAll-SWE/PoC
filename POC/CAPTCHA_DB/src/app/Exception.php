<?php

use Exception;

class UndefinedField extends Exception{
    public function __construct(){
        parent::__construct("Campi inseriti non correttamente.");
    }
}

class FieldNotLoaded extends Exception{
    public function __construct($string){
        parent::__construct("Campo $string non inserito.");
    }
}