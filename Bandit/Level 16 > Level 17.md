# 🧩Nivel 16 → Nivel 17

# 🎯 Objetivo

Las credenciales para el siguiente nivel se pueden obtener enviando la contraseña del nivel actual a un puerto del host local en el rango 31000-32000. Primero, determine cuáles de estos puertos tienen un servidor escuchando. Luego, determine cuáles admiten SSL/TLS y cuáles no. Solo un servidor proporcionará las siguientes credenciales; los demás simplemente le enviarán lo que usted les envíe.

## 🧭Preparando el entorno

💻 Abre tu terminal y utiliza el protocolo de conexiones remotas SSH.

`ssh bandit16@bandit.labs.overthewire.org -p 2220`

Ingresa la contraseña 🚩

## 🛠️ Guía práctica

- Vamos a utilizar la herramienta nmap para analizar los puertos
    
    `nmap -p31000-32000 localhost`
    
- esto nos dara los siguientes puertos abiertos `31046`, `31518`, `31691`, `31790`, `31960`.
- podemos utilizar un escaneo mas profundo con nmap para tener mas información
    
    `Nmap -A localhost -p 31000-32000`
    
- nos dará como resultado la siguiente información
    
    ```
    31790/tcp open  ssl/unknown
    |_ssl-date: TLS randomness does not represent time
    | ssl-cert: Subject: commonName=SnakeOil
    | Not valid before: 2024-06-10T03:59:50
    |_Not valid after:  2034-06-08T03:59:50
    | fingerprint-strings: 
    |   FourOhFourRequest, GenericLines, GetRequest, HTTPOptions, Help, LPDString, RTSPRequest, SIPOptions: 
    |_    Wrong! Please enter the correct current password.
    ```
    
    probamos la conexión por SSL/TLS  mediante netcat con el siguiente comando
    
    `ncat --ssl localhost 31790`
    
- Cuando te conectas con `ncat --ssl localhost <PUERTO>` y escribes la contraseña de tu nivel actual, el servicio te responderá con una **clave privada SSH** (un bloque de texto que empieza con `-----BEGIN RSA PRIVATE KEY-----` y termina con `-----END RSA PRIVATE KEY-----`).
- Copia todo ese bloque y pégalo en un archivo nuevo, por ejemplo: `key17`
- Proteger el archivo con permisos correctos SSH no permite usar claves privadas con permisos abiertos, para protegerla, ejecuta `chmod 600 key17`
- Ahora ya puedes conectarte al siguiente usuario con:
    
    `ssh -i key17 -p 2220 bandit17@bandit.labs.overthewire.org`
    
- Vamos al archivo que almacena la contraseña del usuario **bandit17**, ubicado en `/etc/bandit_pass/bandit17`.
- Esto nos daria como resultado la flag 🚩 del siguiente nivel `bandit17`

<div align="center">

| 🔐 Contraseña |
|:-------------:|
| `EReVavePLFHtFlFsjn3hyzMlvSuSAcRD` ✅ |

</div>
