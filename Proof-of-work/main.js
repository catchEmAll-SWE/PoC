function calcHash(){
    content = document.getElementById('ids').value;
    difficulty = document.gerElementById('difficulty').value;
    var worker = [];
    /*for (let i=0; i<4; ++i){
        worker[i] = new Worker('worker.js');
        worker.postMessage({start, end, difficulty, content});
    }
    /*worker.onmessage = (e) => {
        const {nonce, hash} = e.data;
        document.getElementById('nonce').value = nonce;
        print(nonce);
        worker.terminate();
    }/*/
    var nonce = 0;
    var hash = '';
    while (!hash.startsWith(difficulty)) {
        hash = crypto.subtle.digest('SHA-256', content + nonce);
        if (hash.startsWith(difficulty)) {
            postMessage({nonce, hash});
            break;
        }
        nonce++;
    }
    return false
}