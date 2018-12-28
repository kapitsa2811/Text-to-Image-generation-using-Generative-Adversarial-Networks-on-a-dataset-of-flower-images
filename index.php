<?php  
header('Access-Control-Allow-Origin: *');
define('ROOTPATH', dirname(__FILE__));
$output = exec('python test.py');
echo $output;

?>