# 🧩Nivel 11 → Nivel 12

# 🎯 Objetivo

La contraseña para el siguiente nivel se almacena en el archivo data.txt, donde todas las letras minúsculas (a-z) y mayúsculas (A-Z) se han girado 13 posiciones

## 🛠️ Solución

💻 Abre tu terminal y utiliza el protocolo de conexiones remotas SSH.

    ssh bandit11@bandit.labs.overthewire.org -p 2220
    
Ingresa la contraseña 🚩

## 🧭Navegación

- Al listar los archivos del directorio, encontraremos un archivo llamado `data.txt`.
- Dentro de este archivo está la contraseña cifrada con ROT13, un cifrado que desplaza cada letra 13 posiciones en el alfabeto.
- Para descifrarla, usaremos la herramienta `tr` junto con `cat` de la siguiente manera:

  `cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'`

  - `cat` > se utiliza para mostrar o concatenar el contenido de archivos.
  - `tr` > traduce o reemplaza caracteres, en este caso aplica el cifrado ROT13.
  - Esto nos daria como resultado la flag 🚩 del siguiente nivel

<div align="center">

| 🔐 Contraseña |
|:-------------:|
| `7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4` ✅ |

</div>

> **Nota:** El cifrado ROT13 funciona bien de por si solo, pero si le pasamos algún otro valor este puede llegar a presentar errores 

> **Nota:** Script en Python que permite cifrar o descifrar texto aplicando un desplazamiento variable de caracteres según el cifrado César.
El usuario puede ingresar el texto, elegir la acción (cifrar o descifrar) y especificar el número de posiciones para el desplazamiento. [`Here`](Codes/)
