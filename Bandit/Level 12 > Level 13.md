# # 🧩Nivel 12 → Nivel 13

# # 🎯 Objetivo

La contraseña para el siguiente nivel está almacenada en el archivo `data.txt`, el cual es un volcado hexadecimal (hexdump) de un archivo que ha sido comprimido repetidamente.

Para resolver este nivel, puede ser útil crear un directorio temporal en `/tmp` donde puedas trabajar. Usa el comando `mkdir` con un nombre de directorio difícil de adivinar, o mejor aún, utiliza el comando `mktemp -d` para generar automáticamente un directorio temporal seguro. Luego, copia el archivo de datos usando `cp` y cámbiale el nombre con `mv` (consulta las páginas del manual con `man` si es necesario).

## 🛠️ Solución

💻 Abre tu terminal y utiliza el protocolo de conexiones remotas SSH.

```
 ssh bandit12@bandit.labs.overthewire.org -p 2220
```

Ingresa la contraseña 🚩

- Al listar los archivos del directorio, encontraremos un archivo llamado `data.txt`.
- Dentro de este archivo está un volcado hexadecimal (hexdump)
- Vamos hacer el proceso que nos pide la guia, crear un directorio temporal
  
      mkdir /tmp/banditemp/
      cp data.txt /tmp/banditemp/
      cd /tmp/banditemp/
    
> **Nota:**
   🌐 En el nivel 12, el archivo data.txt
    **no está en binario crudo**, sino en texto que representa un volcado hexadecimal.
    Antes de poder descomprimir nada, necesitas **reconstruir el binario original**
    a partir del texto hexadecimal.

    
- con esto en mente vamos a reconstruir el binario original ha partir de texto hexadecimal
    
    `xxd -r data.txt > data `
    
- esto nos dara el archivo data, y vamos a ver que tipo de archivo es con file
    
    `file data
    resultado: data: gzip compressed data, was "data2.bin", last modified: Mon Jul 28 19:03:31 2025, max compression, from Unix, original size modulo 2^32 574`
    
- tenemos que ir verificando cada archivo con file, renombrar con mv y descomprimir con su formato.

> 📦 Tipos de formatos y cómo tratarlos
> 
> 
> | **Salida del comando `file`** | **Extensión sugerida** | **Comando para descomprimir** |
> | --- | --- | --- |
> | `gzip compressed data` | `.gz` | `gunzip archivo.gz` |
> | `bzip2 compressed data` | `.bz2` | `bunzip2 archivo.bz2` |
> | `POSIX tar archive` | `.tar` | `tar -xf archivo.tar` |
> | `Zip archive data` | `.zip` | `unzip archivo.zip` |
> | `XZ compressed data` | `.xz` | `unxz archivo.xz` |
> | `LZMA compressed data` | `.lzma` | `unlzma archivo.lzma` |
> | `ASCII text` o `UTF-8 text` | `.txt` | Abrir con `cat archivo.txt` o `less` |
> | `data` (sin más info) | (depende) | Volver a probar `file` o hexeditor |
> | `hexdump` (texto con hex) | `.txt` | `xxd -r archivo.txt > archivo_bin` |

---

- sigamos el siguiente proceso 

```c

mv data data.gz
gunzip data.gz

file data : "data: bzip2 compressed data, block size = 900k"

mv data data.bz2
bunzip2 data.bz2

file data : "data: gzip compressed data, was "data4.bin", last modified: Mon Jul 28 19:03:31 2025, max compression, from Unix, original size modulo 2^32 20480
"

mv data data.gz
gunzip data.gz 

file data: "data: POSIX tar archive (GNU)"

mv data data.tar
tar -xf data.tar = "data5.bin"

file data5.bin : "data5.bin: POSIX tar archive (GNU)"

mv data5.bin data5.tar 
tar -xf data.tar = "data6.bin"

file data6.bin : "data6.bin: bzip2 compressed data, block size = 900k"

mv data6.bin data.bz2
bunzip2 data.bz2

file data : "data: POSIX tar archive (GNU)"

mv data data.tar
tar -xf data.tar = "data8.bin"

file data8.bin: "data8.bin: gzip compressed data, was "data9.bin", last modified: Mon Jul 28 19:03:31 2025, max compression, from Unix, original size modulo 2^32 49
"

mv data8.bin data.gz
gunzip data.gz

file data: data: ASCII text
cat data

```

Esto nos daria como resultado la flag 🚩 del siguiente nivel

<div align="center">

| 🔐 Contraseña |
|:-------------:|
| `FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn` ✅ |

</div>
