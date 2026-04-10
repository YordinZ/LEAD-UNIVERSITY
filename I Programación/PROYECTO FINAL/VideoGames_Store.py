import csv # Para manejo de archivos CSV
import json # Para manejo de archivos CSV y JSON
import os # Para manejo de archivos y rutas
import re # Para eliminar códigos ANSI al calcular longitudes visibles

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')


# ─────────────────────────────────────────────
#  Salida de emergencia global
# ─────────────────────────────────────────────

class SalidaForzada(Exception):
    pass


_input_original = input

def input(prompt: str = '') -> str:
    respuesta = _input_original(prompt)
    if respuesta.strip().lower() == 'salir':
        raise SalidaForzada()
    return respuesta


def salir():
    print(f"\n{VERDE}{NEGRITA}¡Hasta luego! 👋{RESET}\n")
    raise SystemExit(0)


# ─────────────────────────────────────────────
#  Colores ANSI
# ─────────────────────────────────────────────

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

def ok(msg: str)       -> str: return f"{VERDE}{NEGRITA}✅ {msg}{RESET}"
def err(msg: str)      -> str: return f"{ROJO}{NEGRITA}❌ {msg}{RESET}"
def warn(msg: str)     -> str: return f"{AMARILLO}⚠️  {msg}{RESET}"
def info(msg: str)     -> str: return f"{AZUL}ℹ️  {msg}{RESET}"
def titulo(msg: str)   -> str: return f"{CYAN}{NEGRITA}{msg}{RESET}"
def dim(msg: str)      -> str: return f"{GRIS}{msg}{RESET}"
def precio(v: float)   -> str: return f"{AMARILLO}${v:.2f}{RESET}"
def resaltar(msg: str) -> str: return f"{MAGENTA}{NEGRITA}{msg}{RESET}"

def linea(char: str = '─', ancho: int = 60, color: str = GRIS) -> str:
    return f"{color}{char * ancho}{RESET}"


# ─────────────────────────────────────────────
#  Helpers de alineado ANSI-aware
# ─────────────────────────────────────────────

def _len_visible(s: str) -> int:
    """Longitud real ignorando códigos de escape ANSI."""
    return len(re.sub(r'\033\[[0-9;]*m', '', s))

def _pad(s: str, ancho: int, alinear: str = 'izq') -> str:
    """Rellena con espacios considerando solo caracteres visibles."""
    espacios = max(0, ancho - _len_visible(s))
    return (' ' * espacios + s) if alinear == 'der' else (s + ' ' * espacios)


# ─────────────────────────────────────────────
#  Catálogo
# ─────────────────────────────────────────────

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


def _buscar_por_id(catalogo: list, juego_id: str) -> dict | None:
    return next((f for f in catalogo if str(f['id']) == str(juego_id)), None)


# ─────────────────────────────────────────────
#  Helpers de color
# ─────────────────────────────────────────────

def _color_esrb(esrb: str) -> str:
    mapa = {
        'E':    f"{VERDE}{NEGRITA}E{RESET}",
        'E10+': f"{VERDE}E10+{RESET}",
        'T':    f"{AMARILLO}{NEGRITA}T{RESET}",
        'M':    f"{ROJO}{NEGRITA}M{RESET}",
        'AO':   f"{MAGENTA}{NEGRITA}AO{RESET}",
        'RP':   f"{GRIS}RP{RESET}",
    }
    return mapa.get(esrb.strip().upper(), f"{GRIS}{esrb}{RESET}")


def _color_stock(stock: int) -> str:
    if stock == 0:
        return f"{ROJO}{NEGRITA}{stock}{RESET}"
    elif stock <= 3:
        return f"{AMARILLO}{stock}{RESET}"
    return f"{VERDE}{stock}{RESET}"


def _color_consola(consola: str) -> str:
    mapa = {
        'ps5':    f"{AZUL}{NEGRITA}PS5{RESET}",
        'xbox':   f"{VERDE}{NEGRITA}Xbox{RESET}",
        'switch': f"{ROJO}{NEGRITA}Nintendo{RESET}",
    }
    return mapa.get(consola.strip().lower(), consola)


# ─────────────────────────────────────────────
#  Modelos
# ─────────────────────────────────────────────

class VideoGame:
    def __init__(self, id, title, genre, price, esrb, consola, stock):
        self.id      = id
        self.title   = title
        self.genre   = genre
        self.price   = float(price)
        self.esrb    = esrb.strip().upper()
        self.consola = consola
        self.stock   = int(stock)

    def to_dict(self):
        return {
            "id":      self.id,
            "title":   self.title,
            "genre":   self.genre,
            "price":   self.price,
            "esrb":    self.esrb,
            "consola": self.consola,
            "stock":   self.stock,
        }


# ─────────────────────────────────────────────
#  Mostrar catálogo (alineado ANSI-aware)
# ─────────────────────────────────────────────

# Anchos visibles de cada columna
_W = {
    'id':      4,
    'titulo':  32,
    'genero':  13,
    'precio':  9,
    'esrb':    4,
    'consola': 8,
    'stock':   5,
}
_SEP_ANCHO = sum(_W.values()) + len(_W) * 2 + 2   # 2 espacios entre columnas + sangría


def mostrar_juegos(catalogo: list):
    sep = linea('─', _SEP_ANCHO)
    print(f"\n{titulo('─── Juegos Disponibles ───')}")
    print(sep)

    # Cabecera (texto plano, f-string normal)
    print(
        f"  {NEGRITA}"
        f"{'ID':<{_W['id']}}  "
        f"{'Título':<{_W['titulo']}}  "
        f"{'Género':<{_W['genero']}}  "
        f"{'Precio':>{_W['precio']}}  "
        f"{'ESRB':<{_W['esrb']}}  "
        f"{'Consola':<{_W['consola']}}  "
        f"{'Stock':>{_W['stock']}}"
        f"{RESET}"
    )
    print(sep)

    for row in catalogo:
        id_s      = f"{GRIS}{row['id']}{RESET}"
        titulo_s  = f"{BLANCO}{row['title']}{RESET}"
        genero_s  = f"{DIM}{row['genre']}{RESET}"
        precio_s  = f"{AMARILLO}${float(row['price']):.2f}{RESET}"
        esrb_s    = _color_esrb(str(row.get('esrb', 'RP')))
        consola_s = _color_consola(str(row.get('consola', '?')))
        stock_s   = _color_stock(int(row['stock']))

        print(
            f"  "
            f"{_pad(id_s,      _W['id'])}  "
            f"{_pad(titulo_s,  _W['titulo'])}  "
            f"{_pad(genero_s,  _W['genero'])}  "
            f"{_pad(precio_s,  _W['precio'], 'der')}  "
            f"{_pad(esrb_s,    _W['esrb'])}  "
            f"{_pad(consola_s, _W['consola'])}  "
            f"{_pad(stock_s,   _W['stock'], 'der')}"
        )

    print(sep)


# ─────────────────────────────────────────────
#  Carrito de Compras
# ─────────────────────────────────────────────

# Anchos del carrito
_WC = {
    'id':       4,
    'titulo':  30,
    'esrb':     4,
    'precio':   9,
    'cant':     4,
    'subtotal': 10,
}
_SEP_CARRITO = sum(_WC.values()) + len(_WC) * 2 + 2


class CarritoCompras:

    def __init__(self):
        self.items: dict = {}

    def agregar(self, catalogo: list, juego_id: str, cantidad: int = 1) -> str:
        fila = _buscar_por_id(catalogo, juego_id)
        if fila is None:
            return err("ID no encontrado.")

        stock_disponible = int(fila['stock'])
        ya_en_carrito    = self.items.get(str(juego_id), {}).get('cantidad', 0)

        if cantidad <= 0:
            return err("La cantidad debe ser mayor a 0.")
        if ya_en_carrito + cantidad > stock_disponible:
            return err(f"Stock insuficiente. Disponible: {stock_disponible - ya_en_carrito}")

        if str(juego_id) in self.items:
            self.items[str(juego_id)]['cantidad'] += cantidad
        else:
            self.items[str(juego_id)] = {
                "title":    fila['title'],
                "price":    float(fila['price']),
                "esrb":     fila.get('esrb', 'RP'),
                "cantidad": cantidad,
            }

        fila['stock'] = stock_disponible - ya_en_carrito - cantidad
        return ok(f"{CYAN}'{fila['title']}'{RESET}{VERDE} x{cantidad} agregado al carrito.")

    def eliminar(self, juego_id: str, catalogo: list) -> str:
        if str(juego_id) not in self.items:
            return err("El juego no está en el carrito.")
        datos = self.items.pop(str(juego_id))
        fila  = _buscar_por_id(catalogo, juego_id)
        if fila:
            fila['stock'] = int(fila['stock']) + datos['cantidad']
        return ok(f"{CYAN}'{datos['title']}'{RESET}{VERDE} eliminado del carrito.")

    def vaciar(self, catalogo: list = None):
        if catalogo is not None:
            for jid, datos in self.items.items():
                fila = _buscar_por_id(catalogo, jid)
                if fila:
                    fila['stock'] = int(fila['stock']) + datos['cantidad']
        self.items.clear()
        print(f"{AMARILLO}🗑️  Carrito vaciado.{RESET}")

    def total(self) -> float:
        return sum(v['price'] * v['cantidad'] for v in self.items.values())

    def esta_vacio(self) -> bool:
        return len(self.items) == 0

    # ── Vista del carrito (alineado ANSI-aware) ──

    def mostrar(self):
        if self.esta_vacio():
            print(f"\n{AMARILLO}🛒 El carrito está vacío.{RESET}")
            return

        sep = linea('─', _SEP_CARRITO)
        print(f"\n{CYAN}{NEGRITA}🛒  Carrito de Compras{RESET}")
        print(sep)

        # Cabecera plana
        print(
            f"  {NEGRITA}"
            f"{'ID':<{_WC['id']}}  "
            f"{'Título':<{_WC['titulo']}}  "
            f"{'ESRB':<{_WC['esrb']}}  "
            f"{'Precio':>{_WC['precio']}}  "
            f"{'Cant':>{_WC['cant']}}  "
            f"{'Subtotal':>{_WC['subtotal']}}"
            f"{RESET}"
        )
        print(sep)

        for jid, datos in self.items.items():
            subtotal  = datos['price'] * datos['cantidad']
            id_s      = f"{GRIS}{jid}{RESET}"
            titulo_s  = f"{BLANCO}{datos['title']}{RESET}"
            esrb_s    = _color_esrb(datos.get('esrb', 'RP'))
            precio_s  = f"{AMARILLO}${datos['price']:.2f}{RESET}"
            cant_s    = f"{CYAN}{datos['cantidad']}{RESET}"
            sub_s     = f"{VERDE}${subtotal:.2f}{RESET}"

            print(
                f"  "
                f"{_pad(id_s,     _WC['id'])}  "
                f"{_pad(titulo_s, _WC['titulo'])}  "
                f"{_pad(esrb_s,   _WC['esrb'])}  "
                f"{_pad(precio_s, _WC['precio'], 'der')}  "
                f"{_pad(cant_s,   _WC['cant'],   'der')}  "
                f"{_pad(sub_s,    _WC['subtotal'],'der')}"
            )

        print(sep)

        # Línea de total alineada a la derecha
        total_s  = f"{MAGENTA}{NEGRITA}${self.total():.2f}{RESET}"
        label_s  = f"{NEGRITA}TOTAL{RESET}"
        ancho_tot = _SEP_CARRITO - 2   # descuenta sangría
        espacios  = ancho_tot - _len_visible(label_s) - _len_visible(total_s)
        print(f"  {label_s}{' ' * max(0, espacios)}{total_s}")
        print(sep)

    # ── Factura en pantalla (alineado ANSI-aware) ──

    def generar_factura(self) -> str:
        if self.esta_vacio():
            return err("El carrito está vacío, no hay factura que generar.")

        ANCHO  = 62
        SEP_D  = f"{MAGENTA}{'═' * ANCHO}{RESET}"
        SEP_S  = f"{GRIS}{'-' * ANCHO}{RESET}"

        _WF = {'titulo': 26, 'esrb': 4, 'cant': 4, 'subtotal': 10}

        lineas = [
            SEP_D,
            f"{MAGENTA}{NEGRITA}{'TIENDA DE VIDEOJUEGOS 🎮':^{ANCHO}}{RESET}",
            f"{CYAN}{'FACTURA DE COMPRA':^{ANCHO}}{RESET}",
            SEP_D,
        ]

        # Cabecera de columnas (texto plano)
        lineas.append(
            f"  {NEGRITA}"
            f"{'Título':<{_WF['titulo']}}  "
            f"{'ESRB':<{_WF['esrb']}}  "
            f"{'Cant':>{_WF['cant']}}  "
            f"{'Subtotal':>{_WF['subtotal']}}"
            f"{RESET}"
        )
        lineas.append(SEP_S)

        for datos in self.items.values():
            subtotal = datos['price'] * datos['cantidad']
            tit_s    = f"{BLANCO}{datos['title']}{RESET}"
            esrb_s   = _color_esrb(datos.get('esrb', 'RP'))
            cant_s   = f"{CYAN}{datos['cantidad']}{RESET}"
            sub_s    = f"{AMARILLO}${subtotal:.2f}{RESET}"

            lineas.append(
                f"  "
                f"{_pad(tit_s,  _WF['titulo'])}  "
                f"{_pad(esrb_s, _WF['esrb'])}  "
                f"{_pad(cant_s, _WF['cant'],     'der')}  "
                f"{_pad(sub_s,  _WF['subtotal'], 'der')}"
            )

        total_s  = f"{MAGENTA}{NEGRITA}${self.total():.2f}{RESET}"
        label_s  = f"{NEGRITA}TOTAL A PAGAR{RESET}"
        espacios = ANCHO - _len_visible(label_s) - _len_visible(total_s)
        lineas  += [
            SEP_S,
            f"  {label_s}{' ' * max(0, espacios - 2)}{total_s}",
            SEP_D,
            f"{VERDE}{NEGRITA}{'¡Gracias por su visita!':^{ANCHO}}{RESET}",
            SEP_D,
        ]
        return "\n".join(lineas)

    # ── Finalizar compra ──

    def finalizar_compra(self, catalogo: list) -> list:
        if self.esta_vacio():
            print(err("El carrito está vacío."))
            return catalogo

        self.mostrar()
        confirmar = input(f"\n{AMARILLO}¿Confirmar compra? (s/n): {RESET}").strip().lower()
        if confirmar != 's':
            print(f"{ROJO}🔙 Compra cancelada.{RESET}")
            return catalogo

        total_compra   = self.total()
        items_comprados = dict(self.items)

        print(f"\n{ok(f'Compra realizada! Total cobrado: {precio(total_compra)}')}")
        print(f"{CYAN}🎮 ¡Gracias por su compra!{RESET}")

        guardar_factura_archivo(items_comprados, total_compra)

        self.items.clear()
        print(f"{AMARILLO}🗑️  Carrito vaciado.{RESET}")
        return catalogo


# ─────────────────────────────────────────────
#  Carga y guardado de datos
# ─────────────────────────────────────────────

def leer_csv() -> list:
    clear()
    ruta = os.path.join(DATA_DIR, 'catalogo.csv')
    print(info("Cargando catálogo desde CSV..."))
    with open(ruta, newline='', encoding='utf-8') as f:
        catalogo = [_normalizar_fila(dict(row)) for row in csv.DictReader(f)]
    catalogo = [f for f in catalogo if f.get('price') is not None]
    return _validar_catalogo(catalogo, 'catalogo.csv')


def leer_json() -> list:
    clear()
    ruta = os.path.join(DATA_DIR, 'catalogo.json')
    print(info("Cargando catálogo desde JSON..."))
    with open(ruta, 'r', encoding='utf-8') as f:
        datos = json.load(f)
    catalogo = [_normalizar_fila(dict(fila)) for fila in datos]
    catalogo = [f for f in catalogo if f.get('price') is not None]
    return _validar_catalogo(catalogo, 'catalogo.json')


def guardar_catalogo(catalogo: list):
    print(f"\n{titulo('¿En qué formato desea guardar?')}")
    print(f"  {AMARILLO}1.{RESET} CSV")
    print(f"  {AMARILLO}2.{RESET} JSON")
    opcion = input(f"{AZUL}Seleccione: {RESET}").strip()

    if opcion == '1':
        ruta = os.path.join(DATA_DIR, 'catalogo.csv')
        fieldnames = ['id', 'title', 'genre', 'price', 'esrb', 'consola', 'stock']
        with open(ruta, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(catalogo)
        print(ok("Guardado en CSV"))

    elif opcion == '2':
        ruta = os.path.join(DATA_DIR, 'catalogo.json')
        with open(ruta, 'w', encoding='utf-8') as f:
            json.dump(catalogo, f, indent=4, ensure_ascii=False)
        print(ok("Guardado en JSON"))

    else:
        print(err("Opción inválida. No se guardó."))


# ─────────────────────────────────────────────
#  Guardar factura en archivo
# ─────────────────────────────────────────────

def guardar_factura_archivo(items: dict, total_compra: float):
    import datetime

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


def seleccionar_formato() -> list:
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


# ─────────────────────────────────────────────
#  Operaciones de catálogo
# ─────────────────────────────────────────────

def agregar_videojuego(catalogo: list) -> list:
    print(f"\n{titulo('─── Agregar Nuevo Videojuego ───')}")

    ids_existentes = {str(f['id']) for f in catalogo}

    while True:
        id_ = input(f"  {CYAN}ID:{RESET} ").strip()
        if not id_:
            print(err("El ID no puede estar vacío.\n"))
        elif not id_.isdigit():
            print(err("El ID debe ser numérico.\n"))
        elif id_ in ids_existentes:
            print(err("ID ya existe.\n"))
        else:
            break

    while True:
        t = input(f"  {CYAN}Título:{RESET} ").strip()
        if t:
            break
        print(err("No puede estar vacío."))

    while True:
        g = input(f"  {CYAN}Género:{RESET} ").strip()
        if not g:
            print(warn("Género no puede estar vacío\n"))
        elif g.isdigit():
            print(err("El género no puede ser solo números.\n"))
        else:
            break

    opciones_esrb = ' / '.join(ESRB_VALIDOS)
    while True:
        e = input(f"  {CYAN}Clasificación ESRB {GRIS}({opciones_esrb}){RESET}: ").strip().upper()
        if e in ESRB_VALIDOS:
            break
        print(err(f"ESRB inválido. Opciones: {opciones_esrb}\n"))

    while True:
        c = input(f"  {CYAN}Consola {GRIS}(ps5 / xbox / switch){RESET}: ").strip().lower()
        if c in ['ps5', 'xbox', 'switch']:
            break
        print(err("Consola inválida. Use: ps5, xbox o switch.\n"))

    while True:
        try:
            p = float(input(f"  {CYAN}Precio:{RESET} "))
            if p < 0:
                print(err("No puede ser negativo.\n"))
            else:
                break
        except ValueError:
            print(err("Ingrese un número válido.\n"))

    while True:
        try:
            s = int(input(f"  {CYAN}Stock:{RESET} "))
            if s < 0:
                print(err("No puede ser negativo.\n"))
            else:
                break
        except ValueError:
            print(err("Ingrese un número válido.\n"))

    juego = VideoGame(id_, t, g, p, e, c, s)
    catalogo.append(juego.to_dict())
    print(ok("Videojuego agregado correctamente."))
    return catalogo


# ─────────────────────────────────────────────
#  Submenú carrito
# ─────────────────────────────────────────────

def _cabecera(icono: str, texto: str):
    sep = linea('═', 38, CYAN)
    print(sep)
    print(f"{CYAN}{NEGRITA}  {icono}  {texto}{RESET}")
    print(sep)


def menu_carrito(catalogo: list, carrito: CarritoCompras) -> list:
    while True:
        clear()
        _cabecera("🛒", "CARRITO DE COMPRAS")

        opciones = [
            ("1", "Ver juegos disponibles"),
            ("2", "Agregar juego al carrito"),
            ("3", "Eliminar juego del carrito"),
            ("4", "Ver carrito"),
            ("5", "Finalizar compra"),
            ("6", "Ver factura"),
            ("7", "Vaciar carrito"),
            ("8", "Volver al menú principal"),
        ]
        for num, texto in opciones:
            print(f"  {AMARILLO}{num}.{RESET} {texto}")
        print()

        opcion = input(f"{AZUL}Seleccione: {RESET}").strip()

        if opcion == '1':
            mostrar_juegos(catalogo)
            volver_a_menu()

        elif opcion == '2':
            mostrar_juegos(catalogo)

            while True:
                jid = input(f"{AZUL}ID del juego a agregar: {RESET}").strip()
                if not jid:
                    print(err("El ID no puede estar vacío.\n"))
                elif not jid.isdigit():
                    print(err("El ID debe ser numérico positivo.\n"))
                else:
                    fila = _buscar_por_id(catalogo, jid)
                    if fila is None:
                        print(err("Ese ID no existe.\n"))
                    else:
                        stock = int(fila['stock'])
                        if stock == 0:
                            print(err(f"'{fila['title']}' no tiene stock disponible.\n"))
                        else:
                            print(f"'{fila['title']}' — {VERDE}{stock}{RESET} unidad(es) disponibles.\n")
                            break

            while True:
                cant_input = input(f"{AZUL}Cantidad: {RESET}").strip()
                if not cant_input:
                    print(err("La cantidad no puede estar vacía.\n"))
                elif not cant_input.isdigit():
                    print(err("La cantidad debe ser un número positivo.\n"))
                else:
                    cant = int(cant_input)
                    if cant <= 0:
                        print(err("La cantidad debe ser mayor que 0.\n"))
                    elif cant > stock:
                        print(err(f"Solo hay {stock} unidades disponibles.\n"))
                    else:
                        print(carrito.agregar(catalogo, jid, cant))
                        break

            volver_a_menu()

        elif opcion == '3':
            carrito.mostrar()
            jid = input(f"{AZUL}ID del juego a eliminar: {RESET}").strip()
            print(carrito.eliminar(jid, catalogo))
            volver_a_menu()

        elif opcion == '4':
            carrito.mostrar()
            volver_a_menu()

        elif opcion == '5':
            catalogo = carrito.finalizar_compra(catalogo)
            volver_a_menu()

        elif opcion == '6':
            print(carrito.generar_factura())
            volver_a_menu()

        elif opcion == '7':
            carrito.vaciar(catalogo)
            volver_a_menu()

        elif opcion == '8':
            break

        else:
            print(err("Opción inválida."))
            volver_a_menu()

    return catalogo


# ─────────────────────────────────────────────
#  Utilidades
# ─────────────────────────────────────────────

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def volver_a_menu():
    input(f"\n{GRIS}Presione Enter para continuar...{RESET}")


# ─────────────────────────────────────────────
#  Menú principal
# ─────────────────────────────────────────────

BANNER = f"""{CYAN}{NEGRITA}
  ╔══════════════════════════════════════╗
  ║      TIENDA DE VIDEOJUEGOS  🎮       ║
  ╚══════════════════════════════════════╝{RESET}"""


def menu():
    carrito  = CarritoCompras()
    catalogo: list = []

    while True:
        clear()
        print(BANNER)

        n_items = sum(v['cantidad'] for v in carrito.items.values())
        if n_items:
            print(f"  {MAGENTA}🛒  {n_items} ítem(s) en el carrito — total {precio(carrito.total())}{RESET}")
        print()

        for num, icono, texto in [
            ("1", "📋", "Catálogo de VideoJuegos"),
            ("2", "➕", "Agregar Videojuego"),
            ("3", "🛒", "Carrito de Compras"),
            ("4", "🚪", "Salir"),
        ]:
            print(f"  {AMARILLO}{num}.{RESET} {icono}  {texto}")

        print()
        opcion = input(f"{AZUL}Seleccione una opción: {RESET}").strip()

        if opcion == '1':
            clear()
            print(titulo("Seleccione el formato del catálogo:"))
            catalogo = seleccionar_formato()
            mostrar_juegos(catalogo)
            volver_a_menu()

        elif opcion == '2':
            clear()
            if catalogo:
                recargar = input(
                    f"{AMARILLO}Ya hay un catálogo cargado. ¿Recargar desde archivo? (s/n): {RESET}"
                ).strip().lower()
                if recargar == 's':
                    print(titulo("Seleccione el formato del catálogo:"))
                    catalogo = seleccionar_formato()
                elif recargar != 'n':
                    print(warn("Opción inválida, continuando sin recargar."))
            else:
                print(titulo("Seleccione el formato del catálogo:"))
                catalogo = seleccionar_formato()

            catalogo = agregar_videojuego(catalogo)
            guardar_catalogo(catalogo)
            volver_a_menu()

        elif opcion == '3':
            if not catalogo:
                print(warn("Cargue el catálogo primero (opción 1)."))
                volver_a_menu()
            else:
                catalogo = menu_carrito(catalogo, carrito)

        elif opcion == '4':
            print(f"\n{VERDE}{NEGRITA}¡Gracias por visitar la Tienda de Videojuegos! ¡Hasta luego! 👋{RESET}\n")
            break

        else:
            print(err("Opción inválida."))
            volver_a_menu()


if __name__ == "__main__":
    try:
        menu()
    except SalidaForzada:
        salir()