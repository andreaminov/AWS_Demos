<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <title>To Do Demo App</title>
</head>

<body>
  <h1>To Do List</h1>
  
  <!--  Display To Do List -->
  <?php

    function displayToDo () {
      try {
        $myPDO = new PDO("pgsql:host=postgress.c6so2hkiqsfy.us-east-1.rds.amazonaws.com;dbname=todo", "postgres", "postgres");
    
        $sql = "SELECT * FROM todos";
    
        foreach($myPDO->query($sql) as $row){
            print "<br/>";
            print $row['text'];
        }

      } catch (PDOException $e) {
          echo $e->getMessage();
      }


    }

    function insertToDo() {
            
      try {
      $myPDO = new PDO("pgsql:host=postgress.c6so2hkiqsfy.us-east-1.rds.amazonaws.com;dbname=todo", "postgres", "postgres");
      
      $sql_insert = "INSERT INTO todos(text)VALUES('$_POST[task]')";
      $myPDO -> query($sql_insert);

      } catch (PDOException $e) {
          echo $e->getMessage();
      }

    }

    displayToDo();

  ?>

  <br/><br/><br/>

    <form method="post" action="index.php <?php insertToDo(); ?>">
        Task: <input type="text" name="task">
        <input type="submit" name="sumbit" class="button" value="submit" />
    </form>

  <!-- Stress and Display Local IP address of Web Server -->

  <?php
    # Stress the system for a maximum of 10 minutes. Kill all stress processes when requested by the user. 
    $stressOrKill = $_GET["stress"];
    if (strlen($stressOrKill) > 0) {
      if ($stressOrKill == "start") {
        echo ("<h2>Generating load</h2>");
        exec("stress --cpu 4 --io 1 --vm 1 --vm-bytes 128M --timeout 600s > /dev/null 2>/dev/null &");
      } elseif ($stressOrKill == "stop") {
        exec("kill -9 (pidof stress)");
        echo ("<h2>Killed stress processes</h2>");
      } else {
      }
    }
  ?>
  
  <!-- Generate Stress Load -->
  <div id="content">
    <center>
      <br />
      <h2>Web Server IP: <?php
          echo $_SERVER['SERVER_ADDR'];
          ?></h2> <br /> <br />
      <h2>Generate Load</h2>
      <table border="0" width="30%" cellpadding="0" cellspacing="0" id="content-table">
        <tr>
          <td>
            <form action="index.php"><input type="hidden" name="stress" value="start" /><input type="submit" value="Start Stress" /></form>
          </td>
          <td>
            <form action="index.php"><input type="hidden" name="stress" value="stop" /><input type="submit" value="Stop Stress" /></form>
          </td>
        </tr>
      </table>
    </center> <!-- end content -->
  </div>

  </body>

</html>