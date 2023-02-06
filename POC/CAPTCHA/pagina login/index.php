<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="./index.css">
    <title>Login Page</title>
</head>
<body>
    <?php
    $dbconnection = mysqli_connect("localhost","root","root-1234","captcha_db");
    if(!$dbconnection)
    die("connessione non riuscita".mysqli_connect_error());
    else
    echo 'connessione riuscita';
    $result = mysqli_query($dbconnection, "SELECT idImmagine FROM captcha_db.immagine");
    $links = [];
    $counter = 0;
    while($row = mysqli_fetch_array($result)){
        $links[$counter] = "https://source.unsplash.com/" . $row["idImmagine"];
        $counter = $counter+1;
    }
    ?>
    <h1>
        <span lang="en">Login</span>
    </h1>
    <form method="POST" action="invio_soluzione.php">
        <div class="captcha-grid">
            <div class="item">
                <input type="checkbox" id="img1" />
                <label for="img1"><img src="<?php echo $links[0]?>" width=100% 
                    height=100%></label>
            </div>
            <div class="item">
                <input type="checkbox" id="img2" />
                <label for="img2"><img src="<?php echo $links[1]?>" width=100% 
                    height=100%></label>
            </div>
            <div class="item">
                <input type="checkbox" id="img3" />
                <label for="img3"><img src="<?php echo $links[2]?>" width=100% 
                    height=100%></label>
            </div>
            <div class="item">
                <input type="checkbox" id="img4" />
                <label for="img4"><img src="<?php echo $links[3]?>" width=100% 
                    height=100%></label>
            </div>
            <div class="item">
                <input type="checkbox" id="img5" />
                <label for="img5"><img src="<?php echo $links[4]?>" width=100% 
                    height=100%></label>
            </div>
            <div class="item">
                <input type="checkbox" id="img6" />
                <label for="img6"><img src="<?php echo $links[5]?>" width=100% 
                    height=100%></label>
            </div>
            <div class="item">
                <input type="checkbox" id="img7" />
                <label for="img7"><img src="<?php echo $links[6]?>" width=100% 
                    height=100%></label>
            </div>
            <div class="item">
                <input type="checkbox" id="img8" />
                <label for="img8"><img src="<?php echo $links[7]?>" width=100% 
                    height=100%></label>
            </div>
            <div class="item">
                <input type="checkbox" id="img9" />
                <label for="img9"><img src="<?php echo $links[8]?>" width=100% 
                    height=100%></label>
            </div>
        </div>
        <div class="conferma-login">
            <button>Conferma</button>
        </div>
    </form>
</body>
</html>