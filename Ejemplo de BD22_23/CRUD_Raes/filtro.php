<?php include("db.php")?>
<?php include("includes/header.php")?>
<div class="container p-4">
    <div class="row">
        <div class="col-md-8">
            <?php if(isset($_SESSION['missatge'])){?>
                 <div class="alert alert-<?=$_SESSION['tipus_missatge'];?> alert-dismissible fade show" role="alert">
                    <?= $_SESSION['missatge'] ?>
                    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
             <?php session_unset();} ?>
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
                    <div class="form-group">
                     <?php if (isset($_POST['filtro'])){
                        $filtro=$_POST['filtro'];
                        $query="select top, nombre, TotalNetWorth, m.idcountry, p.country
                        from pais as p join milionari as m on m.idcountry=p.idcountry 
                        where p.country like '%$filtro%'order by top;";
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
                    <?php } ?>
                </tbody>
            </table>
        </div>
                
        </div>
<?php include("includes/footer.php")?>