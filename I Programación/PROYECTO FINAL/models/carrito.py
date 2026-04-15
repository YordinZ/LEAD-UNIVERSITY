"""
models/carrito.py
Clase CarritoCompras: gestiona los ítems, muestra contenido y genera facturas.
"""
from utils.colors import (
    ok, err, warn, precio,
    RESET, NEGRITA, VERDE, AMARILLO, ROJO, CYAN, MAGENTA, AZUL, GRIS, BLANCO,
    linea, len_visible, pad, color_esrb
)
from utils.archivos import guardar_factura_archivo


def _buscar_por_id(catalogo: list, juego_id: str):
    return next((f for f in catalogo if str(f['id']) == str(juego_id)), None)


# Anchos del carrito
_WC = {'id': 4, 'titulo': 30, 'esrb': 4, 'precio': 9, 'cant': 4, 'subtotal': 10}
_SEP_CARRITO = sum(_WC.values()) + len(_WC) * 2 + 2


class CarritoCompras:
    """Gestiona el carrito de compras con validación de stock."""

    def __init__(self):
        self.__items: dict = {}   # encapsulado con nombre mangled

    # ── @property ──────────────────────────────

    @property
    def items(self) -> dict:
        return self.__items

    @property
    def cantidad_total(self) -> int:
        return sum(v['cantidad'] for v in self.__items.values())

    # ── Operaciones ────────────────────────────

    def agregar(self, catalogo: list, juego_id: str, cantidad: int = 1) -> str:
        fila = _buscar_por_id(catalogo, juego_id)
        if fila is None:
            return err("ID no encontrado.")

        stock_disponible = int(fila['stock'])
        ya_en_carrito    = self.__items.get(str(juego_id), {}).get('cantidad', 0)

        if cantidad <= 0:
            return err("La cantidad debe ser mayor a 0.")
        if ya_en_carrito + cantidad > stock_disponible:
            return err(f"Stock insuficiente. Disponible: {stock_disponible - ya_en_carrito}")

        if str(juego_id) in self.__items:
            self.__items[str(juego_id)]['cantidad'] += cantidad
        else:
            self.__items[str(juego_id)] = {
                "title":    fila['title'],
                "price":    float(fila['price']),
                "esrb":     fila.get('esrb', 'RP'),
                "cantidad": cantidad,
            }

        fila['stock'] = stock_disponible - ya_en_carrito - cantidad
        return ok(f"{CYAN}'{fila['title']}'{RESET}{VERDE} x{cantidad} agregado al carrito.")

    def eliminar(self, juego_id: str, catalogo: list) -> str:
        if str(juego_id) not in self.__items:
            return err("El juego no está en el carrito.")
        datos = self.__items.pop(str(juego_id))
        fila  = _buscar_por_id(catalogo, juego_id)
        if fila:
            fila['stock'] = int(fila['stock']) + datos['cantidad']
        return ok(f"{CYAN}'{datos['title']}'{RESET}{VERDE} eliminado del carrito.")

    def vaciar(self, catalogo: list = None):
        if catalogo is not None:
            for jid, datos in self.__items.items():
                fila = _buscar_por_id(catalogo, jid)
                if fila:
                    fila['stock'] = int(fila['stock']) + datos['cantidad']
        self.__items.clear()
        print(f"{AMARILLO}🗑️  Carrito vaciado.{RESET}")

    def total(self) -> float:
        return sum(v['price'] * v['cantidad'] for v in self.__items.values())

    def esta_vacio(self) -> bool:
        return len(self.__items) == 0

    # ── Vista del carrito ──────────────────────

    def mostrar(self):
        if self.esta_vacio():
            print(f"\n{AMARILLO}🛒 El carrito está vacío.{RESET}")
            return

        sep = linea('─', _SEP_CARRITO)
        print(f"\n{CYAN}{NEGRITA}🛒  Carrito de Compras{RESET}")
        print(sep)
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

        for jid, datos in self.__items.items():
            subtotal  = datos['price'] * datos['cantidad']
            id_s      = f"{GRIS}{jid}{RESET}"
            titulo_s  = f"{BLANCO}{datos['title']}{RESET}"
            esrb_s    = color_esrb(datos.get('esrb', 'RP'))
            precio_s  = f"{AMARILLO}${datos['price']:.2f}{RESET}"
            cant_s    = f"{CYAN}{datos['cantidad']}{RESET}"
            sub_s     = f"{VERDE}${subtotal:.2f}{RESET}"

            print(
                f"  "
                f"{pad(id_s,     _WC['id'])}  "
                f"{pad(titulo_s, _WC['titulo'])}  "
                f"{pad(esrb_s,   _WC['esrb'])}  "
                f"{pad(precio_s, _WC['precio'], 'der')}  "
                f"{pad(cant_s,   _WC['cant'],   'der')}  "
                f"{pad(sub_s,    _WC['subtotal'],'der')}"
            )

        print(sep)
        total_s  = f"{MAGENTA}{NEGRITA}${self.total():.2f}{RESET}"
        label_s  = f"{NEGRITA}TOTAL{RESET}"
        ancho_tot = _SEP_CARRITO - 2
        espacios  = ancho_tot - len_visible(label_s) - len_visible(total_s)
        print(f"  {label_s}{' ' * max(0, espacios)}{total_s}")
        print(sep)

    # ── Factura en pantalla ────────────────────

    def generar_factura(self) -> str:
        if self.esta_vacio():
            return err("El carrito está vacío, no hay factura que generar.")

        ANCHO = 62
        SEP_D = f"{MAGENTA}{'═' * ANCHO}{RESET}"
        SEP_S = f"{GRIS}{'-' * ANCHO}{RESET}"
        _WF   = {'titulo': 26, 'esrb': 4, 'cant': 4, 'subtotal': 10}

        lineas = [
            SEP_D,
            f"{MAGENTA}{NEGRITA}{'TIENDA DE VIDEOJUEGOS 🎮':^{ANCHO}}{RESET}",
            f"{CYAN}{'FACTURA DE COMPRA':^{ANCHO}}{RESET}",
            SEP_D,
            f"  {NEGRITA}"
            f"{'Título':<{_WF['titulo']}}  "
            f"{'ESRB':<{_WF['esrb']}}  "
            f"{'Cant':>{_WF['cant']}}  "
            f"{'Subtotal':>{_WF['subtotal']}}"
            f"{RESET}",
            SEP_S,
        ]

        for datos in self.__items.values():
            subtotal = datos['price'] * datos['cantidad']
            tit_s    = f"{BLANCO}{datos['title']}{RESET}"
            esrb_s   = color_esrb(datos.get('esrb', 'RP'))
            cant_s   = f"{CYAN}{datos['cantidad']}{RESET}"
            sub_s    = f"{AMARILLO}${subtotal:.2f}{RESET}"
            lineas.append(
                f"  "
                f"{pad(tit_s,  _WF['titulo'])}  "
                f"{pad(esrb_s, _WF['esrb'])}  "
                f"{pad(cant_s, _WF['cant'],     'der')}  "
                f"{pad(sub_s,  _WF['subtotal'], 'der')}"
            )

        total_s  = f"{MAGENTA}{NEGRITA}${self.total():.2f}{RESET}"
        label_s  = f"{NEGRITA}TOTAL A PAGAR{RESET}"
        espacios = ANCHO - len_visible(label_s) - len_visible(total_s)
        lineas  += [
            SEP_S,
            f"  {label_s}{' ' * max(0, espacios - 2)}{total_s}",
            SEP_D,
            f"{VERDE}{NEGRITA}{'¡Gracias por su visita!':^{ANCHO}}{RESET}",
            SEP_D,
        ]
        return "\n".join(lineas)

    # ── Finalizar compra ───────────────────────

    def finalizar_compra(self, catalogo: list) -> list:
        from utils.excepciones import input
        if self.esta_vacio():
            print(err("El carrito está vacío."))
            return catalogo

        self.mostrar()
        confirmar = input(f"\n{AMARILLO}¿Confirmar compra? (s/n): {RESET}").strip().lower()
        if confirmar != 's':
            print(f"{ROJO}🔙 Compra cancelada.{RESET}")
            return catalogo

        total_compra    = self.total()
        items_comprados = dict(self.__items)

        print(f"\n{ok(f'Compra realizada! Total cobrado: {precio(total_compra)}')}")
        print(f"{CYAN}🎮 ¡Gracias por su compra!{RESET}")

        guardar_factura_archivo(items_comprados, total_compra)

        self.__items.clear()
        print(f"{AMARILLO}🗑️  Carrito vaciado.{RESET}")
        return catalogo
