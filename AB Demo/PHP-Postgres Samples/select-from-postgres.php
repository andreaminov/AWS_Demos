<?php

try {
    $myPDO = new PDO("pgsql:host=ab-demo.c6so2hkiqsfy.us-east-1.rds.amazonaws.com;dbname=todo", "postgres", "postgres");

    $sql = "SELECT * FROM todos";

    foreach($myPDO->query($sql) as $row){
        print "<br/>";
        print $row.['id'].' - '.$row['text'];
    }

} catch (PDOException $e) {
    echo $e->getMessage();
}

?>