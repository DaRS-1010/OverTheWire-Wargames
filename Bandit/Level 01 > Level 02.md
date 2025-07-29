# 🧩Nivel 01 → Nivel 02

# 🎯 Objetivo 

Encontrar la contraseña del usuario bandit2. Está almacenada en un archivo llamado - ubicado en el home directory.

## 🧭Preparando el entorno
💻 Abre tu terminal y utiliza el protocolo de conexiones remotas SSH. 

     ssh bandit1@bandit.labs.overthewire.org -p 2220

Ingresa la contraseña en este caso <code>ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If</code>

## 🧭Navegación 
- si listamos con <code>ls</code> podremos observar un archivo llamado <code>-</code>

- la forma correcta de abrir el archivo es especificando el directorio en donde se encuentra almacenado el archivo

  `cd ./-`

- Esto nos daria como resultado la flag 🚩 del siguiente nivel

<div align="center">

| 🔐 Contraseña |
|:-------------:|
| `263JGJPfgU6LtdEvgfWU1XP5yac29mFx` ✅ |

</div>
