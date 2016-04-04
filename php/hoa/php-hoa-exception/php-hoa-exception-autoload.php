<?php
/* Autoloader for hoa/exception and its dependencies */

$vendor = '/usr/share/php';
// Dependencies
foreach ([
	$vendor . '/Hoa/Consistency/autoload.php'    => true,
	$vendor . '/Hoa/Event/autoload.php'          => true,
	] as $dep => $mandatory) {
	if ($mandatory || file_exists($dep)) require_once($dep);
}
$fedoraHoaLoader->addNamespace('Hoa\\Exception\\', __DIR__, true);

