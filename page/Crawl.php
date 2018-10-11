<?php
/**
 * Created by PhpStorm.
 * User: defjia
 * Date: 18-10-11
 * Time: 上午10:26
 */

require ('simplehtmldom/simple_html_dom.php');
class Crawl{
    var $keyword;

    function __construct(){
    }

    function get(){
        $url = sprintf('http://www.bit.edu.cn/cms/search/searchResults.jsp?date=&query=%s&offset=0&sortField=publishDate&order=1', $this->keyword);
        $url = 'http://www.bitren.com';
        $html = file_get_html($url);
        return $html;
    }

    function extract(){
        $html = $this->get();
        foreach($html->find('a') as $element)
            echo $element->src . '<br>';
    }
}

$cur = new Crawl();
$cur->keyword = 's';
# $cur->extract();
$url = 'http://www.bitren.com';
$html = file_get_html($url);
var_dump($html);
