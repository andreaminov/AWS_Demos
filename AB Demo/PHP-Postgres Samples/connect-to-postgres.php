<?php

try {
    $myPDO = new PDO("pgsql:host=ab-demo.c6so2hkiqsfy.us-east-1.rds.amazonaws.com;dbname=todo", "postgres", "postgres");
    echo "Connected to PostgreSQL with PDO";

} catch (PDOException $e) {
    echo $e->getMessage();
}

?>