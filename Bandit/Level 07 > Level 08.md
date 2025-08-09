# 🧩Nivel 07 → Nivel 08

# 🎯 Objetivo

La contraseña para el siguiente nivel se almacena en el archivo data.txt junto a la palabra millonésima

## 🧭Preparando el entorno

💻 Abre tu terminal y utiliza el protocolo de conexiones remotas SSH.

    ssh bandit7@bandit.labs.overthewire.org -p 2220

Ingresa la contraseña 🚩

## 🛠️ Guía práctica

- Si primero listamos el contenido del directorio, notaremos que hay un archivo llamado `data.txt`.
- Para este caso, usaremos la herramienta `grep`, que permite buscar texto dentro de archivos.
- Podemos consultar una guía rápida de uso con el comando **`man`**, que abre el **manual** de la herramienta.
- El comando que emplearemos será el siguiente:

    `grep ^millionth data.txt`

- Nos dará como resultado `millionth` `dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc`
    - Podemos refinar aún más esta salida utilizando la herramienta `awk`, de la siguiente manera:

        `awk '{print $2}`

        `'{print $2}'` > se utiliza para mostrar la **segunda columna o palabra** de cada línea del texto que se le pasa como entrada.

> 💡 Nota: `awk` es una herramienta de línea de comandos en Unix/Linux que sirve para procesar y **extraer columnas** de texto.

- Esto nos daria como resultado la flag 🚩 del siguiente nivel

<div align="center">

| 🔐 Contraseña |
|:-------------:|
| `dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc` ✅ |

</div>
