def generar_tablero_desde_archivo(ruta_archivo): #GENERAR EL CUADRADO
    # Leer cuántas casillas quiere el usuario
    with open(ruta_archivo, 'r') as archivo:
        primera_linea = archivo.readline().strip() # Solo la primera línea
        total_casillas = int(primera_linea) # Convertimos a número

    # Generar la parte superior del tablero
    linea_superior = ""
    linea_media = ""
    linea_inferior = ""

    for i in range(1, total_casillas + 1):
        casilla = f"{i:02d}"  # Formato 01, 02, 03...
        linea_superior += "╭────╮"
        linea_media += f"│ {casilla} │"
        linea_inferior += "╰────╯"

    # Imprimir tablero
    print(linea_superior)
    print(linea_media)
    print(linea_inferior)


# EJECUCIÓN
generar_tablero_desde_archivo("tablero.txt")
