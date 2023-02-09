function calcHash(){
    staticText = "text";
    difficulty = "000"
    for (let i=0; i<10; ++i){
        hashcode = crypto.subtle.digest('SHA-256', staticText+str(i));
        if (hashcode.startsWith(difficulty)){
            document.getElementById('nonce').value = hashcode
            i = 10
        }
    }
    return false
}