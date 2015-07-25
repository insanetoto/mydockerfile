<?php

    $mysql_server_name="10.0.0.106";
    $mysql_username="root";
    $mysql_password="gogogo";
    $con = mysql_connect($mysql_server_name,$mysql_username,$mysql_password);
    if (!$con)
    {
	die('失败:'.mysql_error());
    }
    else
    {
	mysql_query("SET NAME utf-8");
	mysql_select_db("scores",$con);
	$result = mysql_query("select * from name_score");
	while($row=mysql_fetch_array($result))
	{
	    echo $row['name']." ".$row['score'];
	    echo "<br />";
	}
	
    }
    mysql_close($con);
?>
