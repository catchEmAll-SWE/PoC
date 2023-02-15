async function sha256Algorithm(content, difficulty){
    var nonce = 0;
    while (true) {
        const msg = new TextEncoder().encode(content + nonce);
        const hashArrayBuffer = await crypto.subtle.digest('SHA-256', msg);
        const hashHex = Array.from(new Uint8Array(hashArrayBuffer))
                        .map(b => b.toString(16).padStart(2, '0'))
                        .join('');
        if (hashHex.startsWith(difficulty)) 
            return nonce;
        nonce++;
    }
}

onmessage = async function (e) {
    const content = e.data[0];
    const difficulty = e.data[1];
    let hashcode = await sha256Algorithm(content, difficulty);
    self.postMessage([hashcode, e.data[2]]);
}