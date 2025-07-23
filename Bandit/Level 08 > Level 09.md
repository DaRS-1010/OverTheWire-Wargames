# 🧩Nivel 08 → Nivel 09
 
# 🎯 Objetivo

La contraseña para el siguiente nivel se almacena en el archivo data.txt y es la única línea de texto que aparece una sola vez

## 🛠️ Solución

💻 Abre tu terminal y utiliza el protocolo de conexiones remotas SSH.

    ssh bandit8@bandit.labs.overthewire.org -p 2220

Ingresa la contraseña 🚩

## 🧭Navegación

- Si primero listamos el contenido del directorio, notaremos que hay un archivo llamado `data.txt`.
- si miramos el contenido del archivo podremos observar una lista extensa de caracteres que será mejor filtrar
- Para este caso, usaremos la herramienta `sort`, que permite buscar texto dentro de archivos.
    
  `sort data.txt | uniq -u`
    
    -`sort data.txt` > Ordena el archivo para que las líneas iguales estén juntas.
    - `uniq -u` > Muestra solo las lineas que no estan repetidas

- Esto nos daria como resultado la flag 🚩 del siguiente nivel

<div align="center">

| 🔐 Contraseña |
|:-------------:|
| `4CKMh1JI91bUIZZPXDqGanal4xvAg0JM` ✅ |

</div>
