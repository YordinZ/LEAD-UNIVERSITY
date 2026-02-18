from .limpiar_pantalla import clear
from .barra_carga import loading_bar
from .sopa_engine import generar_sopa
from .marcar_palabra import marcar_palabra

VERDE = "\033[32m"
ROJO = "\033[31m"
RESET = "\033[0m"

# Función para manejar la entrada del usuario con validación, incluyendo la opción de salir en cualquier momento!
def entrada(texto=""):
    dato = input(texto).strip()
    if dato.lower() in ("exit", "salir"):
        print("\n> Saliendo del programa...")
        raise SystemExit
    return dato

# Función para pausar el programa
def pausar():
    input("\nPresione Enter para continuar...")

# Función para ingresar palabras con validación
def ingresar_palabra():
    palabras = []

    while len(palabras) < 15:
        palabra = entrada("\nIngrese una palabra: ").lower()

        if palabra == "":
            print("Error: No puede estar vacía.")
            continue
        elif palabra in palabras:
            print("Error: La palabra ya ha sido ingresada.")
            continue
        elif palabra.isdigit():
            print("Error: No se permiten números.")
            continue

        palabras.append(palabra)

        while True:
            continuar = entrada("¿Desea ingresar otra palabra? (si/no): ").lower()

            if continuar in ("s", "si", "sí"):
                break
            elif continuar in ("n", "no"):
                return palabras
            else:
                print("\nError: Solo se permite 'si' o 'no'.")

    print("Máximo de 15 palabras alcanzado.")
    return palabras

# Función para imprimir la sopa de letras y las listas de palabras
def imprimir_sopa_y_lista(grid, marcas, palabras_usuario, palabras_random):
    print("...SOPA DE LETRAS...\n")
    for i, fila in enumerate(grid):
        out = []
        for j, ch in enumerate(fila):
            if marcas[i][j] == 1:
                out.append(f"{VERDE}{ch}{RESET}")
            elif marcas[i][j] == 2:
                out.append(f"{ROJO}{ch}{RESET}")
            else:
                out.append(ch)
        print(" ".join(out))

    print("\nPALABRAS:\n")
    for p in palabras_usuario:
        print(f"{VERDE}{p}{RESET}")
    for p in palabras_random:
        print(f"{ROJO}{p}{RESET}")

# MAIN
def main():
    pausar()
    clear()
    print("...SOPAS DE LETRAS - INGRESO DE PALABRAS...\n")
    print("Reglas: - Máximo 15 palabras.\n"
          "       - No pueden estar vacías.\n"
          "       - No se permiten números.\n"
          "       - No se permiten palabras repetidas.\n"
          "       - Nota: Puede escribir 'salir' o 'exit' en cualquier momento para terminar el programa.")

    palabras = ingresar_palabra()
    clear()
    print("Palabras ingresadas:", palabras)
    pausar()
    loading_bar()
    clear()

    # GENERAR SOPA 10x10
    grid, user_words, rnd_words = generar_sopa(palabras, n=10, cantidad_random=6)

    # Crear matriz de marcas (0 normal, 1 verde, 2 rojo)
    marcas = [[0] * len(grid) for _ in range(len(grid))]

    imprimir_sopa_y_lista(grid, marcas, user_words, rnd_words)

    # BÚSQUEDA
    while True:
        buscar = entrada("\n¿Qué palabra quieres buscar?: ").strip().upper()

        if buscar.lower() in ("salir", "exit"):
            break

        encontrada = marcar_palabra(grid, marcas, buscar, user_words, rnd_words)

        if encontrada:
            print("✅ Palabra encontrada y marcada en la sopa.")
        else:
            print("❌ Palabra no encontrada o no pertenece a la lista.")

        pausar()
        clear()
        imprimir_sopa_y_lista(grid, marcas, user_words, rnd_words)


if __name__ == "__main__":
    main()

#EJECUTAR: TAREAS/Tarea_3/python -m Tarea_3.Sopa_letras