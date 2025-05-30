import re

# Tokens y sus expresiones regulares
tokens = [
    ("ID", r"\b[a-zA-Z_][a-zA-Z0-9_]*\b"),
    ("NUMBER", r"\b\d+(\.\d+)?\b"),
    ("STRING", r'"[^"\n]*"'),
    ("EQUALS", r"="),
    ("EQ", r"=="),
    ("NE", r"!="),
    ("LE", r"<="),
    ("GE", r">="),
    ("LT", r"<"),
    ("GT", r">"),
    ("NOT", r"!"),
    ("PLUS", r"\+"),
    ("MINUS", r"-"),
    ("TIMES", r"\*"),
    ("DIVIDE", r"/"),
    ("LPAREN", r"\("),
    ("RPAREN", r"\)"),
    ("WHITESPACE", r"[ \t]+"),
]

token_regex = [(nombre, re.compile(patron)) for nombre, patron in tokens]

def analizar_linea(linea, numero_linea):
    i = 0
    while i < len(linea):
        match = None
        for nombre, patron in token_regex:
            match = patron.match(linea, i)
            if match:
                lexema = match.group()
                if nombre == "WHITESPACE":
                    pass  # Ignorar espacios
                else:
                    print(f"✔ Token '{nombre}' reconocido: '{lexema}' (Línea {numero_linea})")
                i = match.end()
                break
        if not match:
            print(f"❌ Error léxico en línea {numero_linea}: '{linea[i]}'")
            i += 1

with open("fuente.txt", "r", encoding="utf-8") as archivo:
    for num_linea, linea in enumerate(archivo, start=1):
        analizar_linea(linea.strip(), num_linea)

# cbhas
