"""
ui/menus.py
Funciones de menú: principal, catálogo y carrito.
"""
import os

from models.videojuego import VideoJuego, JuegoPS5, JuegoXbox, JuegoNintendo, crear_juego
from models.carrito import CarritoCompras
from ui.vistas import mostrar_juegos
from utils.archivos import seleccionar_formato, guardar_catalogo
from utils.excepciones import input
from utils.colors import (
    ok, err, warn, titulo, precio, linea,
    RESET, NEGRITA, VERDE, AMARILLO, ROJO, CYAN, MAGENTA, AZUL, GRIS
)

ESRB_VALIDOS = ['E', 'E10+', 'T', 'M', 'AO', 'RP']


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def volver_a_menu():
    input(f"\n{GRIS}Presione Enter para continuar...{RESET}")


def _cabecera(icono: str, texto: str):
    sep = linea('═', 38, CYAN)
    print(sep)
    print(f"{CYAN}{NEGRITA}  {icono}  {texto}{RESET}")
    print(sep)


def _buscar_por_id(catalogo: list, juego_id: str):
    return next((f for f in catalogo if str(f['id']) == str(juego_id)), None)


# ── Agregar videojuego ─────────────────────────

def agregar_videojuego(catalogo: list) -> list:
    """
    Solicita datos al usuario, valida y crea la instancia correcta
    según la consola (polimorfismo con factory).
    """
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

    # Usar factory para crear la subclase correcta (polimorfismo)
    datos = {'id': id_, 'title': t, 'genre': g, 'price': p,
             'esrb': e, 'consola': c, 'stock': s}
    juego = crear_juego(datos)

    # Demo de polimorfismo: muestra descripción específica de plataforma
    print(f"\n{CYAN}🎮 {juego.descripcion_consola()}{RESET}")
    print(ok("Videojuego agregado correctamente."))

    catalogo.append(juego.to_dict())
    return catalogo


# ── Submenú carrito ────────────────────────────

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


# ── Menú principal ─────────────────────────────

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

        n_items = carrito.cantidad_total
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
