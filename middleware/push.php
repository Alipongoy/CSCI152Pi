<?php header('Access-Control-Allow-Origin: *'); ?>
<?php
/* Attempt MySQL server connection. Assuming you are running MySQL
 *  * server with default setting (user 'root' with no password) */
$link = mysqli_connect("localhost", "CSCI152Pi", "piIsGood", "parkingLots");
if($link === false){
    die("ERROR: Could not connect. " . mysqli_connect_error());
}

$data = json_decode(file_get_contents('php://input'), true);

foreach($data as $spot) {
    $lot = "lotQ";
    $genIDX = htmlspecialchars($spot["lot"]);
    $genIDY = htmlspecialchars($spot["genID"]);
    $genID = "$genIDY-$genIDY";
    $space = htmlspecialchars($spot["space"]) + 1;
    $isOpen = htmlspecialchars($spot["isOpen"]);
    if(!$isOpen) $isOpen = 0;
    echo "$lot , $genID , $space , $isOpen\n";
    $sql = "UPDATE parking SET isOpen=$isOpen WHERE lot='$lot' AND genID='$genID' AND space=$space";
    if(mysqli_query($link, $sql)) {
        //echo "Records modified successfully.";
    } else {
        $sql = "INSERT INTO parking (lot, genID, space, isOpen) VALUES ('$lot', '$genID', '$space', '$isOpen')";
        if(mysqli_query($link, $sql)) {
            //echo "Records added successfully.";
        } else {
            echo "ERROR: Could not able to execute $sql. " . mysqli_error($link);
        }
    }
}
?>
