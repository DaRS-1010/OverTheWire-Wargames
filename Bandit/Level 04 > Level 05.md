# 🧩Nivel 04 → Nivel 05

# 🎯 Objetivo

Encontrar el archivo que es legible por humanos entre muchos archivos que no lo son.

## 🧭Preparando el entorno

💻 Abre tu terminal y utiliza el protocolo de conexiones remotas SSH.

    ssh bandit4@bandit.labs.overthewire.org -p 2220

Ingresa la contraseña 🚩

## 🛠️ Guía práctica

- Una vez dentro del sistema, usamos el comando `ls -la` para listar todos los archivos, incluyendo los ocultos.
- Veremos un directorio llamado `inhere`, y dentro de él hay 10 archivos con nombres como `file00` hasta `file09`.
- Nuestro objetivo es identificar cuál de estos archivos contiene una posible flag, similar a las que ya hemos visto en niveles anteriores.
- Para leer estos archivos, utilizamos el comando `cat -- -file00`, repitiendo el proceso para cada archivo hasta encontrar el correcto.
- En este caso, al leer `file07`, obtendremos la flag 🚩 que corresponde al siguiente nivel.

<div align="center">

| 🔐 Contraseña |
|:-------------:|
| `4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw` ✅ |

</div>
