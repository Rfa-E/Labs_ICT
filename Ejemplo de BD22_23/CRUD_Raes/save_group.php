
<?php 
include("db.php") ;
		if (isset($_POST['save_group'])){
			$id = $_POST['id'];
			$nom = $_POST['nom'];
			$origen = $_POST['origen'];
			$anyFundacio = $_POST['anyFundacio'];
			//echo $nom;
			$inserir="INSERT INTO grups (id,nom,origen,anyFundacio) values ($id,'$nom','$origen',$anyFundacio)";
			$resultat=mysqli_query($connexio,$inserir);
			if($resultat){
				//echo "<h3>Inserit correctament</h3>";
				$_SESSION['missatge'] = "Grup Inserit Correctament";
				$_SESSION['tipus_missatge'] = 'success'; // Color verd pel missatge (succes és un verd a Bootstrap)
				header("Location: index.php");//redirecciona a index.php
			}
			else die("Inserció errònia"); //finalitza l'aplicació
		}
	?>