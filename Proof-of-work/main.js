
async function calcHash(content, nonce){
    hashArrayBuffer = await crypto.subtle.digest('SHA-256', enc.encode(content + nonce));
    hashArray = Array.from(new Uint8Array(hashArrayBuffer));
    return hashArray.map((b) => b.toString(16).padStart(2, '0')).join('');
}

async function resolveHashProblem(){
    content = document.getElementById('ids').value;
    difficulty = document.getElementById('difficulty').value;
    /*var worker = [];
    for (let i=0; i<4; ++i){
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
    enc = new TextEncoder()
    dec = new TextDecoder()
    while (true) {
        calcHash(content, nonce).then((str_hash) => {
            if (str_hash.startsWith(difficulty)) {
                document.getElementById('nonce').value = nonce;
                console.log('nonce found:: '+nonce)
                return true;
                nonce++
            }    
        })
       return true
    }
    return false
}