# 🧩Nivel 09 → Nivel 10

# 🎯 Objetivo

La clave para avanzar al siguiente nivel está guardada en el archivo data.txt, dentro de una de las pocas líneas que se pueden leer fácilmente, y que comienza con varios signos «=».

## 🧭Preparando el entorno

💻 Abre tu terminal y utiliza el protocolo de conexiones remotas SSH.

`ssh bandit9@bandit.labs.overthewire.org -p 2220`

Ingresa la contraseña 🚩

## 🛠️ Guía práctica

- Al listar los archivos del directorio, encontraremos un archivo llamado `data.txt`.
- Al revisar el contenido de ese archivo, veremos una larga lista de caracteres, por lo que será conveniente aplicar un filtro para facilitar su análisis.
- Para este caso, usaremos dos herramientas `strings` y `grep`
    
    `strings data.txt | grep '^=='`
    
    - `string`s > Extrae todas las cadenas de texto legibles (caracteres imprimibles) de un archivo, incluso si el archivo contiene datos binarios o no está en formato de texto plano.
    - `grep` > Busca líneas que **comienzan con el símbolo `=`** en la entrada que recibe.
    - Podremos observa la siguiente respuesta
    
            ========== the
            ========== password{k
            =========== is
            ========== FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey
    
    
- Esto nos daria como resultado la flag 🚩 del siguiente nivel

<div align="center">

| 🔐 Contraseña |
|:-------------:|
| `FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey` ✅ |

</div>
