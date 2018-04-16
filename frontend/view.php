<?php header('Access-Control-Allow-Origin: *'); ?>
<?php
//-----CODE RUNS ON ANDREW BELL'S PI AS MIDDLE WARE-----//
/* Attempt MySQL server connection. Assuming you are running MySQL
 *  * server with default setting (user 'root' with no password) */
$link = mysqli_connect("localhost", "CSCI152Pi", "piIsGood", "parkingLots");
if($link === false){
            die("ERROR: Could not connect. " . mysqli_connect_error());
}
$sql = "SELECT * FROM parking";
$result = mysqli_query($link, $sql);
if($result) {
        $myObj = array();
            $myObj = $result->fetch_all(MYSQLI_ASSOC);
}

$myJSON = json_encode($myObj);

echo $myJSON;

?>
