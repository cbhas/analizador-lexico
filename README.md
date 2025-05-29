# Analizador Léxico Básico en Python

## Descripción
Este proyecto contiene un analizador léxico simple que lee un archivo fuente y detecta tokens como palabras reservadas, identificadores, números, cadenas, operadores y símbolos de puntuación. Muestra mensajes de éxito o error para cada token reconocido.

## Estructura del lenguaje

- Las instrucciones terminan con `;`.
- Soporta impresión con `print "texto";`.
- Soporta asignaciones simples `id = valor;`.
- Soporta suma de números `id = número + número;`.

## Tokens reconocidos

| Token     | Ejemplo          |
|-----------|------------------|
| PRINT     | print            |
| ID        | variable1        |
| NUMBER    | 123              |
| STRING    | "texto"          |
| EQUALS    | =                |
| PLUS      | +                |
| SEMICOLON | ;                |

## Cómo usar

1. Coloca tu código fuente en el archivo `fuente.txt`.
2. Ejecuta el analizador:
   ```bash
   python3 src/analizador.py
3. Verás mensajes indicando qué tokens fueron reconocidos o si hubo errores léxicos.
