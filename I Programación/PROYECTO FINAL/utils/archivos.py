"""
utils/archivos.py
Funciones para carga y guardado de catálogo y facturas en CSV/JSON.
"""
import csv
import json
import os
import datetime

from models.videojuego import crear_juego, VideoJuego
from utils.colors import ok, err, warn, info, titulo, CYAN, AZUL, AMARILLO, GRIS, RESET, VERDE, ROJO

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')

COLUMNAS_REQUERIDAS = {'id', 'title', 'genre', 'price', 'esrb', 'consola', 'stock'}
ESRB_VALIDOS        = ['E', 'E10+', 'T', 'M', 'AO', 'RP']

_ALIAS = {
    'nombre':    'title',
    'categoria': 'genre',
    'precio':    'price',
}


def _normalizar_fila(fila: dict) -> dict:
    fila = {_ALIAS.get(k, k): v for k, v in fila.items()}
    try:
        fila['price'] = float(fila['price'])
    except (ValueError, KeyError):
        fila['price'] = None
    try:
        fila['stock'] = int(fila['stock'])
    except (ValueError, KeyError):
        fila['stock'] = 0
    fila['esrb'] = str(fila.get('esrb', '')).strip().upper() or 'RP'
    return fila


def _validar_catalogo(catalogo: list, fuente: str) -> list:
    if not catalogo:
        raise ValueError(f"El archivo {fuente} está vacío.")
    faltantes = COLUMNAS_REQUERIDAS - set(catalogo[0].keys())
    if faltantes:
        raise ValueError(f"El archivo {fuente} no tiene las columnas: {faltantes}")
    return catalogo


def leer_csv() -> list:
    """Carga catálogo desde CSV, retorna lista de dicts normalizados."""
    ruta = os.path.join(DATA_DIR, 'catalogo.csv')
    print(info("Cargando catálogo desde CSV..."))
    with open(ruta, newline='', encoding='utf-8') as f:
        catalogo = [_normalizar_fila(dict(row)) for row in csv.DictReader(f)]
    catalogo = [f for f in catalogo if f.get('price') is not None]
    return _validar_catalogo(catalogo, 'catalogo.csv')


def leer_json() -> list:
    """Carga catálogo desde JSON, retorna lista de dicts normalizados."""
    ruta = os.path.join(DATA_DIR, 'catalogo.json')
    print(info("Cargando catálogo desde JSON..."))
    with open(ruta, 'r', encoding='utf-8') as f:
        datos = json.load(f)
    catalogo = [_normalizar_fila(dict(fila)) for fila in datos]
    catalogo = [f for f in catalogo if f.get('price') is not None]
    return _validar_catalogo(catalogo, 'catalogo.json')


def seleccionar_formato() -> list:
    """Pide al usuario elegir CSV o JSON y retorna el catálogo cargado."""
    from utils.excepciones import input
    print(f"  {AMARILLO}1.{RESET} CSV")
    print(f"  {AMARILLO}2.{RESET} JSON")
    formato = input(f"{AZUL}Seleccione el formato: {RESET}").strip()
    if formato == '1':
        return leer_csv()
    elif formato == '2':
        return leer_json()
    else:
        print(warn("Formato inválido, cargando CSV por defecto."))
        return leer_csv()


def guardar_catalogo(catalogo: list):
    """Guarda el catálogo en CSV o JSON según elección del usuario."""
    from utils.excepciones import input
    print(f"\n{titulo('¿En qué formato desea guardar?')}")
    print(f"  {AMARILLO}1.{RESET} CSV")
    print(f"  {AMARILLO}2.{RESET} JSON")
    opcion = input(f"{AZUL}Seleccione: {RESET}").strip()

    os.makedirs(DATA_DIR, exist_ok=True)

    if opcion == '1':
        ruta = os.path.join(DATA_DIR, 'catalogo.csv')
        fieldnames = ['id', 'title', 'genre', 'price', 'esrb', 'consola', 'stock']
        with open(ruta, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            # Serializar objetos VideoJuego si es necesario
            rows = [j.to_dict() if isinstance(j, VideoJuego) else j for j in catalogo]
            writer.writerows(rows)
        print(ok("Guardado en CSV"))

    elif opcion == '2':
        ruta = os.path.join(DATA_DIR, 'catalogo.json')
        rows = [j.to_dict() if isinstance(j, VideoJuego) else j for j in catalogo]
        with open(ruta, 'w', encoding='utf-8') as f:
            json.dump(rows, f, indent=4, ensure_ascii=False)
        print(ok("Guardado en JSON"))

    else:
        print(err("Opción inválida. No se guardó."))


def guardar_factura_archivo(items: dict, total_compra: float):
    """Guarda factura en CSV o JSON con nombre de archivo elegido por el usuario."""
    from utils.excepciones import input

    print(f"\n{titulo('─── Guardar Factura ───')}")

    while True:
        cliente = input(f"  {CYAN}Nombre del cliente:{RESET} ").strip()
        if cliente:
            break
        print(err("El nombre no puede estar vacío."))

    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    while True:
        nombre_archivo = input(f"  {CYAN}Nombre del archivo {GRIS}(sin extensión){RESET}: ").strip()
        if nombre_archivo:
            break
        print(err("El nombre no puede estar vacío."))

    print(f"  {AMARILLO}1.{RESET} CSV")
    print(f"  {AMARILLO}2.{RESET} JSON")
    fmt = input(f"  {AZUL}Formato: {RESET}").strip()

    os.makedirs(DATA_DIR, exist_ok=True)

    if fmt == '1':
        ruta = os.path.join(DATA_DIR, f"{nombre_archivo}.csv")
        with open(ruta, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(
                f,
                fieldnames=['cliente', 'fecha', 'titulo', 'esrb', 'cantidad', 'precio_unit', 'subtotal', 'total']
            )
            writer.writeheader()
            primera = True
            for datos in items.values():
                subtotal = datos['price'] * datos['cantidad']
                writer.writerow({
                    'cliente':     cliente if primera else '',
                    'fecha':       fecha   if primera else '',
                    'titulo':      datos['title'],
                    'esrb':        datos.get('esrb', 'RP'),
                    'cantidad':    datos['cantidad'],
                    'precio_unit': datos['price'],
                    'subtotal':    round(subtotal, 2),
                    'total':       round(total_compra, 2) if primera else '',
                })
                primera = False
        print(ok(f"Factura guardada en: {CYAN}{ruta}{RESET}"))

    elif fmt == '2':
        ruta = os.path.join(DATA_DIR, f"{nombre_archivo}.json")
        factura = {
            "cliente": cliente,
            "fecha":   fecha,
            "items": [
                {
                    "titulo":      d['title'],
                    "esrb":        d.get('esrb', 'RP'),
                    "cantidad":    d['cantidad'],
                    "precio_unit": d['price'],
                    "subtotal":    round(d['price'] * d['cantidad'], 2),
                }
                for d in items.values()
            ],
            "total": round(total_compra, 2),
        }
        with open(ruta, 'w', encoding='utf-8') as f:
            json.dump(factura, f, indent=4, ensure_ascii=False)
        print(ok(f"Factura guardada en: {CYAN}{ruta}{RESET}"))

    else:
        print(warn("Formato inválido. Factura no guardada."))
