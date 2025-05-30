import re

# Palabras reservadas de tu lenguaje
palabras_reservadas = {
    "start_main", "endmain", "var", "int", "string", "bool", "double", "true", "false",
    "if", "endif", "loop", "endloop", "show"
}

# Tokens y sus expresiones regulares
tokens = [
    ("NUMBER", r"\b\d+(\.\d+)?\b"),
    ("STRING", r'"[^"\n]*"'),
    ("EQ", r"=="),
    ("NE", r"!="),
    ("LE", r"<="),
    ("GE", r">="),
    ("EQUALS", r"="),
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
    ("ID", r"\b[a-zA-Z_][a-zA-Z0-9_]*\b"),
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
                    pass
                elif nombre == "ID" and lexema in palabras_reservadas:
                    print(f"✔ Token 'RESERVADA' reconocido: '{lexema}' (Línea {numero_linea})")
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
