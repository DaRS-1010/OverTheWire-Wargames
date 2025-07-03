# 🧩Nivel 00 → Nivel 01

## 🎯 Objetivo ##

El propósito de este nivel es que aprendas a iniciar sesión en el entorno del juego utilizando el protocolo SSH.
Para hacerlo, deberás conectarte al servidor `bandit.labs.overthewire.org`, específicamente al puerto 2220.
🔐 Tanto el nombre de usuario como la contraseña son bandit0.

Una vez que hayas accedido correctamente al sistema remoto, puedes avanzar visitando la página del Nivel 1, donde encontrarás instrucciones para superar el siguiente reto.

## 🛠️ Solución ##
💻 Abre tu terminal y utiliza el protocolo de conexiones remotas SSH. 

⚠️ Aunque SSH usa por defecto el puerto 22, en este caso deberás usar el puerto 2220. 
Luego, especifica el nombre de usuario y el dominio del servidor al que deseas conectarte:.

     ssh bandit0@bandit.labs.overthewire.org -p 2220

__✅ Recuerda el esquema: protocolo usuario@host -opciones (si las necesitas)__

Ingresa la contraseña en este caso <code>bandit0</code>

## 🧭Navegación## 
- entramos como el usuario y host <code>bandit0@bandit</code>
- <code>ls</code> para listar y mirar que contenido tenemos dentro del host
- Podremos observar un archivo con el nombre <code>readme</code> ahora vamos a ver su
  contenido con <code>cat</code>
      
  Nos daran unas felicitaciones y el codigo para acceder al siguiente nivel:
  
<div align="center">

| 🔐 Contraseña |
|:-------------:|
| `ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If` ✅ |

</div>






