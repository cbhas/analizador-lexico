import re

tokens = {
    "PRINT": r"print",
    "ID": r"[a-zA-Z_][a-zA-Z0-9_]*",
    "NUMBER": r"\d+",
    "EQUALS": r"=",
    "STRING": r"\".*?\"",
    "PLUS": r"\+",
    "SEMICOLON": r";"
}

def analizar_linea(linea, numero_linea):
    posicion = 0
    while posicion < len(linea):
        if linea[posicion].isspace():
            posicion += 1
            continue
        
        match_encontrado = False
        for nombre, patron in tokens.items():
            regex = re.compile(patron)
            match = regex.match(linea, posicion)
            if match:
                print(f"✔ Token '{nombre}' reconocido: '{match.group()}' (Línea {numero_linea})")
                posicion = match.end()
                match_encontrado = True
                break
        if not match_encontrado:
            print(f"❌ Error léxico en línea {numero_linea}: '{linea[posicion]}'")
            posicion += 1

def analizar_archivo(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        for i, linea in enumerate(archivo, 1):
            analizar_linea(linea.strip(), i)

if __name__ == "__main__":
    analizar_archivo("fuente.txt")
