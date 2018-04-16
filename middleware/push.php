<?php header('Access-Control-Allow-Origin: *'); ?>
<?php
/* Attempt MySQL server connection. Assuming you are running MySQL
 *  * server with default setting (user 'root' with no password) */
$link = mysqli_connect("localhost", "CSCI152Pi", "piIsGood", "parkingLots");
if($link === false){
        die("ERROR: Could not connect. " . mysqli_connect_error());
}
$lot = htmlspecialchars($_POST["lot"]);
$genID = htmlspecialchars($_POST["genID"]);
$space = htmlspecialchars($_POST["space"]);
$isOpen = htmlspecialchars($_POST["isOpen"]);
echo "$lot , $genID , $space , $isOpen\n";

$sql = "UPDATE parking SET isOpen=$isOpen WHERE lot='$lot' AND genId='$genID' AND space=$space";
if(mysqli_query($link, $sql)){
        echo "Records added successfully.";
} else{
        echo "ERROR: Could not able to execute $sql. " . mysqli_error($link);
}

?>
