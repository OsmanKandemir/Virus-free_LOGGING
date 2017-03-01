<html>
	<head>
		<title>Register</title>
<?php
$host = "localhost";
$user = "****";
$pass = "****";
$db = "****";	

$baglan = mysql_connect($host,$user,$pass);
$db_sec = mysql_select_db($db);


if(! $db_sec)
   {
	echo('Could not connect: ' . mysql_error());
   }
echo 'Connections successfully<br>';


?>

	</head>
</html>