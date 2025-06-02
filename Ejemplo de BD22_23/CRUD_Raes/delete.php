<?php
include("db.php");
if (isset($_GET['top'])){ 
    $id=$_GET['top'];
    $esborra="delete from grups where id=$top";
    $resultat=mysqli_query($connexio,$esborra);
    if (!$resultat){
        die ("Esborrar erròni");
    }
    $_SESSION['missatge'] = "Grup Esborrat Correctament";
	$_SESSION['tipus_missatge'] = 'danger'; // Color verd pel missatge (succes és un verd a Bootstrap)
    header("Location: index.php");//redirecciona a index.php
}
?>