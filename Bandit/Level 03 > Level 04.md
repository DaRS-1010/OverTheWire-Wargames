# 🧩Nivel 03 → Nivel 04

## 🎯 Objetivo

Encontrar la contraseña del usuario bandit4. Está almacenada 
en un archivo oculto en el home directory.

## 🛠️ Solución

💻 Abre tu terminal y utiliza el protocolo de conexiones remotas SSH.

  `ssh bandit3@bandit.labs.overthewire.org -p 2220`

Ingresa la contraseña 🚩

## 🧭Navegación

- Una vez nos encontremos dentro del sistema vamos a utilizar el comando `ls -la`
- `l` (long): muestra la información en **formato largo**, es decir, cada archivo en una línea con detalles como permisos, propietario, tamaño, etc.
- `a` (all): muestra **todos los archivos**, incluyendo los **ocultos** (los que comienzan con `.`).

- encontraremos el archivo `inhere` y dentro de este el archivo …Hiding-From-You
- utilizamos `cat` para observar el contenido del archivo
- Esto nos daria como resultado la flag 🚩 del siguiente nivel

<div align="center">

| 🔐 Contraseña |
|:-------------:|
| `2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ` ✅ |

</div>
