# 🧩Nivel 02 → Nivel 03

## 🎯 Objetivo

Encontrar la contraseña del usuario bandit3. Está almacenada en un archivo llamado “spaces in this filename”ubicado en el home directory.

## 🛠️ Solución

💻 Abre tu terminal y utiliza el protocolo de conexiones remotas SSH.

  `ssh bandit2@bandit.labs.overthewire.org -p 2220`

Ingresa la contraseña 🚩

## 🧭Navegación

- si listamos con <code>ls</code> podremos observar un archivo llamado <code>spaces in this filename</code>
- En este caso nos encontramos con espacio entre el nombre del archivo el cual afecta su llamado en shell
- La forma correcta de observar el contenido del archivo es atreves de las comillas
    
   `cat "spaces in this filename"`
   
- Esto nos daria como resultado la flag 🚩 del siguiente nivel

<div align="center">

| 🔐 Contraseña |
|:-------------:|
| `MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx` ✅ |

</div>
