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
	    $html = file_get_html($url);
        return $html;
    }

    function extract(){
	    $html = $this->get();
	    $res = $html->find('.con03')[0];
		$as = $res->find('a');
	    $cur = array();
	    $i = 0;
	    foreach ($as as $a){
		    $cur[$i] = array('a'=>$a->href);
		    $cur[$i]['title'] = $a->plaintext;
		$i ++;
	    }
	    $ps = $res->find('p');
	    $i = 0;
	    foreach($ps as $p){
		    $cur[$i]['p'] = $p->plaintext;
		    $i++;
	    }
	    return $cur;
    }
}
/*
$cur = new Crawl();
$cur->keyword = 's';
# $cur->extract();
$url = 'http://www.bitren.com';
$html = file_get_html($url);
 */
