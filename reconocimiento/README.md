# OSCP reconocimiento

En esta sección se incluyen distintos comandos preparados para funcionar de forma directa con los recursos disponibles en Kali linux y en el arbol de directorios incluido.

## Comandos de reconocimiento

Los siguientes comandos pueden ser empleados para realizar un reconocimiento de servicios: (Hacer export TARGET=IP_objetivo)
  
### NMAP

1) Escaneo NMAP                        -->  `nmap -sV -O -Pn -p- --script auth --script vuln -v $TARGET`

### SSH

2) Enumeración de usuarios SSH         -->  `python ssh/users-enum.py  --username root $TARGET`

### SAMBA

3) Reconocimiento SMB version          -->  `smb/smb-version.sh $TARGET`

4) Conexion SMB client                 -->  `smbclient -L $TARGET -N`

5) Enum4linux                          -->  `enum4linux $TARGET` 

### WEB

6) Dirbuster                           --> __HTTP__ `dirb /usr/share/dirb/wordlist/big.txt http://$TARGET`        
 __HTTPS__ `dirb /usr/share/dirb/wordlist/big.txt https://$TARGET` 
                                       
                                        
