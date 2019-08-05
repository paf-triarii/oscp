Los siguientes comandos pueden ser empleados para realizar un reconocimiento de servicios: (Hacer export TARGET=<IP-maquina-objetivo>)

1) Escaneo NMAP                        -->  nmap -sV -O -Pn -p- --script auth --script vuln -v $TARGET

[SSH]

2) Enumeración de usuarios SSH         -->  python $OSCP/reconocimiento/ssh/users-enum.py  --username root $TARGET

[SAMBA]

3) Reconocimiento SMB version          -->  $OSCP/reconocimiento/smb/smb-version.sh $TARGET

4) Conexion SMB client                 -->  smbclient -L $TARGET -N

5) Enum4linux                          -->  enum4linux $TARGET 

[WEB]

6) Listado de directorios existentes   -->  dirb http://$TARGET:<PORT> <wordlists.txt> -o dirb.txt

7) Escaner de la web                   --> nikto -h http://$TARGET:<PORT> -o nikto.txt
  
8) DAV                                 --> cadaver htp://$TARGET:<PORT>  
  
9) Escáner para WordPress              --> wpscan --url http://$TARGET:<PORT>
