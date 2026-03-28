"""
╔══════════════════════════════════════╗
║         AGENDA DE CONTACTOS          ║
╚══════════════════════════════════════╝
"""

import pandas as pd
import json
import os

# ── Rutas ─────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))   # fix: os.path (no os.pat)
DATA_DIR = os.path.join(BASE_DIR, 'data')
os.makedirs(DATA_DIR, exist_ok=True)                    # crea /data si no existe

RUTA_CSV  = os.path.join(DATA_DIR, 'personas.csv')
RUTA_JSON = os.path.join(DATA_DIR, 'personas.json')

CAMPOS = ['nombre', 'telefono', 'email', 'edad', 'residencia']

# ── Colores ANSI ──────────────────────────────────────────────
VERDE    = '\033[92m'
AMARILLO = '\033[93m'
ROJO     = '\033[91m'
CYAN     = '\033[96m'
BLANCO   = '\033[97m'
GRIS     = '\033[90m'
RESET    = '\033[0m'
NEGRITA  = '\033[1m'


# ═════════════════════════════════════════════════════════════
#  HELPERS UI
# ═════════════════════════════════════════════════════════════

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def linea(char='─', n=52, color=GRIS):
    print(f"{color}{char * n}{RESET}")


def pausar():
    input(f"\n{GRIS}  Presiona Enter para continuar...{RESET}")


def encabezado(subtitulo=''):
    clear()
    linea('═', 52, CYAN)
    print(f"{CYAN}{NEGRITA}{'AGENDA DE CONTACTOS':^52}{RESET}")
    if subtitulo:
        print(f"{GRIS}{subtitulo:^52}{RESET}")
    linea('═', 52, CYAN)


def input_campo(etiqueta, requerido=True):
    while True:
        valor = input(f"  {etiqueta}: ").strip()
        if valor or not requerido:
            return valor
        print(f"  {ROJO}Este campo es obligatorio.{RESET}")


# ═════════════════════════════════════════════════════════════
#  MOSTRAR UN CONTACTO
# ═════════════════════════════════════════════════════════════

def mostrar_contacto(c, idx=None):
    prefijo = f"{GRIS}[{idx}]{RESET} " if idx is not None else "  "
    get = lambda k: (c.get(k, '—') if isinstance(c, dict) else c[k])
    print(f"{prefijo}{NEGRITA}{BLANCO}{get('nombre')}{RESET}  "
          f"{CYAN}☎ {get('telefono')}{RESET}  "
          f"{AMARILLO}Edad: {get('edad')}{RESET}  "
          f"{GRIS}{get('email')} | {get('residencia')}{RESET}")


# ═════════════════════════════════════════════════════════════
#  LEER ARCHIVOS
# ═════════════════════════════════════════════════════════════

def leer_csv():
    if not os.path.exists(RUTA_CSV):
        return pd.DataFrame(columns=CAMPOS)
    return pd.read_csv(RUTA_CSV, dtype={'telefono': str})


def leer_json():
    if not os.path.exists(RUTA_JSON):
        return pd.DataFrame(columns=CAMPOS)
    with open(RUTA_JSON, 'r', encoding='utf-8') as f:
        datos = json.load(f)
    return pd.DataFrame(datos if isinstance(datos, list) else datos.get('contactos', []))


# ═════════════════════════════════════════════════════════════
#  GUARDAR ARCHIVOS
# ═════════════════════════════════════════════════════════════

def guardar_csv(df):
    df.to_csv(RUTA_CSV, index=False, encoding='utf-8')


def guardar_json(df):
    with open(RUTA_JSON, 'w', encoding='utf-8') as f:
        json.dump(df.to_dict(orient='records'), f, ensure_ascii=False, indent=2)


# ═════════════════════════════════════════════════════════════
#  OPCIONES DEL MENÚ
# ═════════════════════════════════════════════════════════════

def opcion_cargar():
    encabezado('Cargar Agenda')
    print(f"\n  {AMARILLO}1.{RESET} Desde CSV   ({GRIS}{RUTA_CSV}{RESET})")
    print(f"  {AMARILLO}2.{RESET} Desde JSON  ({GRIS}{RUTA_JSON}{RESET})")
    print(f"  {AMARILLO}0.{RESET} Cancelar")
    linea()

    op = input("  Elige formato: ").strip()
    if op == '0':
        return

    if op == '1':
        df = leer_csv(); fuente = 'CSV'
    elif op == '2':
        df = leer_json(); fuente = 'JSON'
    else:
        print(f"\n  {ROJO}Opción inválida.{RESET}"); pausar(); return

    print()
    if df.empty:
        print(f"  {AMARILLO}El archivo {fuente} no existe o está vacío. "
              f"Se creará al agregar el primer contacto.{RESET}")
    else:
        print(f"  {VERDE}✔ {len(df)} contacto(s) cargado(s) desde {fuente}:{RESET}\n")
        linea()
        for i, row in df.iterrows():
            mostrar_contacto(row, i + 1)
        linea()
        try:
            prom = pd.to_numeric(df['edad'], errors='coerce').mean()
            print(f"  {GRIS}Promedio de edad: {CYAN}{prom:.1f} años{RESET}")
        except Exception:
            pass
    pausar()


def opcion_agregar():
    encabezado(f"Agregar Contacto{RESET}  |  Escribe {AMARILLO}'Cancelar'{RESET} para salir")
    print("\n")

    nombre     = input_campo("Nombre")
    if nombre.lower() == 'cancelar': return

    telefono   = input_campo("Teléfono")
    if telefono.lower() == 'cancelar': return

    email      = input_campo("Email (opcional)", requerido=False)
    if email.lower() == 'cancelar': return

    edad_str   = input_campo("Edad")
    if edad_str.lower() == 'cancelar': return

    residencia = input_campo("Residencia (opcional)", requerido=False)
    if residencia.lower() == 'cancelar': return

    if not edad_str.isdigit():
        print(f"\n  {ROJO}La edad debe ser un número entero.{RESET}")
        pausar(); return

    nuevo = {
        'nombre': nombre, 'telefono': telefono,
        'email': email, 'edad': int(edad_str), 'residencia': residencia,
    }

    print(f"\n  ¿Dónde guardar?")
    print(f"  {AMARILLO}1.{RESET} CSV")
    print(f"  {AMARILLO}2.{RESET} JSON")
    print(f"  {AMARILLO}3.{RESET} Ambos")
    linea()
    op = input("  Elige: ").strip()

    def guardar_en_csv():
        df = leer_csv()
        df = pd.concat([df, pd.DataFrame([nuevo])], ignore_index=True)
        guardar_csv(df)
        print(f"  {VERDE}✔ Guardado en CSV ({len(df)} contacto(s) total).{RESET}")

    def guardar_en_json():
        df = leer_json()
        df = pd.concat([df, pd.DataFrame([nuevo])], ignore_index=True)
        guardar_json(df)
        print(f"  {VERDE}✔ Guardado en JSON ({len(df)} contacto(s) total).{RESET}")

    print()
    try:
        if op == '1':   guardar_en_csv()
        elif op == '2': guardar_en_json()
        elif op == '3': guardar_en_csv(); guardar_en_json()
        else: print(f"  {ROJO}Opción inválida, contacto no guardado.{RESET}")
    except Exception as e:
        print(f"  {ROJO}Error al guardar: {e}{RESET}")
    pausar()


def opcion_eliminar_archivo():
    encabezado('Eliminar Archivo')
    print(f"\n  {ROJO}⚠  Esta acción es irreversible.{RESET}\n")
    print(f"  {AMARILLO}1.{RESET} Eliminar CSV   ({GRIS}{RUTA_CSV}{RESET})")
    print(f"  {AMARILLO}2.{RESET} Eliminar JSON  ({GRIS}{RUTA_JSON}{RESET})")
    print(f"  {AMARILLO}3.{RESET} Eliminar ambos")
    print(f"  {AMARILLO}0.{RESET} Cancelar")
    linea()

    op = input("  Elige: ").strip()
    if op == '0': return

    def borrar(ruta):
        if os.path.exists(ruta):
            os.remove(ruta)
            print(f"  {VERDE}✔ Eliminado: {os.path.basename(ruta)}{RESET}")
        else:
            print(f"  {AMARILLO}No existe: {os.path.basename(ruta)}{RESET}")

    print()
    confirmacion = input(f"  {ROJO}¿Confirmas la eliminación? (s/n): {RESET}").strip().lower()
    if confirmacion != 's':
        print(f"  {GRIS}Cancelado.{RESET}"); pausar(); return

    print()
    if op == '1':   borrar(RUTA_CSV)
    elif op == '2': borrar(RUTA_JSON)
    elif op == '3': borrar(RUTA_CSV); borrar(RUTA_JSON)
    else: print(f"  {ROJO}Opción inválida.{RESET}")
    pausar()


def opcion_buscar():
    encabezado('Buscar Contacto')
    print(f"\n  {AMARILLO}1.{RESET} Por nombre")
    print(f"  {AMARILLO}2.{RESET} Por teléfono")
    linea()

    op = input("  Elige: ").strip()
    campo = {'1': 'nombre', '2': 'telefono'}.get(op)
    if not campo:
        print(f"  {ROJO}Opción inválida.{RESET}"); pausar(); return

    termino = input_campo("Término de búsqueda (parcial)").lower()

    df = pd.concat([leer_csv(), leer_json()]).drop_duplicates().reset_index(drop=True)

    if df.empty or campo not in df.columns:
        print(f"\n  {AMARILLO}No hay contactos guardados.{RESET}"); pausar(); return

    mask = df[campo].astype(str).str.lower().str.contains(termino, na=False)
    resultados = df[mask]

    print(); linea()
    if resultados.empty:
        print(f"  {AMARILLO}Sin resultados para '{termino}'.{RESET}")
    else:
        print(f"  {VERDE}{len(resultados)} resultado(s):{RESET}\n")
        for i, row in resultados.iterrows():
            mostrar_contacto(row, i + 1)
    linea(); pausar()


def opcion_mostrar_todos():
    encabezado('Todos los Contactos')
    df = pd.concat([leer_csv(), leer_json()]).drop_duplicates().reset_index(drop=True)

    print()
    if df.empty:
        print(f"  {AMARILLO}No hay contactos guardados aún.{RESET}")
    else:
        linea()
        for i, row in df.iterrows():
            mostrar_contacto(row, i + 1)
        linea()
        try:
            prom = pd.to_numeric(df['edad'], errors='coerce').mean()
            print(f"  {GRIS}Total: {len(df)} | Promedio de edad: {CYAN}{prom:.1f} años{RESET}")
        except Exception:
            print(f"  {GRIS}Total: {len(df)} contacto(s){RESET}")
    pausar()


# ═════════════════════════════════════════════════════════════
#  MENÚ PRINCIPAL
# ═════════════════════════════════════════════════════════════

OPCIONES = {
    '1': ('Cargar y ver agenda',          opcion_cargar),
    '2': ('Agregar contacto',             opcion_agregar),
    '3': ('Buscar contacto',              opcion_buscar),
    '4': ('Mostrar todos los contactos',  opcion_mostrar_todos),
    '5': ('Eliminar archivo',             opcion_eliminar_archivo),
    '6': ('Salir',                        None),
}


def menu():
    while True:
        encabezado()
        print()
        for key, (label, _) in OPCIONES.items():
            if key == '6':
                print(f"  {AMARILLO}6.{RESET}  {ROJO}{label}{RESET}")
            else:
                print(f"  {AMARILLO}{key}.{RESET}  {BLANCO}{label}{RESET}")
        linea()

        eleccion = input(f"  {CYAN}→ Elige una opción: {RESET}").strip()

        if eleccion == '6':
            clear()
            print(f"\n{CYAN}{'Hasta luego 👋':^52}{RESET}\n")
            break
        elif eleccion in OPCIONES:
            OPCIONES[eleccion][1]()
        else:
            print(f"\n  {ROJO}Opción '{eleccion}' no válida.{RESET}")
            pausar()


if __name__ == '__main__':
    menu()
