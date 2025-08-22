# 🧩Nivel 19 → Nivel 20

# 🎯 Objetivo

Para acceder al siguiente nivel, debe usar el binario setuid en el directorio personal. Ejecútelo sin argumentos para saber cómo usarlo. 
La contraseña para este nivel se encuentra en el directorio habitual (/etc/bandit_pass), después de usar el binario setuid.

## 🧭Preparando el entorno

💻 Abre tu terminal y utiliza el protocolo de conexiones remotas SSH.

`ssh bandit19@bandit.labs.overthewire.org -p 2220`

Ingresa la contraseña 🚩

## 🛠️ Guía práctica

- Contamos con un **binario con SUID** (es decir, un ejecutable al que se le ha asignado el permiso especial *Set User ID*).
- Gracias a que el binario tiene **SUID**, podemos usarlo como un *wrapper*, es decir, ejecutar comandos con los privilegios de su propietario en lugar de los nuestros.
- vamos a ejecutar el siguiente comando
    
    `./bandit20-do cat /etc/bandit_pass/bandit20`
    
    - El binario `bandit20-do` recibe el comando `cat /etc/bandit_pass/bandit20`.
    - Como corre con permisos de `bandit20`, puede acceder a ese archivo.
    - Entonces, **te muestra en pantalla la contraseña de bandit20**, aunque tú sigas logueado como `bandit19`.
- Esto nos daria como resultado la flag 🚩 del siguiente nivel `bandit20`

<div align="center">

| 🔐 Contraseña |
|:-------------:|
| `0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO` ✅ |

</div>
