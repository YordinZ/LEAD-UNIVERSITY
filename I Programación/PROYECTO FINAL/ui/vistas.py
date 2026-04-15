"""
ui/vistas.py
Funciones de visualización del catálogo en terminal.
"""
from utils.colors import (
    titulo, linea,
    RESET, NEGRITA, GRIS, BLANCO, DIM, AMARILLO, CYAN,
    pad, color_esrb, color_stock, color_consola
)

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
_SEP_ANCHO = sum(_W.values()) + len(_W) * 2 + 2


def mostrar_juegos(catalogo: list):
    """Muestra el catálogo completo alineado y con colores ANSI."""
    sep = linea('─', _SEP_ANCHO)
    print(f"\n{titulo('─── Juegos Disponibles ───')}")
    print(sep)

    # Cabecera
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
        # Soporta tanto dicts como objetos VideoJuego
        if hasattr(row, 'to_dict'):
            row = row.to_dict()

        id_s      = f"{GRIS}{row['id']}{RESET}"
        titulo_s  = f"{BLANCO}{row['title']}{RESET}"
        genero_s  = f"{DIM}{row['genre']}{RESET}"
        precio_s  = f"{AMARILLO}${float(row['price']):.2f}{RESET}"
        esrb_s    = color_esrb(str(row.get('esrb', 'RP')))
        consola_s = color_consola(str(row.get('consola', '?')))
        stock_s   = color_stock(int(row['stock']))

        print(
            f"  "
            f"{pad(id_s,      _W['id'])}  "
            f"{pad(titulo_s,  _W['titulo'])}  "
            f"{pad(genero_s,  _W['genero'])}  "
            f"{pad(precio_s,  _W['precio'], 'der')}  "
            f"{pad(esrb_s,    _W['esrb'])}  "
            f"{pad(consola_s, _W['consola'])}  "
            f"{pad(stock_s,   _W['stock'], 'der')}"
        )

    print(sep)
