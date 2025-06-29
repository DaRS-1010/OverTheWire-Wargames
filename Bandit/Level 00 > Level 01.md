# Nivel 00 > nivel 01

## Objectivo
El propósito de este nivel es que aprendas a iniciar sesión en el entorno del juego utilizando el protocolo `SSH`.  
Para hacerlo, deberás conectarte al servidor `bandit.labs.overthewire.org`, específicamente al puerto `2220`.  
Tanto el nombre de usuario como la contraseña son `bandit0`.

Una vez que hayas accedido correctamente al sistema remoto, puedes avanzar visitando la página del [Nivel 1](https://overthewire.org/wargames/bandit/bandit1.html), donde encontrarás instrucciones para superar el siguiente reto.

## Solution

1. Abre tu terminal y, a continuación, utiliza el protocolo de conexiones remotas SSH.
    Aunque SSH suele operar por defecto en el puerto 22, en este caso deberás usar el puerto 2220.
    Luego, especifica el nombre de usuario y el dominio del servidor al que deseas conectarte.
    `ssh bandit0@bandit.labs.overthewire.org -p 2220`

### Recuerda el esquema: protocolo user@host -utilidades (si las necesitas)###

2. Ingresa la contraseña en este caso <code>bandit0</code>

3. ## Navegación ##
    - entramos como el usuario <code>bandit0@bandit</code> user: bandit0 y host: bandit
    - <code>ls</code> para listar y mirar que contenido tenemos dentro del host
    - Podremos observar un archivo con el nombre <code>readme</code> ahora vamos a ver su
      contenido con <code>cat</code>
      
      Nos daran unas felicitacione y el codigo para acceder al siguiente nivel: 
      |Contraseña| ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If | 
      

      







