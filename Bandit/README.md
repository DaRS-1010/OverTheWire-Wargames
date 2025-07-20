![bandit](Assets/Bnt.jpg)

# Bandit 

Este repositorio documenta los niveles del reto **Bandit** de la plataforma [OverTheWire](https://overthewire.org/wargames/bandit/). 
Bandit está diseñado para ayudar a comprender los conceptos básicos de Linux, seguridad y terminal.

## 🎯 ¿Qué es Bandit?

> Bandit es un *wargame* para principiantes que enseña el uso básico de la terminal, navegación de archivos, permisos, SSH, y técnicas básicas de seguridad.
Ideal para quienes inician en el **hacking ético**, **ciberseguridad** o **administración de sistemas Linux**.

---
Cada nivel contiene:
- 🧠 Explicación paso a paso
- 💻 Comandos utilizados
- 🔑 Contraseña obtenida
- 📝 Notas adicionales

## 🚀 Cómo empezar

1. Visita: [https://overthewire.org/wargames/bandit/](https://overthewire.org/wargames/bandit/)
2. Lee la descripción del nivel.
3. Ve a la carpeta correspondiente en este repositorio.
4. Sigue los pasos y comandos descritos.
---

## 📁 Estructura del repositorio

Cada nivel está documentado en su propia carpeta:

| Nivel | Descripción | Enlace |
|-------|-------------|--------|
| Nivel 00 | Conexión SSH básica | [Ir a nivel00](./nivel00) |
| Nivel 01 | Leer archivo oculto | [Ir a nivel01](./nivel01) |
| Nivel 02 | Archivos con nombres especiales | [Ir a nivel02](./nivel02) |
| Nivel 03 | Archivos ocultos en carpetas ocultas | [Ir a nivel03](./nivel03) |

## ⚙️ Herramientas Utilizadas

| Herramienta | Descripción breve                            | Ejemplo de uso                                                      | Parámetros útiles                     |
| ----------- | -------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------- |
| `find`      | Busca archivos y directorios según criterios | `find / -type f -user bandit7 -group bandit6 -size 33c 2>/dev/null` | `-type f`, `-user`, `-group`, `-size` |
| `grep`      | Busca texto dentro de archivos               | `grep ^millionth data.txt`                                          | `^`, `-i`, `-r`                       |
| `sort`      | Ordena líneas de texto alfabéticamente       | `sort data.txt`                                                     | —                                     |
| `uniq`      | Filtra líneas duplicadas en texto ordenado   | `sort data.txt \| uniq -u`                                          | `-u` (únicos), `-d` (duplicados)      |
| `awk`       | Procesa texto por columnas o patrones        | `awk '{print $2}'`                                                  | `$1`, `$2`, `-F` (separador)          |
| `strings`   | Extrae cadenas de texto legibles de archivos binarios o mixtos | `strings archivo.bin`                             | `-a` escanea todo el archivo (no solo datos) |
| `base64`    | Codifica datos en formato Base64             | `base64 archivo.txt` `cat data.txt \| base64 --decode`              | `--decode` permite decodificar contenido codificado|

## 📬 Contacto

¿Dudas, aportes o correcciones? Puedes abrir un [Issue](https://github.com/) o hacer un Pull Request.


## ⚠️ Nota

⚠️ Este repositorio es solo para fines **educativos** y de **documentación personal**.  
No contiene contraseñas activas, y no fomenta el uso indebido de sistemas remotos.

---
