# 🧩Nivel 10 → Nivel 11

# 🎯 Objetivo

La contraseña para el siguiente nivel se almacena en el archivo data.txt, que contiene datos codificados en `base64`

## 🧭Preparando el entorno

💻 Abre tu terminal y utiliza el protocolo de conexiones remotas SSH.

`ssh bandit10@bandit.labs.overthewire.org -p 2220`
     
Ingresa la contraseña 🚩

## 🛠️ Guía práctica

- Al listar los archivos del directorio, encontraremos un archivo llamado `data.txt`.
- Dentro de este encontramos un string encriptada con base64
- Para este caso, usaremos dos herramientas `cat` y `base64`
    
    `cat data.txt | base64 --decode`

    - `cat` > se utiliza para unir o visualizar el contenido de uno o varios archivos.
    - `base64` > Codifica o decodifica datos en formato Base64**
    - Podremos observa la siguiente respuesta
- Esto nos daria como resultado la flag 🚩 del siguiente nivel

<div align="center">

| 🔐 Contraseña |
|:-------------:|
| `dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr` ✅ |

</div>
