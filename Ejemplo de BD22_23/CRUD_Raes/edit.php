<?php
include("db.php");
if (isset($_GET['id'])){
    $id=$_GET['id'];
    $modifica="select * from grups where id=$id";
    $resultat=mysqli_query($connexio,$modifica);
    if (mysqli_num_rows($resultat)== 1){
        //echo "es pot modificar";
        $row=mysqli_fetch_array($resultat);
        $nom=$row['nom'];
        $origen=$row['origen'];
        $anyFundacio=$row['anyFundacio'];


    }

}
if (isset($_POST['modifica'])){
    echo "actualizando";
    $id = $_GET['id'];

	$nom = $_POST['nom'];
	$origen = $_POST['origen'];
	$anyFundacio = $_POST['anyFundacio'];

	$modificar="UPDATE grups set nom='$nom',origen='$origen',anyFundacio=$anyFundacio where id=$id";
	$resultat=mysqli_query($connexio,$modificar);
	if($resultat){
		//echo "<h3>Modificat correctament</h3>";
		$_SESSION['missatge'] = "Grup Modificat Correctament";
		$_SESSION['tipus_missatge'] = 'success'; // Color verd pel missatge (succes és un verd a Bootstrap)
		header("Location: index.php");//redirecciona a index.php
    }
    die("Modificacio incorrecta");
}

?>
<?php include("includes/header.php")?>
<!-- a continuacio s'utilitze classes de bootstrap -->
<div class="container p-4">
    <div class="row">
        <div class="col-md-4 mx-auto">
            <div class="card-card-body">
                <form action="edit.php?id=<?php echo $_GET['id']; ?>" method="POST">
                    <div class="form-group">
                    <input type="text" name= "nom" value="<?php echo $nom; ?>"
                    class= "form-control" placeholder= "Modifica Nom">
                    </div>
                    <div class="form-group">
                    <input type="text" name= "origen" value="<?php echo $origen; ?>"
                    class= "form-control" placeholder= "Modifica Pais origen">
                    </div>
                    <div class="form-group">
                    <input type="text" name= "anyFundacio" value="<?php echo $anyFundacio; ?>"
                    class= "form-control" placeholder= "Modifica Any de fundació">
                    </div>
                    <button class="btn btn-success" name="modifica" >
                    Modifica
                    </button>
                </form>
            </div>
        </div>
    </div>
</div>


<?php include("includes/footer.php")?>