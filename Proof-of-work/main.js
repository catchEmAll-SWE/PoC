function calcHash(){
    Content = document.getElementById('ids').value;
    difficulty = document.gerElementById('difficulty').value;
    for (let i=0; i<10; ++i){
        hashcode = crypto.subtle.digest('SHA-256', staticText+str(i));
        if (hashcode.startsWith(difficulty)){
            document.getElementById('nonce').value = hashcode
            i = 10
        }
    }
    return false
}