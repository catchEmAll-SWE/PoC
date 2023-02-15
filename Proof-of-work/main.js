let running = 0;

function pow(){
    if (typeof(Worker) !== "undefined") {    
        console.log("Starting pow's workers");

        //get the content and difficulty from the form
        content = document.getElementById('ids').value;
        difficulty = document.getElementById('difficulty').value;

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
    if(running === 0){
        console.log("All workers complete");
    }
}

/*

hashcode da calcolare = 2 ^ (4 * numero di 0 che vogliamo)
In quanto hashcode è una stringa esadecimala, ogni carattere rappresenta 4 bit. 
Per provare tutte le combinazioni al fine di trovare un hashcode < difficulty dobbiamo calcolare 2 ^ (4 * numero di 0 che vogliamo) combinazioni. 

*/