<?php
    $get = $_GET;
    $content = $get['content'];
?>
<!DOCTYPE html>
<html>
<head>
    <title>北湖之道</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="bootstrap/bootstrap.min.css">
    <script src="bootstrap/jquery.min.js"></script>
    <script src="bootstrap/popper.min.js"></script>
    <script src="bootstrap/bootstrap.min.js"></script>
    <link rel="stylesheet" href="main.css">
</head>
<body>

<div class="container_result">
    <a href="index.php"><img src="image/logo.svg" class="logo"></a>
    <form class="form-inline input-form2" method="get" action="result.php">
        <input type="text" class="input-box form-control" id="input-box" name="content" placeholder="<?php echo $content;?>">
        <button type="submit" class="btn btn-outline-primary search-button">湖说</button>
    </form>
    <div class="container">
        <ul>
            <li>

            </li>
        </ul>
    </div>
</div>
<div class="footer" style="position: absolute;width: 100%;text-align: center;bottom:2vh">
    <hr color=#ccc width=61.8% style="text-align: center"/>
    <h6>Copyright © 2018 <a href='http://blog.defjia.top' style="color: black">DefJia</a>. All rights reserved. </h6>
</div>
</body>
</html>
