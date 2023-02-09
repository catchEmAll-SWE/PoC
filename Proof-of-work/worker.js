onmessage = (e) => {
    const {start, end, difficulty, content} = e.data;
    let nonce = start;
    let hash = '';
    while (nonce < end) {
        hash = crypto.subtle.digest('SHA-256', content + nonce);
        if (hash.startsWith(difficulty)) {
            postMessage({nonce, hash});
            break;
        }
        nonce++;
    }
}