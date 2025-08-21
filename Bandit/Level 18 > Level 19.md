# 🧩Nivel 18 → Nivel 19

# 🎯 Objetivo

La contraseña para el siguiente nivel se almacena en un archivo "readme" en el directorio personal. Lamentablemente, alguien modificó el archivo .bashrc para cerrar sesión al iniciar sesión con SSH.

## 🧭Preparando el entorno

💻 Abre tu terminal y utiliza el protocolo de conexiones remotas SSH.

`ssh bandit18@bandit.labs.overthewire.org -p 2220`

Ingresa la contraseña 🚩

## 🛠️ Guía práctica

- No es posible abrir una sesión interactiva porque la conexión se cierra automáticamente debido a la configuración en `.bashrc`.
- Por esta razón, debemos ejecutar los comandos de forma remota utilizando **ssh**, de la siguiente manera:
    
    `ssh bandit18@bandit.labs.overthewire.org -p 2220 "<comando>"`
    
- Para ir al grano, dentro de la carpeta *home* se encuentra un archivo llamado `readme`. Podemos visualizarlo con el siguiente comando:
    
    `ssh bandit18@bandit.labs.overthewire.org -p 2220 "cat readme"`
    
- Esto nos daria como resultado la flag 🚩 del siguiente nivel `bandit19`

<div align="center">

| 🔐 Contraseña |
|:-------------:|
| `cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8` ✅ |

</div>
