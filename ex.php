<?php


	require("connect.php");
	$email = $_GET['e'];
	$password = $_GET['p'];

	
	if($email != NULL){
		if($password != NULL){

			mysql_query("INSERT INTO log (email,password) values ('$email','$password')");
			echo "Email and password registered";
	
	
		}
	} else {
		echo "otherwise something went";



	}

	

?>