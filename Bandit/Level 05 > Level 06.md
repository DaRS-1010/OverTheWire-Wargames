# 🧩Nivel 05 → Nivel 06

# 🎯 Objetivo

La contraseña del siguiente nivel está guardada en un archivo ubicado en algún lugar dentro del directorio actual. Este archivo cumple con todas las siguientes condiciones:

- Su contenido es legible por humanos.
- Tiene un tamaño exacto de 1033 bytes.
- No tiene permisos de ejecución.

## 🛠️ Solución

💻 Abre tu terminal y utiliza el protocolo de conexiones remotas SSH.

`ssh bandit5@bandit.labs.overthewire.org -p 2220`

Ingresa la contraseña 🚩

## 🧭Navegación

- De una forma rapida podemos empezar a filtrar con las condiciones que nos dieron
    
    podemos utilizar el siguiente comando 
    

      find . -type f -size 1033c ! -executable -exec file {} \; 

    
    - `exec` → le dice a `find` que **ejecute un comando** para cada archivo que encuentre.
    - `file` → es el comando que se va a ejecutar. En este caso, `file` analiza el tipo de contenido del archivo.
    - `{}` → representa **el nombre del archivo encontrado**.
    - `\;` → finaliza el `exec` (es obligatorio; el punto y coma debe ir escapado con `\` para que Bash no lo interprete mal).
- esto nos dara como resultado

`./inhere/maybehere07/.file2: ASCII text, with very long lines (1000)`
visitamos la ruta y …

- Esto nos daria como resultado la flag 🚩 del siguiente nivel
