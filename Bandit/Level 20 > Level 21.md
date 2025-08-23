# 🧩Nivel 20 → Nivel 21

# 🎯 Objetivo

Hay un binario setuid en el directorio personal que realiza lo siguiente: establece una conexión con localhost en el puerto especificado como argumento de línea de comandos. Luego, lee una línea de texto de la conexión y la compara con la contraseña del nivel anterior (bandit20). Si la contraseña es correcta, transmite la contraseña del siguiente nivel (bandit21).

NOTA: Intenta conectarte a tu propio daemon de red para comprobar si funciona como esperas

## 🧭Preparando el entorno

💻 Abre tu terminal y utiliza el protocolo de conexiones remotas SSH.

`ssh bandit20@bandit.labs.overthewire.org -p 2220`

Ingresa la contraseña 🚩

##  🛠️ Guía práctica

- Tenemos un binario con el nombre de `suconnect`. Si lo ejecutamos sin un parámetro nos dará la siguiente respuesta:
    
    `Usage: ./suconnect <portnumber>`
    
- Como primer paso vamos a preparar un servidor que escuche en `localhost:3232`. En algunas versiones de `nc`, el comando `nc -l -p 3232` no escucha en la dirección correcta, por lo que es más seguro usar: `nc -l -p 3232`
    
- Ahora sí podemos ejecutar el binario, indicándole el puerto que especificamos para escuchar conexiones TCP:
    
    `./suconnect 3232`
    
- En este punto, el binario se conectará a nuestro servidor netcat, 
En la terminal donde tienes `nc`, pega la contraseña de **bandit20** y presiona **Enter**.
- Esto nos daria como resultado la flag 🚩 del siguiente nivel `bandit21`

<div align="center">

| 🔐 Contraseña |
|:-------------:|
| `EeoULMCra2q0dSkYj561DX7s1CpBuOBt` ✅ |

</div>
