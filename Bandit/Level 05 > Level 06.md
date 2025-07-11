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

    - `find` → le dice a `find` Busca archivos/directorios desde el directorio actual **(.)**.
    - `-type f` Limita los resultados a archivos regulares (excluye directorios, enlaces, etc.).
    - `-size 1033c` Filtra los archivos cuyo **tamaño es exactamente 1033 bytes**, `c` significa "bytes" (caracteres).
    - `! -executable` Excluye los archivos que son ejecutables, El signo `!` es una negación.
    - `-exec file {} \;` Por cada archivo que cumpla los criterios anteriores, ejecuta el comando:
        - `file` intenta determinar el tipo de contenido del archivo (por ejemplo, texto ASCII, binario, imagen, etc.).
        - `{}` es un marcador de posición que representa cada archivo encontrado.
        - `\;` indica el final del comando -exec.
- esto nos dara como resultado

`./inhere/maybehere07/.file2: ASCII text, with very long lines (1000)`
visitamos la ruta y …

- Esto nos daria como resultado la flag 🚩 del siguiente nivel

<div align="center">

| 🔐 Contraseña |
|:-------------:|
| `HWasnPhtq9AVKe0dmk45nxy20cvUa6EG` ✅ |

</div>
