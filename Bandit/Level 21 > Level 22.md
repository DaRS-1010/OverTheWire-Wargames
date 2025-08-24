# 🧩Nivel 21→ Nivel 22

# 🎯 Objetivo

Un programa se ejecuta automáticamente a intervalos regulares desde cron, el programador de tareas basado en tiempo. Busque la configuración en /etc/cron.d/ y vea qué comando se está ejecutando.

## 🧭Preparando el entorno

💻 Abre tu terminal y utiliza el protocolo de conexiones remotas SSH.

`ssh bandit21@bandit.labs.overthewire.org -p 2220`

Ingresa la contraseña 🚩

## 🛠️ Guía práctica

- Una vez dentro nos dirigimos al directorio `/etc/cron.d` y listamos su contenido:
    
    ```
    cd /etc/cron.d
    ls -l
    ```
    
- Obtendremos varios ficheros, pero el que nos interesa es `cronjob_bandit22`.
- si miramos el contenido de este fichero nos mostrara el siguiente resultado:
    
    ```
    @reboot bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
    * * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
    ```
    
- Esto nos dice que cada minuto se ejecuta el script `/usr/bin/cronjob_bandit22.sh`.
- y si ahora nos dirigimos a ese directorio y mostramos su contenido nos dará el siguiente resultado:
    
    ```
    #!/bin/bash
    chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
    cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
    ```
    
- El script lo que hace es copiar la contraseña de bandit22 al archivo temporal `/tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv`.
- veamos el contenido de la copia con el siguiente comando:
    
    ```
    cat  /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
    ```
    
- Esto nos daria como resultado la flag 🚩 del siguiente nivel `bandit22`

<div align="center">

| 🔐 Contraseña |
|:-------------:|
| `tRae0UfB9v0UzbCdn9cY0gQnds9GF58Q` ✅ |

</div>
