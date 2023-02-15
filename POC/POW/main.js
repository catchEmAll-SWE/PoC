let running = 0;

function pow(){
    if (typeof(Worker) !== "undefined") {    
        console.log("Starting pow's workers");

        //get the content and difficulty from the form
        content = document.getElementById('captcha-hashcode-id').value;
        difficulty = document.getElementById('captcha-difficulty').value;

        //create 4 workers
        for(let i=0; i<4; ++i){
            worker = new Worker("web-worker.js");
            worker.onmessage = workerDone;
            worker.postMessage([content, difficulty, i]);
            running++;
        }

    } else {
        // Sorry! No Web Worker support..
        console.log("No Web Worker support");
    }
}

function workerDone(e){
    --running;
    console.log("Worker "+e.data[1]+" is done, hashcode found: "+e.data[0]);
    document.getElementById('nonce').value = e.data[0];
    if(running === 0){
        console.log("All workers complete");
    }
}

/*

hashcode da calcolare = 2 ^ (4 * numero di 0 che vogliamo)
In quanto hashcode è una stringa esadecimala, ogni carattere rappresenta 4 bit. 
Per provare tutte le combinazioni al fine di trovare un hashcode < difficulty dobbiamo calcolare 2 ^ (4 * numero di 0 che vogliamo) combinazioni. 
Per il POC il multithread è implementato (con 4 workers sperimentalmente) i quali cercano di trovare il hashcode in parallelo a partire 
da un content e un'insieme di nonce uguale tra di loro.
Inoltre non viene considerato il caso in cui il browser non supporti i web worker.
(Scopo del POC è integrare le tecnologie)

*/