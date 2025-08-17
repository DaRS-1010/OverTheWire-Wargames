# 🧩Nivel 14 → Nivel 15

# 🎯 Objetivo

La contraseña para el siguiente nivel se puede recuperar enviando la contraseña del nivel actual al puerto 30000 en localhost.

## 🧭Preparando el entorno

💻 Abre tu terminal y utiliza el protocolo de conexiones remotas SSH.

  `ssh bandit14@bandit.labs.overthewire.org -p 2220`

Ingresa la contraseña 🚩

## 🛠️ Guía práctica**

- probamos la conexión al puerto 30000
    
    `nc localhost 30000`
  
- nc localhost 30000 abre una conexión TCP al puerto 30000 de tu máquina; envías tu contraseña `bandit14`, el servicio la valida y devuelve la clave del siguiente nivel en pantalla. 
- Esto nos daria como resultado la flag 🚩 del siguiente nivel `bandit15`


<div align="center">

| 🔐 Contraseña |
|:-------------:|
| `8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo` ✅ |

</div>
