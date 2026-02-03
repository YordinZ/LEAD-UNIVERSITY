import random 

# VARIABLES GLOBALES
registro_jugadas = [] # Lista de diccionarios con el historial , acumula datos como diccionario (ronda, jugador, dado, antes, después, tipo, descripción).
jugadores = [] # Lista de nombres de jugadores actual
total_casillas = 0 # Meta / Última casilla
reglas = {} # Dict {pos: {"accion": str, "valor": int}} (ej: {5: {"accion":"AVANZA","valor":2}}
tablero = [] # Lista auxiliar que va de 0 a total_casillas (no se usa intensamente, pero se utiliza para representar el rango de casillas).

# ENTRADA SEGURA
def entrada(texto=""):
    '''
    Leer entrada del usuario de forma segura.
    Si se escribe 'exit' o 'salir' sale inmediatamente del programa.
    Devuelve la cadena en minúsculas y sin espacios al inicio/final.
    '''
    dato = input(texto).strip()
    if dato.lower() in ("exit", "salir"):
        print("\n> Saliendo del programa...")
        exit()
    return dato 

# FUNCIONES DE CARGA Y VALIDACIÓN DEL ARCHIVO
def validar_accion(accion):
    '''Verifica si la accion es válida.'''
    return accion in ("AVANZA", "RETROCEDE", "PIERDE_TURNO")

def cargar_tablero(ruta_archivo):
    """ Función responsable de leer el archivo de configuración con el formato esperado:
            Carga el archivo de configuración del tablero.
            Formato esperado:
            40
            posicion;accion;valor
            5;AVANZA;2
            ...
    """

    global total_casillas, reglas, tablero # usamos global, para modificas la variable global original

    # INTENTAR ABRIR EL ARCHIVO
    '''
    OPEN (RUTA. MODO) dos parametros
        1. Ruta del archivo= ruta/nombre_archivo.txt
        2. Modo de apertura:
        'r'= leer, valor por defecto (Si el archivo no existe da error)
        'a'= agregar, si el archivo no exite lo crea, agregar los datos
        'w'= escribir, si el archivo existe lo sobre escribe, sino existe lo crea
        'x'= crear, crea un archivo nuevo
    '''
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            lineas = [l.strip() for l in archivo.readlines() if l.strip()] # Quita líneas vacías y espacios
    except FileNotFoundError:
        print(f"ERROR: El archivo '{ruta_archivo}' no existe.")
        return False
    except Exception as e:
        print("ERROR al leer el archivo:", e)
        return False

    if not lineas:
        print("ERROR: El archivo está vacío.")
        return False

    # LEER CANTIDAD DE CASILLAS
    try:
        total_casillas = int(lineas[0]) # Convierte la primera línea a int y lo asigna a total_casillas. Valida que sea > 0
        if total_casillas <= 0:
            print("ERROR: El número de casillas debe ser entero positivo.")
            return False
    except ValueError:
        print("ERROR: La primera línea debe ser un número entero (total de casillas).")
        return False

    reglas_temp = {} # se usa para evitar que el juego quede en un estado dañado si el archivo del tablero tiene errores.
    ''' para construir reglas_temp:
            -Ignora encabezado si empieza con "posicion".
            -Requiere ; como separador.
            -Divide en 3 partes: pos, accion, valor.
            -Valida que pos y valor sean enteros.
            -Convierte accion a mayúsculas y valida con validar_accion (solo AVANZA, RETROCEDE, PIERDE_TURNO aceptadas).
            -Valida rango: 0 <= pos <= total_casillas.
            -Evita duplicados (si aparece la misma pos dos veces, ignora la segunda).
    '''
    lineas_reglas = lineas[1:]

    # PROCESAR REGLAS
    for linea in lineas_reglas:
        if not linea:
            continue

        # Saltar encabezado pensado como "posicion;accion;valor"
        if linea.lower().startswith("posicion"): # startswith, verificar si un texto empieza con una palabra o una secuencia específica.
            continue

        if ";" not in linea:
            print(f"ADVERTENCIA: Línea ignorada (falta ';'): {linea}")
            continue

        partes = [p.strip() for p in linea.split(";")]
        if len(partes) != 3:
            print(f"ADVERTENCIA: Formato inválido (3 campos requeridos): {linea}")
            continue

        # Validar enteros
        try:
            pos = int(partes[0])
            valor = int(partes[2])
        except ValueError:
            print(f"ADVERTENCIA: posición o valor no son enteros en: {linea}")
            continue

        accion = partes[1].upper()

        if not validar_accion(accion):
            print(f"ADVERTENCIA: acción inválida '{accion}' en: {linea}")
            continue

        # Validación rango
        if pos < 0 or pos > total_casillas:
            print(f"ADVERTENCIA: posición fuera de rango (0..{total_casillas}): {pos}")
            continue

        # Duplicados
        if pos in reglas_temp:
            print(f"ADVERTENCIA: casilla duplicada, se ignora: {pos}")
            continue

        # Guardar regla
        reglas_temp[pos] = {"accion": accion, "valor": valor}

    # ASIGNAR RESULTADOS
    reglas = reglas_temp
    tablero = list(range(0, total_casillas + 1))

    # CONFIRMACIÓN
    print(f"> Archivo cargado correctamente | Total de casillas: {total_casillas}")

    if reglas:
        print("\nReglas especiales encontradas:")
        print("=========================================")
        for pos, datos in sorted(reglas.items()): # Reglas especiales
            print(f"  Casilla {pos}: {datos['accion']} {datos['valor']}")
        print("=========================================")
    else:
        print("No hay casillas especiales definidas.")

    return True

# FUNCIONES DEL TABLERO Y VISUALIZACIÓN
def imprimir_tablero(posiciones, ultima_jugada=None):
    '''
    Muestra el estado claro del tablero:
    - Posición actual de cada jugador.
    - Si pasas ultima_jugada, la imprime también.)
    '''
    print("\n.......... TABLERO ..........")
    print(f"Meta (casilla final): {total_casillas}")

    for jugador in posiciones:
        '''
        {jugador:<12}, jugador → variable a imprimir
            : = comienza la configuración de formato
            < = alinear a la izquierda
            12 = ocupar 12 espacios de ancho
        '''
        print(f"Jugador: {jugador:<12} | Posición: {posiciones[jugador]}") # permite que la tabla se vea alineada aunque los nombres tengan longitud distinta.

    if ultima_jugada:
        print("\nÚltima jugada:")
        print(ultima_jugada)

    print(".............................\n")  

# FUNCIONES DE JUEGO
def lanzar_dado():
    '''Devuelve un entero aleatorio entre 1 y 6.'''
    return random.randint(1, 6)

def registrar_jugada(ronda, jugador, dado, pos_anterior, pos_nueva, tipo_casilla, descripcion):
    '''
    Guarda en registro_jugadas la jugada como diccionario:
    'ronda', 'jugador', 'dado', 'posicion_anterior', 'posicion_nueva',
    'tipo_de_casilla', 'descripcion'
    '''
    jugada = { #diccionario, parecido a una estructura JSON.
        'ronda': ronda,
        'jugador': jugador,
        'dado': dado,
        'posicion_anterior': pos_anterior,
        'posicion_nueva': pos_nueva,
        'tipo_de_casilla': tipo_casilla,
        'descripcion': descripcion
    }
    registro_jugadas.append(jugada) # Almacena las jugadas
    
def verificar_victoria(posicion):
    '''
    Devuelve True si la posicion es mayor o igual que la meta (total_casillas).
    '''
    return posicion >= total_casillas

# INICIO DE LA PARTIDA
def iniciar_partida():
    '''
    Inicia una partida:
    - Pide número de jugadores (2-4)
    - Pide nombre de cada jugador
    - Inicializa posiciones y estructura de perder turnos
    - Controla el flujo completo de rondas hasta que alguien gane
    '''
    global registro_jugadas, jugadores # usamos global, para modificas la variable global original
    
    # Número de jugadores (validado 2..4)
    while True:
        entrada_text = entrada("> Ingrese un número de los jugadores (2-4): ") 
        '''
        Utilizamos entrada() en vez de input(), por que permite agregar reglas como:
            - La forma en que recibes datos (ejemplo: limpiar espacios, permitir "salir", logs, validación, etc.)
            - Clean code
            - Permite personalizar cómo se lee la entrada
        '''
        try:
            x = int(entrada_text)
            if 2 <= x <= 4: # simplificacion sin usar AND, comparaciones encadenadas
                break
            else:
                print("Debe ingresar un número entero entre 2 y 4.\n")
        except ValueError:
            print("Entrada inválida | Escriba un número entre 2 y 4, o 'salir' para terminar.\n")
    
    # Nombres de jugadores
    jugadores = []
    for i in range(x):
        while True:
            nombre = entrada(f"Nombre del jugador {i+1}: ").strip()
            if nombre == "":
                print("> El nombre no puede estar vacío.\n")
            elif nombre in jugadores:
                print("> Ya existe un jugador con ese nombre. (Elija otro)\n")
            else:
                jugadores.append(nombre) # Almacena
                break
    
    # Inicializaciones
    posiciones= {jugador: 0 for jugador in jugadores} # Todos comienzan en 0 según enunciado
    perder_turnos = {jugador: 0 for jugador in jugadores} # cuántos turnos le faltan por perder
    registro_jugadas = []
    ronda = 1
    ganador = None

    print("\nComienza la partida 🎲. Suerte a todos❗\n")

    # Bucle principal por rondas
    while not ganador:
        print(f"----- Ronda {ronda} -----")
        for jugador in jugadores:
            print(f"\nTurno de {jugador} (Posición actual: {posiciones[jugador]})")

            # Validación de perder turno
            if perder_turnos[jugador] > 0:
                perder_turnos[jugador] -= 1
                descripcion = f"El jugador {jugador} pierde este turno por penalización. Turnos restantes: {perder_turnos[jugador]}"
                print(descripcion)
                # Guardar en registro (sin lanzar dado)
                registrar_jugada(ronda, jugador, 0, posiciones[jugador], posiciones[jugador], "PIERDE_TURNO", descripcion)
                # Mostrar estado después
                imprimir_tablero(posiciones)
                continue

            # Lanzar dado (presionar ENTER)
            entrada("Presione ENTER para lanzar el dado...")
            dado = lanzar_dado()
            print(f"El dado cayó en: {dado}")

            pos_anterior = posiciones[jugador]
            pos_tentativa = pos_anterior + dado

            # Verificar victoria inmediata (antes de aplicar casilla)
            if verificar_victoria(pos_tentativa):
                # Actualizamos la posición, registramos y declaramos ganador
                posiciones[jugador] = pos_tentativa
                descripcion = f"{jugador} llegó a {pos_tentativa}, supero o igualo a la meta ({total_casillas})."
                registrar_jugada(ronda, jugador, dado, pos_anterior, posiciones[jugador], "META", descripcion)
                imprimir_tablero(posiciones, ultima_jugada=descripcion)
                ganador = jugador
                print(f"¡FELICIDADES, {jugador} GANASTE LA CARRERA DE DATOS! 🎉")
                break  # sale del for
            # Sino gana de inmediato, aplicar reglas si la casilla tentativa tiene efecto
            tipo_casilla = "Normal"
            descripcion = "Movimiento normal"
            pos_nueva = pos_tentativa

            # Si la casilla tentativa tiene una regla, aplicarla
            if pos_tentativa in reglas:
                regla = reglas[pos_tentativa]
                accion = regla["accion"]
                valor = regla["valor"]

                if accion == "AVANZA":
                    pos_nueva = pos_tentativa + valor
                    descripcion = f"Casilla especial: AVANZA {valor} → nueva posición: {pos_nueva}"
                    tipo_casilla = f"AVANZA +{valor}"

                elif accion == "RETROCEDE":
                    pos_nueva = pos_tentativa - valor
                    if pos_nueva < 0:
                        pos_nueva = 0
                    descripcion = f"Casilla especial: RETROCEDE {valor} → nueva posición: {pos_nueva}"
                    tipo_casilla = f"RETROCEDE -{valor}"

                elif accion == "PIERDE_TURNO":
                    # marcar al jugador para perder 'valor' turnos
                    perder_turnos[jugador] = valor
                    pos_nueva = pos_tentativa  # no se mueve en PIERDE_TURNO (según interpretación)
                    descripcion = f"Casilla especial: PIERDE_TURNO {valor} → pierde {valor} turno(s)"
                    tipo_casilla = "PIERDE_TURNO"

                else:
                    descripcion = "Acción especial desconocida"
                    tipo_casilla = "DESCONOCIDA"

            # Asegurarse que no supere la casilla meta
            if pos_nueva > total_casillas:
                pos_nueva = total_casillas

            # Actualizar posición
            posiciones[jugador] = pos_nueva

            # Registrar jugada
            registrar_jugada(ronda, jugador, dado, pos_anterior, pos_nueva, tipo_casilla, descripcion)

            # Mostrar mensajes
            print(descripcion)
            print(f"Posición anterior: {pos_anterior} → Posición nueva: {pos_nueva}")

            # Imprimir tablero con la última jugada
            ultima = f"Ronda {ronda} - {jugador}: dado {dado} | {descripcion}"
            imprimir_tablero(posiciones, ultima_jugada=ultima)

            # Verificar victoria luego de aplicar efectos
            if verificar_victoria(posiciones[jugador]):
                ganador = jugador
                print(f"\n¡FELICIDADES, {jugador} GANASTE LA CARRERA DE DATOS! 🎉")
                break

        # fin for jugadores
        if not ganador:
            ronda += 1

    # Al finalizar la partida, imprimir registro completo
    print("¡Partida finalizada!")
    imprimir_registro_detallado()


# FUNCIONES DE IMPRESIÓN Y REGISTRO
def imprimir_registro_detallado():
    """
    Imprime el registro de jugadas
    """
    print("\n========== REGISTRO DE JUGADAS ==========\n")
    for r in registro_jugadas:
        print(f"Ronda {r['ronda']}: {r['jugador']} | Dado: {r['dado']} | Antes: {r['posicion_anterior']} | Después: {r['posicion_nueva']} | Tipo: {r['tipo_de_casilla']} | {r['descripcion']}")
    print("\n=========================================\n")
    volver_jugar()

# FUNCION VOLVER A JUGAR
def volver_jugar():
    print(".......... ¿Desea jugar de nuevo? ..........")

    while True:
        op= entrada("Introduzca una opción (S/N): ").strip().lower() #Convertir a minúsculas
        if op in ['s', 'si', 'sí']:
            main()
            break
        
        elif op in ['n', 'no']:
            print("\n> ¡Gracias por jugar! 🔚")
            exit()
        else:
            print("> Opción inválida\n")

# MENÚ PRINCIPAL
def main():
    """
    Menú principal con validación
    1 - Jugar
    2 - Salir
    """
    while True:
        print("\n.......... CARRERA DE DATOS 🏇 ..........")
        print("1. Jugar")
        print("2. Salir")
        print("> Nota: Para salir del juego en cualquier momento, escribe 'exit' o 'salir'.\n")
        opcion = entrada("Introduzca una opción (1/2): ").strip()
        if opcion == "1":
            # Cargar tablero (busca automáticamente tablero.txt en la misma carpeta del script)
            # Obtener la ruta del directorio donde está este script
            ruta_script = __file__.replace('\\', '/').rsplit('/', 1)[0] if '/' in __file__ or '\\' in __file__ else '.'
            archivo = ruta_script + "/tablero.txt"
            print(f"\nBuscando archivo 'tablero.txt' en la carpeta del script...")
            ok = cargar_tablero(archivo)
            if not ok:
                print("> Error en archivo | Regresando al menú principal.")
                continue
            # Generar (imprimir) tablero inicial y empezar partida
            imprimir_tablero({})  # mostrará meta y nada más (se usa dentro de iniciar_partida)
            """
            llamada la función imprimir_tablero, donde está pasando como argumento un diccionario vacío ({}).
                - La función recibirá ese diccionario como su parámetro
            """
            iniciar_partida()
        elif opcion == "2":
            print("\n> ¡Gracias por jugar! 🔚")
            exit()
        else:
            print("> Opción inválida. Ingrese '1' o '2'.")


# PUNTO DE ENTRADA 
if __name__ == "__main__": # Evitar que se ejecute el código principal cuando el archivo se importa como módulo.
    main()