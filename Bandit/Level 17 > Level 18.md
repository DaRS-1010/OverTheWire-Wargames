# 🧩Nivel 17 → Nivel 18

# 🎯 Objetivo

Hay dos archivos en el directorio de inicio: passwords.old y passwords.new. La contraseña para el siguiente nivel está en passwords.new y es la única línea que se ha cambiado entre passwords.old y passwords.new.

## 🧭Preparando el entorno

💻 Abre tu terminal y utiliza el protocolo de conexiones remotas SSH.

`ssh bandit17@bandit.labs.overthewire.org -p 2220`

Ingresa la contraseña 🚩

## 🛠️ Guía práctica

- Una vez tengamos accesos encontraremos dos archivos `passwords.old` y `passwords.new`
- vamos  a utilizar `diff` para comparar ambos archivos
    
    `diff passwords.old passwords.new`
  
- podremos observar lo siguiente
    
    ```
    42c42
    < gvE89l3AhAhg3Mi9G2990zGnn42c8v20 (Pass old)
    ---
    > x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO (pass new)
    
    ```
    
- Esto nos daria como resultado la flag 🚩 del siguiente nivel `bandit18`


<div align="center">

| 🔐 Contraseña |
|:-------------:|
| `x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO` ✅ |

</div>
