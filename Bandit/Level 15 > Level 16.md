# 🧩Nivel 15 → Nivel 16

# 🎯 Objetivo

La contraseña del siguiente nivel se puede recuperar enviando la contraseña del nivel actual al puerto 30001 del host local mediante cifrado SSL/TLS.

## 🧭Preparando el entorno

💻 Abre tu terminal y utiliza el protocolo de conexiones remotas SSH.

`ssh bandit15@bandit.labs.overthewire.org -p 2220`

Ingresa la contraseña 🚩

## 🛠️ Guía práctica

- para utilizar la comunicación cifrada utilizamos un cliente SSL en este caso openssl y ejecutamos el siguiente comando
    
    `openssl s_client -connect localhost:30001`
    
- Verás que se abre una conexión y aparecen certificados y handshakes, cuando quede esperando input pega tu contraseña de bandit15 y presiona enter
- Esto nos daria como resultado la flag 🚩 del siguiente nivel `bandit16`

<div align="center">

| 🔐 Contraseña |
|:-------------:|
| `kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx` ✅ |

</div>
