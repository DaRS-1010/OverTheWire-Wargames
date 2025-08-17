# 🧩Nivel 13 → Nivel 14

# 🎯 Objetivo

La contraseña para el siguiente nivel se almacena en /etc/bandit_pass/bandit14 y solo puede ser leída por el usuario bandit14. Para este nivel,
no se obtiene la siguiente contraseña, sino una clave SSH privada que permite iniciar sesión en el siguiente nivel. Nota: localhost es un nombre 
de host que se refiere a la máquina en la que se está trabajando.

## 🧭Preparando el entorno

💻 Abre tu terminal y utiliza el protocolo de conexiones remotas SSH.

 `ssh bandit13@bandit.labs.overthewire.org -p 2220`

Ingresa la contraseña 🚩

## 🛠️ Guía práctica

- Al listar los archivos del directorio, encontraremos un archivo llamado `sshkey.private` , tipo de archivo : PEM RSA private key
- tenemos que darle privilegios al archivo `sshkey.private` con el comando 

      chmod 600 sshkey.private

- una vez tengamos listo el archivo vamos a conectarnos via ssh a [localhost](http://localhost) como el usuario bandit14
    
      ssh -i ./sshkey.private -p 2220 bandit14@localhost
    
- una vez dentro nos dirigimos hacia la ruta que nos dan el objetivo `/etc/bandit_pass/`  y copiamos la clave del archivo bandit14
- Esto nos daria como resultado la flag 🚩 del siguiente nivel

<div align="center">

| 🔐 Contraseña |
|:-------------:|
| `MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS` ✅ |

</div>
