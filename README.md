# Analizador Léxico - Lenguaje Personalizado

Este proyecto es un analizador léxico desarrollado en Python. Analiza línea por línea un archivo fuente de texto (`fuente.txt`) y reconoce tokens definidos por un lenguaje personalizado.

## 📌 Estructura del Lenguaje

Este lenguaje incluye:

- **Palabras reservadas** como `var`, `if`, `loop`, `endloop`, `endif`, `show`, `start_main`, `endmain`.
- Declaraciones de variables: `var edad = 25`
- Ciclos: `loop`, `endloop`
- Condicionales: `if`, `endif`
- Impresiones: `show("Hola mundo")`
- Bloques principales: `start_main`, `endmain`

## ✅ Tokens que reconoce

| Token        | Significado                        | Ejemplo                |
|--------------|------------------------------------|------------------------|
| `RESERVADA`  | Palabra clave del lenguaje         | `var`, `loop`, `if`    |
| `ID`         | Identificadores                    | `contador`, `nombre`   |
| `NUMBER`     | Números (enteros o decimales)      | `10`, `3.14`           |
| `STRING`     | Cadenas entre comillas             | `"Hola mundo"`         |
| `EQ`         | Igualdad (`==`)                    | `a == b`               |
| `NE`         | Diferente (`!=`)                   | `a != b`               |
| `LE`         | Menor o igual (`<=`)               | `a <= b`               |
| `GE`         | Mayor o igual (`>=`)               | `a >= b`               |
| `EQUALS`     | Asignación (`=`)                   | `x = 5`                |
| `LT`         | Menor que (`<`)                    | `x < y`                |
| `GT`         | Mayor que (`>`)                    | `x > y`                |
| `NOT`        | Negación (`!`)                     | `!true`                |
| `PLUS`       | Suma (`+`)                         | `x + y`                |
| `MINUS`      | Resta (`-`)                        | `x - y`                |
| `TIMES`      | Multiplicación (`*`)               | `x * y`                |
| `DIVIDE`     | División (`/`)                     | `x / y`                |
| `LPAREN`     | Paréntesis izquierdo (`(`)         | `(`                    |
| `RPAREN`     | Paréntesis derecho (`)`)           | `)`                    |

## ⚠️ Errores léxicos

Si el analizador encuentra un carácter no reconocido por el lenguaje, lo reporta indicando la línea y el símbolo problemático.

## 🧪 Cómo usar

1. Escribe tu código en `fuente.txt`.
2. Ejecuta el archivo `analizador.py`:
```bash
python analizador.py
```
3. El programa imprimirá el resultado línea por línea en consola.

## ✍️ Ejemplo de fuente.txt

```plaintext
start_main
var edad = 25
show("Hola mundo")
loop
    edad = edad + 1
endloop
endmain
```

## ℹ️ Notas finales

- Las **palabras reservadas** se reconocen automáticamente y se clasifican como `RESERVADA`, incluso si coinciden con la expresión regular de un `ID`.
- Los espacios y tabulaciones (`WHITESPACE`) se ignoran durante el análisis.

---

### Autor

Analizador léxico creado como parte del proyecto educativo personalizado.
