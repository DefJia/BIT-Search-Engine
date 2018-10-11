<?php
    $get = $_GET;
	$content = $get['content'];
	include_once('Crawl.php');
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
    <style>
        body{
            background-color: #efe;
        }
    </style>
</head>
<body>
<div class="container_result container">
    <a href="index.php"><img src="image/logo.svg" class="logo"></a>
    <form class="form-inline input-form2" method="get" action="result.php">
        <input type="text" class="input-box form-control" id="input-box" name="content" placeholder="<?php echo $content;?>的搜索结果">
        <button type="submit" class="btn btn-outline-primary search-button">湖说</button>
    </form>
</div>

<div class="container">
    <ul>
<!--
        <li class="result">
            <a href="https://www.bit.edu.cn">北京理工大学</a>
            <h6>http://www.bit.edu.cn</h6>
            <p>【转载】奋力开创新时代教育工作新局面 北理工创新项目获首届中俄（工业）创新大赛二等奖  北理工举办2018年“一带一路”与国际化人才培养... 北理工成功举办国家自然科学基金仪器类项目交流会 北理工黄佳琦特别研究</p>
	</li>
-->
        <?php
            $cur = new Crawl();
            $cur->keyword = $content;
            $res = $cur->extract();
            for($i = 0; $i < 10; $i++) {
                $e = $res[$i];
                $li = sprintf('<li class="result"><a href="%s">%s</a><p>%s</p></li>', $e['a'], $e['title'], $e['p']);
                echo $li;
            }
        ?>
    </ul>
</div>

<div class="footer" style="width: 100%;text-align: center;bottom:2vh">
    <hr color=#ccc width=61.8% style="text-align: center"/>
    <h6>Copyright © 2018 <a href='https://github.com/DefJia' style="color: black">DefJia</a>. All rights reserved. </h6>
</div>
</body>
</html>
