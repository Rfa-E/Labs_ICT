<?php include("db.php")?>
<?php include("includes/header.php")?>
<div class="container p-4">
    <div class="row">
        <div class="col-md-4">
            <?php if(isset($_SESSION['missatge'])){?>
                <div class="alert alert-<?=$_SESSION['tipus_missatge'];?> alert-dismissible fade show" role="alert">
                    <?= $_SESSION['missatge'] ?>
                    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
            <?php session_unset();} ?> <!-- elimina les variables de la sessió -->
            <div class="card card-body">
                <form action="save_group.php" method="POST">
                    <div class="form-group">
                        <label>Codi:</label>
                        <input type="number" name="id" class="form-control" 
                            placeholder="escribe el codigo ID" autofocus>
                    </div>
                    <div class="form-group">                            
                        <label>Nom:</label>
			            <input type="text" name="nom" class="form-control" 
                            placeholder="escribe el nombre del Milionari" autofocus>
                    </div>
                    <div class="form-group">
                        <label>Riqueza:</label>
	                    <input type="number" name="Riqueza" class="form-control" 
                            placeholder="escribe la cantidad" autofocus>                            
                    </div>
                    <div class="form-group">
                        <label>Id Pais:</label>
	                    <input type="number" name="Codigo industria" class="form-control"                                   
                            placeholder="escribe el codigo del pais" autofocus>
                    </div>
                    <div class="form-group">
                        <label>Industria:</label>
	                    <input type="number" name="Codigo industria" class="form-control"                                   
                            placeholder="escribe el codigo de la industria" autofocus>
                    </div>
                    <input type = "submit" class="btn btn-success btn-block" 
                        name ="save_group" value="Inserir dades Milionari">
	            </form>
            </div>
        </div>
        <div class>
            <div class="row">
                <div class="col-md-8">
                <?php if(isset($_SESSION['missatge'])){?>
                <div class="alert alert-<?=$_SESSION['tipus_missatge'];?> alert-dismissible fade show" role="alert">
                    <?= $_SESSION['missatge'] ?>
                    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
            <?php session_unset();} ?> <!-- elimina les variables de la sessió -->
            <div class="card card-body">
                <label> Pais para el que quiere hacer la consulta.</label>
                <input type="text" name="pais_f" class="form-control"
                placeholder="escribe el nombre del pais" autofocus>
            </div>
        </div> 
        
        <div class="col-md-8">
            <table class="table table-bordered">
                <thead>
                    <tr>
                        <th>Top</th>
                        <th>Nom</th>
                        <th>Riqueza</th>
                        <th>Id Pais</th>
                        <th>Pais</th>
                        
                </thead>
                <tbody>
                    <?php
                    $query="select top, nombre, TotalNetWorth, m.idcountry, p.country
                    from pais as p join milionari as m on m.idcountry=p.idcountry order by top;";
                    $resultat_query=mysqli_query($connexio,$query);
                    while ($row=mysqli_fetch_array($resultat_query)){ ?>
                        <tr>
                            <td><?php echo $row['top'] ?></td>
                            <td><?php echo $row['nombre'] ?></td>
                            <td><?php echo $row['TotalNetWorth'] ?></td>
                            <td><?php echo $row['idcountry'] ?></td>
                            <td><?php echo $row['country'] ?></td>
                            <td>
                                <a href="edit.php?id=<?php echo $row['top']?>" class= "btn btn-secondary">
                                <!--  Edit -->
                                <i class="fas fa-marker"></i>
                                </a><!-- enllaç -->
                                <a href="delete.php?id=<?php echo $row['top']?>" class= "btn btn-danger"> 
                                <!-- Delete-->
                                <i class="far fa-trash-alt"></i>
                                </a><!-- enllaç -->
                            </td> 
                             
                        </tr>
                    <?php } ?>
                </tbody>
            </table>
        </div>
    </div> 
    
</div>
<?php include("includes/footer.php")?>