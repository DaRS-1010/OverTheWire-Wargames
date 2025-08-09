# 🧩Nivel 06 → Nivel 07

# 🎯 Objetivo

La contraseña del próximo nivel se encuentra en algún lugar dentro del servidor y cumple con todas las siguientes características.

- propiedad del usuario bandit7
- propiedad del grupo bandit6
- 33 bytes de tamaño

## 🧭Preparando el entorno

💻 Abre tu terminal y utiliza el protocolo de conexiones remotas SSH.

```
 ssh bandit6@bandit.labs.overthewire.org -p 2220
```

Ingresa la contraseña 🚩

## 🛠️ Guía práctica

- De una forma rapida podemos empezar a filtrar con las condiciones que nos dieron
    
    podemos utilizar el siguiente comando 
    
    ```visual-basic
    find / -type f -user bandit7 -group bandit6 -size 33c 2>/dev/null
    ```
    
    - `/` → lo usamos con find para analizar la información desde la raiz
    - `-type f` → tipo de archivo
        
       | Opción    | Significado               |
       | --------- | ------------------------- |
       | `-type f` | **Archivo regular**       |
       | `-type d` | Directorio                |
       | `-type l` | Enlace simbólico          |
       | `-type s` | Socket                    |
       | `-type p` | FIFO (pipe con nombre)    |
       | `-type b` | Dispositivo en bloque     |
       | `-type c` | Dispositivo de caracteres |
      
    - `-user bandit7` → pertenecientes al usuario `bandit7`
    - `-group bandit6` → del grupo `bandit6`
    - `-size 33c` → con tamaño de 33 bytes (c = bytes)
    - `2>/dev/null`: ignora errores de permisos
- esto nos dara como resultado

`/var/lib/dpkg/info/bandit7.password`

visitamos la ruta y …

- Esto nos daria como resultado la flag 🚩 del siguiente nivel
<div align="center">

| 🔐 Contraseña |
|:-------------:|
| `morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj` ✅ |

</div>



