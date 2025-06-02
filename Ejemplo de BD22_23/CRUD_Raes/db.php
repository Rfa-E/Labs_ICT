<?php
session_start();

/*connexió amb la base de dades amb la llibreria de MYSQL: mysqli
  declarem la variable connexio i li assignem

  El codi ha d'estar ditre de sintàxi de php*/

$connexio= mysqli_connect(
'localhost', // cometes simples o dobles
'root',
"1234",
"Proyecto_raes"
) or die("Error en conexion");
/* Si volem comprovar la connexio utilitzem aquest codi
if (isset($connexio)){
	echo "BD connectada";
}*/

?>