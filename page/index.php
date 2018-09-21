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
    <style>
        body{
            background: url("image/bg.jpg") no-repeat;
            background-size:cover;
        }
    </style>
</head>
<body>

<div class="container_index container">
    <div class="wrap">
        <div class="icon icon-red"></div>
    </div>
    <!--
        <img src="image/logo.svg" class="logo"/>
    -->
    <form class="form-inline input-form" method="get" action="result.php">
        <input type="text" class="input-box form-control" id="input-box" name="content" placeholder="我想问北湖..." style="width: 30%">
        <button type="submit" class="btn btn-light search-button">湖说</button>
    </form>
</div>
<div class="footer" style="position: absolute;width: 100%;text-align: center;bottom:2vh">
    <hr color=#ccc width=61.8% style="text-align: center"/>
    <h6 style="color: white">Copyright © 2018 <a href='http://blog.defjia.top' style="color: white">DefJia</a>. All rights reserved. </h6>
</div>
</body>
</html>