import json
import os
import sys
import time


# RUTAS BASE DEL PROYECTO
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
RUTA_JSON = os.path.join(DATA_DIR, "super_smash.json")


# Códigos ANSI para colorear la salida en consola.
# No uso librerías externas (colorama, etc.), solo códigos de escape.
class Colores:

    RESET = "\033[0m"

    ROJO = "\033[1;31m"

    # El negro puro no se ve en una terminal con fondo oscuro,
    # así que lo muestro como texto negro sobre fondo gris claro.
    NEGRO = "\033[1;30;47m"

    GRIS = "\033[90m"

    NEGRITA = "\033[1m"


def habilitar_ansi_windows():
    # En Windows la consola no procesa códigos ANSI por defecto.
    # Esta llamada vacía a os.system activa ese modo sin necesitar
    # ninguna librería adicional.
    if os.name == "nt":
        os.system("")


def limpiar_pantalla():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def barra_progreso(actual, total, prefijo="Cargando"):

    if total == 0:
        return

    longitud = 35
    fraccion = actual / total
    llenado = int(longitud * fraccion)

    barra = "█" * llenado + "░" * (longitud - llenado)
    porcentaje = round(fraccion * 100, 1)

    sys.stdout.write(
        f"\r{Colores.ROJO}{prefijo}{Colores.RESET} "
        f"|{Colores.GRIS}{barra}{Colores.RESET}| "
        f"{porcentaje:>5.1f}%"
    )

    sys.stdout.flush()

    if actual >= total:
        print()


# ÁRBOL ROJO-NEGRO (ordenado por ataque)
class NodoRN:

    def __init__(self, personaje=None, color="NEGRO"):

        self.ataque = personaje["ataque"] if personaje else None
        self.personaje = personaje

        self.color = color

        self.izquierdo = None
        self.derecho = None
        self.padre = None


class ArbolRojoNegro:

    def __init__(self):

        # Nodo centinela NIL: representa todas las hojas vacías.
        # Siempre es negro. Usarlo en vez de None es lo que permite
        # corregir bien la eliminación, porque a diferencia de None,
        # el NIL sí puede tener color y un padre asociado.
        self.NIL = NodoRN(color="NEGRO")
        self.raiz = self.NIL

    def buscar(self, ataque):

        actual = self.raiz

        while actual is not self.NIL:

            if ataque == actual.ataque:
                return actual

            elif ataque < actual.ataque:
                actual = actual.izquierdo

            else:
                actual = actual.derecho

        return None

    def rotar_izquierda(self, x):

        y = x.derecho

        x.derecho = y.izquierdo

        if y.izquierdo is not self.NIL:
            y.izquierdo.padre = x

        y.padre = x.padre

        if x.padre is None:
            self.raiz = y

        elif x == x.padre.izquierdo:
            x.padre.izquierdo = y

        else:
            x.padre.derecho = y

        y.izquierdo = x
        x.padre = y

    def rotar_derecha(self, x):

        y = x.izquierdo

        x.izquierdo = y.derecho

        if y.derecho is not self.NIL:
            y.derecho.padre = x

        y.padre = x.padre

        if x.padre is None:
            self.raiz = y

        elif x == x.padre.derecho:
            x.padre.derecho = y

        else:
            x.padre.izquierdo = y

        y.derecho = x
        x.padre = y

    def insertar(self, personaje):

        ataque = personaje["ataque"]

        # Si el ataque ya existe, se ignora la inserción.
        if self.buscar(ataque) is not None:

            print(
                f"El ataque {ataque} ya existe. "
                f"Se ignora la inserción de "
                f"{personaje['nombre']}."
            )

            return False

        nuevo = NodoRN(personaje, color="ROJO")
        nuevo.izquierdo = self.NIL
        nuevo.derecho = self.NIL

        # Bajamos por el árbol como en un BST normal
        # para encontrar dónde va el nuevo nodo.
        padre = None
        actual = self.raiz

        while actual is not self.NIL:

            padre = actual

            if nuevo.ataque < actual.ataque:
                actual = actual.izquierdo
            else:
                actual = actual.derecho

        nuevo.padre = padre

        if padre is None:

            self.raiz = nuevo

        elif nuevo.ataque < padre.ataque:

            padre.izquierdo = nuevo

        else:

            padre.derecho = nuevo

        # Si es el primer nodo, se queda negro y ya está.
        if nuevo.padre is None:

            nuevo.color = "NEGRO"
            return True

        # Si el padre es la raíz, no hay abuelo, así que
        # todavía no puede haber conflicto de rojo-rojo.
        if nuevo.padre.padre is None:
            return True

        self.corregir_insercion(nuevo)

        return True

    def corregir_insercion(self, nodo):

        while (
            nodo != self.raiz
            and nodo.padre is not None
            and nodo.padre.color == "ROJO"
        ):

            padre = nodo.padre
            abuelo = padre.padre

            if abuelo is None:
                break

            if padre == abuelo.izquierdo:

                tio = abuelo.derecho

                # Tío rojo: solo hay que recolorear, sin rotar.
                if tio.color == "ROJO":

                    padre.color = "NEGRO"
                    tio.color = "NEGRO"
                    abuelo.color = "ROJO"

                    nodo = abuelo

                else:

                    # Caso triángulo: primero enderezamos con una rotación.
                    if nodo == padre.derecho:

                        nodo = padre
                        self.rotar_izquierda(nodo)

                    # Caso línea: recolorear y rotar el abuelo.
                    nodo.padre.color = "NEGRO"
                    nodo.padre.padre.color = "ROJO"

                    self.rotar_derecha(nodo.padre.padre)

            else:

                tio = abuelo.izquierdo

                if tio.color == "ROJO":

                    padre.color = "NEGRO"
                    tio.color = "NEGRO"
                    abuelo.color = "ROJO"

                    nodo = abuelo

                else:

                    if nodo == padre.izquierdo:

                        nodo = padre
                        self.rotar_derecha(nodo)

                    nodo.padre.color = "NEGRO"
                    nodo.padre.padre.color = "ROJO"

                    self.rotar_izquierda(nodo.padre.padre)

        self.raiz.color = "NEGRO"

    def minimo(self, nodo):

        actual = nodo

        while actual.izquierdo is not self.NIL:
            actual = actual.izquierdo

        return actual

    def transplantar(self, u, v):
        # Reemplaza el subárbol de u por el de v.

        if u.padre is None:

            self.raiz = v

        elif u == u.padre.izquierdo:

            u.padre.izquierdo = v

        else:

            u.padre.derecho = v

        # v puede ser un nodo real o el NIL, y ambos pueden
        # llevar la referencia al padre sin problema.
        v.padre = u.padre

    def eliminar(self, ataque):

        nodo = self.buscar(ataque)

        if nodo is None:
            return False

        y = nodo
        color_original = y.color

        if nodo.izquierdo is self.NIL:

            x = nodo.derecho
            self.transplantar(nodo, nodo.derecho)

        elif nodo.derecho is self.NIL:

            x = nodo.izquierdo
            self.transplantar(nodo, nodo.izquierdo)

        else:

            # Nodo con dos hijos: se reemplaza por su sucesor
            # (el mínimo del subárbol derecho).
            y = self.minimo(nodo.derecho)
            color_original = y.color

            x = y.derecho

            if y.padre == nodo:

                x.padre = y

            else:

                self.transplantar(y, y.derecho)

                y.derecho = nodo.derecho
                y.derecho.padre = y

            self.transplantar(nodo, y)

            y.izquierdo = nodo.izquierdo
            y.izquierdo.padre = y
            y.color = nodo.color

        # Si el nodo eliminado era negro, se rompió el balance
        # de altura negra y hay que corregirlo.
        if color_original == "NEGRO":

            self.corregir_eliminacion(x)

        return True

    def corregir_eliminacion(self, x):

        while x != self.raiz and x.color == "NEGRO":

            padre = x.padre

            if x == padre.izquierdo:

                hermano = padre.derecho

                # Caso 1: el hermano es rojo, lo giramos para
                # que quede un hermano negro y seguir con los otros casos.
                if hermano.color == "ROJO":

                    hermano.color = "NEGRO"
                    padre.color = "ROJO"

                    self.rotar_izquierda(padre)

                    hermano = padre.derecho

                # Caso 2: el hermano y sus dos hijos son negros.
                # Se le pasa el "negro extra" al padre.
                if (
                    hermano.izquierdo.color == "NEGRO"
                    and hermano.derecho.color == "NEGRO"
                ):

                    hermano.color = "ROJO"
                    x = padre

                else:

                    # Caso 3: el hijo derecho del hermano es negro,
                    # se rota para dejarlo en la forma del caso 4.
                    if hermano.derecho.color == "NEGRO":

                        hermano.izquierdo.color = "NEGRO"
                        hermano.color = "ROJO"

                        self.rotar_derecha(hermano)

                        hermano = padre.derecho

                    # Caso 4: rotación final que resuelve el desbalance.
                    hermano.color = padre.color
                    padre.color = "NEGRO"
                    hermano.derecho.color = "NEGRO"

                    self.rotar_izquierda(padre)

                    x = self.raiz

            else:

                hermano = padre.izquierdo

                if hermano.color == "ROJO":

                    hermano.color = "NEGRO"
                    padre.color = "ROJO"

                    self.rotar_derecha(padre)

                    hermano = padre.izquierdo

                if (
                    hermano.derecho.color == "NEGRO"
                    and hermano.izquierdo.color == "NEGRO"
                ):

                    hermano.color = "ROJO"
                    x = padre

                else:

                    if hermano.izquierdo.color == "NEGRO":

                        hermano.derecho.color = "NEGRO"
                        hermano.color = "ROJO"

                        self.rotar_izquierda(hermano)

                        hermano = padre.izquierdo

                    hermano.color = padre.color
                    padre.color = "NEGRO"
                    hermano.izquierdo.color = "NEGRO"

                    self.rotar_derecha(padre)

                    x = self.raiz

        x.color = "NEGRO"

    def mostrar_inorden(self):

        if self.raiz is self.NIL:

            print("El árbol rojo-negro está vacío.")
            return

        print(
            f"\n{Colores.ROJO}ÁRBOL ROJO-NEGRO "
            f"(ordenado por ATAQUE){Colores.RESET}"
        )

        print(f"{Colores.GRIS}{'-' * 75}{Colores.RESET}")

        self._mostrar_inorden(self.raiz)

    def _mostrar_inorden(self, nodo):

        if nodo is self.NIL:
            return

        self._mostrar_inorden(nodo.izquierdo)

        color_txt = self._color_nodo(nodo.color)

        print(
            f"Ataque: {nodo.ataque:<5} | "
            f"Nombre: {nodo.personaje['nombre']:<15} | "
            f"Color: {color_txt}"
        )

        self._mostrar_inorden(nodo.derecho)

    def mostrar_estructura(self):

        if self.raiz is self.NIL:

            print("El árbol rojo-negro está vacío.")
            return

        print(f"\n{Colores.ROJO}ESTRUCTURA DEL ÁRBOL ROJO-NEGRO{Colores.RESET}")
        print(f"{Colores.GRIS}{'-' * 75}{Colores.RESET}")

        self._mostrar_estructura(self.raiz, "", True)

    def _mostrar_estructura(self, nodo, espacio, ultimo):

        if nodo is self.NIL:
            return

        conector = "└── " if ultimo else "├── "
        color_txt = self._color_nodo(nodo.color)

        print(
            f"{Colores.GRIS}{espacio}{conector}{Colores.RESET}"
            f"{nodo.ataque} - {nodo.personaje['nombre']} "
            f"[{color_txt}]"
        )

        nuevo_espacio = espacio + ("    " if ultimo else "│   ")

        hijos = []

        if nodo.izquierdo is not self.NIL:
            hijos.append(nodo.izquierdo)

        if nodo.derecho is not self.NIL:
            hijos.append(nodo.derecho)

        for i, hijo in enumerate(hijos):

            self._mostrar_estructura(
                hijo,
                nuevo_espacio,
                i == len(hijos) - 1
            )

    def _color_nodo(self, color):

        if color == "ROJO":
            return f"{Colores.ROJO} ROJO {Colores.RESET}"

        return f"{Colores.NEGRO} NEGRO {Colores.RESET}"


# ÁRBOL AVL (ordenado por defensa)
class NodoAVL:

    def __init__(self, personaje):

        self.defensa = personaje["defensa"]
        self.personaje = personaje

        self.altura = 1

        self.izquierdo = None
        self.derecho = None


class ArbolAVL:

    def __init__(self):
        self.raiz = None

    def buscar(self, defensa):

        actual = self.raiz

        while actual is not None:

            if defensa == actual.defensa:
                return actual

            elif defensa < actual.defensa:
                actual = actual.izquierdo

            else:
                actual = actual.derecho

        return None

    def obtener_altura(self, nodo):

        if nodo is None:
            return 0

        return nodo.altura

    def actualizar_altura(self, nodo):

        nodo.altura = 1 + max(
            self.obtener_altura(nodo.izquierdo),
            self.obtener_altura(nodo.derecho)
        )

    def obtener_balance(self, nodo):

        if nodo is None:
            return 0

        return (
            self.obtener_altura(nodo.izquierdo)
            - self.obtener_altura(nodo.derecho)
        )

    def rotar_derecha(self, y):

        x = y.izquierdo
        temporal = x.derecho

        x.derecho = y
        y.izquierdo = temporal

        self.actualizar_altura(y)
        self.actualizar_altura(x)

        return x

    def rotar_izquierda(self, x):

        y = x.derecho
        temporal = y.izquierdo

        y.izquierdo = x
        x.derecho = temporal

        self.actualizar_altura(x)
        self.actualizar_altura(y)

        return y

    def insertar(self, personaje):

        defensa = personaje["defensa"]

        if self.buscar(defensa) is not None:

            print(
                f"La defensa {defensa} ya existe. "
                f"Se ignora la inserción de "
                f"{personaje['nombre']}."
            )

            return False

        self.raiz = self._insertar(self.raiz, personaje)

        return True

    def _insertar(self, nodo, personaje):

        if nodo is None:
            return NodoAVL(personaje)

        defensa = personaje["defensa"]

        if defensa < nodo.defensa:

            nodo.izquierdo = self._insertar(nodo.izquierdo, personaje)

        else:

            nodo.derecho = self._insertar(nodo.derecho, personaje)

        self.actualizar_altura(nodo)

        balance = self.obtener_balance(nodo)

        # Izquierda-Izquierda
        if balance > 1 and defensa < nodo.izquierdo.defensa:
            return self.rotar_derecha(nodo)

        # Derecha-Derecha
        if balance < -1 and defensa > nodo.derecho.defensa:
            return self.rotar_izquierda(nodo)

        # Izquierda-Derecha
        if balance > 1 and defensa > nodo.izquierdo.defensa:
            nodo.izquierdo = self.rotar_izquierda(nodo.izquierdo)
            return self.rotar_derecha(nodo)

        # Derecha-Izquierda
        if balance < -1 and defensa < nodo.derecho.defensa:
            nodo.derecho = self.rotar_derecha(nodo.derecho)
            return self.rotar_izquierda(nodo)

        return nodo

    def minimo(self, nodo):

        actual = nodo

        while actual.izquierdo is not None:
            actual = actual.izquierdo

        return actual

    def eliminar(self, defensa):

        if self.buscar(defensa) is None:
            return False

        self.raiz = self._eliminar(self.raiz, defensa)

        return True

    def _eliminar(self, nodo, defensa):

        if nodo is None:
            return None

        if defensa < nodo.defensa:

            nodo.izquierdo = self._eliminar(nodo.izquierdo, defensa)

        elif defensa > nodo.defensa:

            nodo.derecho = self._eliminar(nodo.derecho, defensa)

        else:

            if nodo.izquierdo is None and nodo.derecho is None:
                return None

            elif nodo.izquierdo is None:
                return nodo.derecho

            elif nodo.derecho is None:
                return nodo.izquierdo

            else:

                # Dos hijos: se reemplaza por el sucesor
                # (el menor del subárbol derecho).
                sucesor = self.minimo(nodo.derecho)

                nodo.defensa = sucesor.defensa
                nodo.personaje = sucesor.personaje

                nodo.derecho = self._eliminar(
                    nodo.derecho,
                    sucesor.defensa
                )

        self.actualizar_altura(nodo)

        balance = self.obtener_balance(nodo)

        if balance > 1 and self.obtener_balance(nodo.izquierdo) >= 0:
            return self.rotar_derecha(nodo)

        if balance > 1 and self.obtener_balance(nodo.izquierdo) < 0:
            nodo.izquierdo = self.rotar_izquierda(nodo.izquierdo)
            return self.rotar_derecha(nodo)

        if balance < -1 and self.obtener_balance(nodo.derecho) <= 0:
            return self.rotar_izquierda(nodo)

        if balance < -1 and self.obtener_balance(nodo.derecho) > 0:
            nodo.derecho = self.rotar_derecha(nodo.derecho)
            return self.rotar_izquierda(nodo)

        return nodo

    def mostrar_inorden(self):

        if self.raiz is None:

            print("El árbol AVL está vacío.")
            return

        print(f"\n{Colores.ROJO}ÁRBOL AVL (ordenado por DEFENSA){Colores.RESET}")
        print(f"{Colores.GRIS}{'-' * 75}{Colores.RESET}")

        self._mostrar_inorden(self.raiz)

    def _mostrar_inorden(self, nodo):

        if nodo is None:
            return

        self._mostrar_inorden(nodo.izquierdo)

        balance = self.obtener_balance(nodo)

        print(
            f"Defensa: {nodo.defensa:<5} | "
            f"Nombre: {nodo.personaje['nombre']:<15} | "
            f"{Colores.GRIS}Altura: {nodo.altura:<3} | "
            f"Balance: {balance}{Colores.RESET}"
        )

        self._mostrar_inorden(nodo.derecho)

    def mostrar_estructura(self):

        if self.raiz is None:

            print("El árbol AVL está vacío.")
            return

        print(f"\n{Colores.ROJO}ESTRUCTURA DEL ÁRBOL AVL{Colores.RESET}")
        print(f"{Colores.GRIS}{'-' * 75}{Colores.RESET}")

        self._mostrar_estructura(self.raiz, "", True)

    def _mostrar_estructura(self, nodo, espacio, ultimo):

        if nodo is None:
            return

        balance = self.obtener_balance(nodo)
        conector = "└── " if ultimo else "├── "

        print(
            f"{Colores.GRIS}{espacio}{conector}{Colores.RESET}"
            f"{nodo.defensa} - {nodo.personaje['nombre']} "
            f"{Colores.GRIS}(Altura: {nodo.altura}, "
            f"Balance: {balance}){Colores.RESET}"
        )

        nuevo_espacio = espacio + ("    " if ultimo else "│   ")

        hijos = []

        if nodo.izquierdo is not None:
            hijos.append(nodo.izquierdo)

        if nodo.derecho is not None:
            hijos.append(nodo.derecho)

        for i, hijo in enumerate(hijos):

            self._mostrar_estructura(
                hijo,
                nuevo_espacio,
                i == len(hijos) - 1
            )


# Lectura del archivo y utilidades del menú
def leer_json():

    try:

        with open(RUTA_JSON, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        if not isinstance(datos, list):

            print("ERROR: El JSON debe contener una lista de personajes.")
            return []

        return datos

    except FileNotFoundError:

        print(f"ERROR: No se encontró el archivo en {RUTA_JSON}.")
        return []

    except json.JSONDecodeError:

        print("ERROR: El archivo JSON no tiene un formato válido.")
        return []


def mostrar_personajes(datos):

    if not datos:

        print("No hay personajes cargados.")
        return

    print(f"\n{Colores.ROJO}PERSONAJES DEL ARCHIVO{Colores.RESET}")
    print(f"{Colores.GRIS}{'=' * 75}{Colores.RESET}")

    for item in datos:

        print(f"Nombre: {item.get('nombre', 'N/A')}")
        print(f"Ataque: {item.get('ataque', 'N/A')}")
        print(f"Defensa: {item.get('defensa', 'N/A')}")
        print(f"Poder especial: {item.get('poder_especial', 'N/A')}")

        print(f"{Colores.GRIS}{'-' * 75}{Colores.RESET}")


def menu():

    print(f"""{Colores.ROJO}
........................................
          SUPER SMASH BROS
........................................{Colores.RESET}

1. Leer archivo JSON
2. Cargar personajes en árbol rojo-negro
3. Cargar personajes en árbol AVL
4. Mostrar árbol rojo-negro
5. Mostrar árbol AVL
6. Eliminar por valor de ataque
7. Eliminar por valor de defensa
8. Salir

{Colores.ROJO}........................................{Colores.RESET}
""")


def sub_menu():

    habilitar_ansi_windows()

    datos = []

    arbol_rojo_negro = ArbolRojoNegro()
    arbol_avl = ArbolAVL()

    while True:

        limpiar_pantalla()

        menu()

        try:

            op = int(input("Ingrese una opción: "))

        except ValueError:

            print("\nDebe ingresar un número.")
            input("\nPresione ENTER para continuar...")
            continue

        if op < 1 or op > 8:

            print("\nOpción inválida.")
            input("\nPresione ENTER para continuar...")
            continue

        if op == 1:

            limpiar_pantalla()

            datos = leer_json()

            if datos:

                print(f"\nSe cargaron {len(datos)} personajes.")
                mostrar_personajes(datos)

            input("\nPresione ENTER para continuar...")

        elif op == 2:

            limpiar_pantalla()

            if not datos:

                print(
                    "Primero debe leer el archivo JSON "
                    "con la opción 1."
                )

            else:

                arbol_rojo_negro = ArbolRojoNegro()

                cantidad = 0
                repetidos = 0
                total = len(datos)

                for i, personaje in enumerate(datos, start=1):

                    if "ataque" in personaje and "nombre" in personaje:

                        insertado = arbol_rojo_negro.insertar(personaje)

                        if insertado:
                            cantidad += 1
                        else:
                            repetidos += 1

                    barra_progreso(
                        i,
                        total,
                        prefijo="Cargando árbol rojo-negro"
                    )

                    time.sleep(0.01)

                print("\nCarga del árbol rojo-negro terminada.")
                print(f"Personajes insertados: {cantidad}")
                print(f"Valores repetidos ignorados: {repetidos}")

                arbol_rojo_negro.mostrar_inorden()

            input("\nPresione ENTER para continuar...")

        elif op == 3:

            limpiar_pantalla()

            if not datos:

                print(
                    "Primero debe leer el archivo JSON "
                    "con la opción 1."
                )

            else:

                arbol_avl = ArbolAVL()

                cantidad = 0
                repetidos = 0
                total = len(datos)

                for i, personaje in enumerate(datos, start=1):

                    if "defensa" in personaje and "nombre" in personaje:

                        insertado = arbol_avl.insertar(personaje)

                        if insertado:
                            cantidad += 1
                        else:
                            repetidos += 1

                    barra_progreso(
                        i,
                        total,
                        prefijo="Cargando árbol AVL           "
                    )

                    time.sleep(0.01)

                print("\nCarga del árbol AVL terminada.")
                print(f"Personajes insertados: {cantidad}")
                print(f"Valores repetidos ignorados: {repetidos}")

                arbol_avl.mostrar_inorden()

            input("\nPresione ENTER para continuar...")

        elif op == 4:

            limpiar_pantalla()

            arbol_rojo_negro.mostrar_estructura()
            print()
            arbol_rojo_negro.mostrar_inorden()

            input("\nPresione ENTER para continuar...")

        elif op == 5:

            limpiar_pantalla()

            arbol_avl.mostrar_estructura()
            print()
            arbol_avl.mostrar_inorden()

            input("\nPresione ENTER para continuar...")

        elif op == 6:

            limpiar_pantalla()

            if arbol_rojo_negro.raiz is arbol_rojo_negro.NIL:

                print("El árbol rojo-negro está vacío.")
                print(
                    "\nPrimero cargue los personajes "
                    "con la opción 2."
                )

            else:

                try:

                    ataque = int(
                        input("Ingrese el valor de ataque a eliminar: ")
                    )

                    nodo = arbol_rojo_negro.buscar(ataque)

                    if nodo is None:

                        print(
                            f"\nNo existe ningún personaje "
                            f"con ataque {ataque}."
                        )

                    else:

                        nombre = nodo.personaje["nombre"]

                        eliminado = arbol_rojo_negro.eliminar(ataque)

                        if eliminado:

                            print(f"\nSe eliminó a {nombre}.")
                            print(f"Ataque eliminado: {ataque}")

                except ValueError:

                    print("\nDebe ingresar un número entero.")

            input("\nPresione ENTER para continuar...")

        elif op == 7:

            limpiar_pantalla()

            if arbol_avl.raiz is None:

                print("El árbol AVL está vacío.")
                print(
                    "\nPrimero cargue los personajes "
                    "con la opción 3."
                )

            else:

                try:

                    defensa = int(
                        input("Ingrese el valor de defensa a eliminar: ")
                    )

                    nodo = arbol_avl.buscar(defensa)

                    if nodo is None:

                        print(
                            f"\nNo existe ningún personaje "
                            f"con defensa {defensa}."
                        )

                    else:

                        nombre = nodo.personaje["nombre"]

                        eliminado = arbol_avl.eliminar(defensa)

                        if eliminado:

                            print(f"\nSe eliminó a {nombre}.")
                            print(f"Defensa eliminada: {defensa}")

                except ValueError:

                    print("\nDebe ingresar un número entero.")

            input("\nPresione ENTER para continuar...")

        elif op == 8:

            limpiar_pantalla()

            print(f"{Colores.ROJO}........................................{Colores.RESET}")
            print("       Programa finalizado.")
            print(f"{Colores.ROJO}........................................{Colores.RESET}")

            break


if __name__ == "__main__":
    sub_menu()
