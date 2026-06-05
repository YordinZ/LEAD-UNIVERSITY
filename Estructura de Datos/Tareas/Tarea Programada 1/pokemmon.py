import csv
import os

# Códigos ANSI
RESET    = '\033[0m'
NEGRITA  = '\033[1m'
DIM      = '\033[2m'

VERDE    = '\033[92m'
AMARILLO = '\033[93m'
ROJO     = '\033[91m'
CYAN     = '\033[96m'
MAGENTA  = '\033[95m'
AZUL     = '\033[94m'
GRIS     = '\033[90m'
BLANCO   = '\033[97m'

# Rutas 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
os.makedirs(DATA_DIR, exist_ok=True)

CSV_ORIGEN = os.path.join(DATA_DIR, 'pokemones.csv')

# Índices de columnas en el CSV
COL_NOMBRE  = 1   # Name
COL_ATAQUE  = 6   # Attack
COL_DEFENSA = 7   # Defense

# UTILIDADES
def clear_console():
    """Limpia la consola (compatible con Windows y Unix)."""
    os.system('cls' if os.name == 'nt' else 'clear')


# ALGORITMOS DE ORDENAMIENTO
def merge_sort(arr, key_fn):
    """MergeSort in-place usando key_fn para extraer la clave de comparación."""
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L, key_fn)
        merge_sort(R, key_fn)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if key_fn(L[i]) <= key_fn(R[j]):
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def quick_sort(arr, key_fn):
    """QuickSort funcional que devuelve una nueva lista ordenada."""
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    menor  = [x for x in arr[1:] if key_fn(x) <  key_fn(pivot)]
    igual  = [x for x in arr[1:] if key_fn(x) == key_fn(pivot)]
    mayor  = [x for x in arr[1:] if key_fn(x) >  key_fn(pivot)]
    return quick_sort(menor, key_fn) + [pivot] + igual + quick_sort(mayor, key_fn)


# E/S  (CSV)
def leer_csv(ruta):
    """Lee el CSV y devuelve (encabezado, filas).  Omite filas vacías."""
    with open(ruta, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        filas  = [row for row in reader if row]
    encabezado = filas[0]
    datos      = filas[1:]
    return encabezado, datos


def guardar_csv(ruta, encabezado, datos):
    """Escribe encabezado + datos en un CSV."""
    with open(ruta, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(encabezado)
        writer.writerows(datos)


# KEY FUNCTIONS  (evitan crashes si la columna no es numérica)
def _safe_int(row, col):
    try:
        return int(row[col])
    except (ValueError, IndexError):
        return 0


def key_nombre(row):  return row[COL_NOMBRE].lower() if len(row) > COL_NOMBRE else ''
def key_ataque(row):  return _safe_int(row, COL_ATAQUE)
def key_defensa(row): return _safe_int(row, COL_DEFENSA)


# LÓGICA DE ORDENAMIENTO + GUARDADO
def ordenar_y_guardar(criterio_nombre, criterio_label, key_fn, tipo):
    """
    Lee el CSV, ordena según key_fn con el algoritmo elegido,
    guarda el resultado y muestra feedback en consola.
    """
    print(f"\n{GRIS}  Leyendo {CSV_ORIGEN}...{RESET}")

    try:
        encabezado, datos = leer_csv(CSV_ORIGEN)
    except FileNotFoundError:
        print(f"{ROJO}{NEGRITA}  ✗ No se encontró el archivo:{RESET} {CSV_ORIGEN}")
        return

    # ── Ordenar ───────────────────────────────────────────────────────────────
    if tipo == 'mergesort':
        merge_sort(datos, key_fn)
        ordenados = datos
    else:  # quicksort
        ordenados = quick_sort(datos, key_fn)

    # ── Guardar ───────────────────────────────────────────────────────────────
    nombre_archivo = f"pokemones_{criterio_label}_{tipo}.csv"
    ruta_salida    = os.path.join(DATA_DIR, nombre_archivo)
    guardar_csv(ruta_salida, encabezado, ordenados)

    # ── Feedback ──────────────────────────────────────────────────────────────
    print(f"\n{VERDE}{NEGRITA}  ✔ Ordenamiento exitoso{RESET}")
    print(f"  {DIM}Criterio : {RESET}{CYAN}{criterio_nombre}{RESET}")
    print(f"  {DIM}Algoritmo: {RESET}{MAGENTA}{tipo.capitalize()}{RESET}")
    print(f"  {DIM}Archivo  : {RESET}{AMARILLO}{ruta_salida}{RESET}")

    # Preview de las 5 primeras filas
    print(f"\n  {AZUL}{NEGRITA}Primeras 5 filas:{RESET}")
    for fila in ordenados[:5]:
        print(f"  {GRIS}│{RESET} {BLANCO}{fila[COL_NOMBRE]:<30}{RESET}"
              f"  {DIM}Atk:{RESET}{AMARILLO}{fila[COL_ATAQUE]:>4}{RESET}"
              f"  {DIM}Def:{RESET}{CYAN}{fila[COL_DEFENSA]:>4}{RESET}")


# MENÚS
def menu_algoritmo():
    """Pide al usuario que elija el algoritmo.  Devuelve 'mergesort' | 'quicksort' | None."""
    print(f"\n  {AZUL}── Algoritmo de ordenamiento ──{RESET}")
    print(f"  {NEGRITA}a.{RESET} MergeSort")
    print(f"  {NEGRITA}b.{RESET} QuickSort")
    op = input(f"\n  {AMARILLO}Elige (a/b): {RESET}").strip().lower()
    if op == 'a':
        clear_console()
        return 'mergesort'
    elif op == 'b':
        clear_console()
        return 'quicksort'
    else:
        print(f"\n  {ROJO}Opción no válida.{RESET}")
        return None


def menu_principal():
    """Muestra el menú principal y devuelve la opción elegida."""
    print(f"\n{AZUL}{'═' * 50}{RESET}")
    print(f"{AZUL}{NEGRITA}  🎮  POKÉMON SORTER{RESET}")
    print(f"{AZUL}{'═' * 50}{RESET}")
    print(f"  {NEGRITA}1.{RESET} Ordenar por {CYAN}nombre{RESET}")
    print(f"  {NEGRITA}2.{RESET} Ordenar por {AMARILLO}ataque{RESET}")
    print(f"  {NEGRITA}3.{RESET} Ordenar por {VERDE}defensa{RESET}")
    print(f"  {NEGRITA}4.{RESET} {ROJO}Salir{RESET}")
    print(f"{GRIS}{'─' * 50}{RESET}")
    return input(f"  {AMARILLO}Selecciona una opción (1-4): {RESET}").strip()


# MAIN
OPCIONES = {
    '1': ('Nombre',  'nombre',  key_nombre),
    '2': ('Ataque',  'ataque',  key_ataque),
    '3': ('Defensa', 'defensa', key_defensa),
}

def main():
    while True:
        op = menu_principal()

        if op == '4':
            print(f"\n{MAGENTA}  Hasta la próxima, entrenador. 👋{RESET}\n")
            break

        if op not in OPCIONES:
            print(f"\n{ROJO}  Opción no válida. Intenta de nuevo.{RESET}")
            continue

        criterio_nombre, criterio_label, key_fn = OPCIONES[op]
        algo = menu_algoritmo()

        if algo is None:
            continue

        ordenar_y_guardar(criterio_nombre, criterio_label, key_fn, algo)

        input(f"\n{GRIS}  Presiona Enter para continuar...{RESET}")


if __name__ == '__main__':
    main()