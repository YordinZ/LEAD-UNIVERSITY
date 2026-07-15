import json
import heapq
import os
import sys


#  RUTAS BASE DEL PROYECTO
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")


#  COLORES ANSI
class Color:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"

    NARANJA = "\033[38;5;166m"      
    NARANJA_CLARO = "\033[38;5;208m"
    BLANCO = "\033[97m"
    GRIS = "\033[38;5;245m"
    VERDE = "\033[38;5;71m"
    ROJO = "\033[38;5;160m"
    AZUL = "\033[38;5;110m"
    AMARILLO = "\033[38;5;179m"


def titulo(texto):
    ancho = max(60, len(texto) + 4)
    linea = "═" * ancho
    print(f"\n{Color.NARANJA}{Color.BOLD}{linea}{Color.RESET}")
    print(f"{Color.NARANJA}{Color.BOLD}  {texto}{Color.RESET}")
    print(f"{Color.NARANJA}{Color.BOLD}{linea}{Color.RESET}\n")


def subtitulo(texto):
    print(f"\n{Color.NARANJA_CLARO}{Color.BOLD}▶ {texto}{Color.RESET}")
    print(f"{Color.GRIS}{'-' * (len(texto) + 2)}{Color.RESET}")


def info(etiqueta, valor, color_valor=Color.BLANCO):
    print(f"  {Color.GRIS}{etiqueta}:{Color.RESET} {color_valor}{valor}{Color.RESET}")


def ok(texto):
    print(f"{Color.VERDE}✔ {texto}{Color.RESET}")


def error(texto):
    print(f"{Color.ROJO}✘ {texto}{Color.RESET}")


#  CARGA Y VALIDACION DEL GRAFO
def buscar_grafo_json(nombre_archivo="grafo.json"):
    directorio_script = os.path.dirname(os.path.abspath(__file__))
    directorio_padre = os.path.dirname(directorio_script)

    candidatos = [
        os.path.join(DATA_DIR, nombre_archivo),
        os.path.join(directorio_script, "data", nombre_archivo),
        os.path.join(directorio_script, nombre_archivo),
        os.path.join(directorio_padre, "data", nombre_archivo),
        os.path.join(os.getcwd(), nombre_archivo),
    ]

    # Eliminar duplicados manteniendo el orden
    vistos = set()
    candidatos_unicos = []
    for c in candidatos:
        if c not in vistos:
            vistos.add(c)
            candidatos_unicos.append(c)

    for candidato in candidatos_unicos:
        if os.path.isfile(candidato):
            return candidato, candidatos_unicos

    return None, candidatos_unicos


def cargar_grafo(ruta_json):

    if not os.path.isfile(ruta_json):
        raise FileNotFoundError(
            f"No se encontro el archivo JSON: {ruta_json}\n\n"
            f"  Diagnostico de rutas:\n"
            f"    BASE_DIR (raiz del proyecto) : {BASE_DIR}\n"
            f"    DATA_DIR (carpeta esperada)  : {DATA_DIR}\n\n"
            f"  Verifique que:\n"
            f"    1. 'main.py' este dentro de una carpeta 'scripts/' \n"
            f"       (BASE_DIR sube DOS niveles desde main.py).\n"
            f"    2. Exista la carpeta 'data/' al mismo nivel que 'scripts/'.\n"
            f"    3. El archivo se llame exactamente 'grafo.json' dentro de 'data/'."
        )

    with open(ruta_json, "r", encoding="utf-8") as f:
        try:
            datos = json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"El archivo JSON no es valido: {e}")

    # Validacion basica de estructura
    campos_requeridos = ["vertices", "aristas"]
    for campo in campos_requeridos:
        if campo not in datos:
            raise ValueError(f"El JSON no contiene el campo requerido: '{campo}'")

    vertices = datos["vertices"]
    aristas = datos["aristas"]

    if not isinstance(vertices, list) or len(vertices) == 0:
        raise ValueError("El campo 'vertices' debe ser una lista no vacia.")
    if not isinstance(aristas, list):
        raise ValueError("El campo 'aristas' debe ser una lista.")

    vertices_set = set(vertices)
    grafo = {v: [] for v in vertices}

    for i, arista in enumerate(aristas):
        for campo in ("origen", "destino", "peso"):
            if campo not in arista:
                raise ValueError(f"La arista en posicion {i} no contiene el campo '{campo}'.")

        origen = arista["origen"]
        destino = arista["destino"]
        peso = arista["peso"]

        if origen not in vertices_set or destino not in vertices_set:
            raise ValueError(
                f"La arista {origen} -> {destino} referencia un vertice no declarado."
            )
        if not isinstance(peso, (int, float)) or peso < 0:
            raise ValueError(f"Peso invalido en la arista {origen} -> {destino}: {peso}")

        grafo[origen].append((destino, peso))

    return grafo, vertices, datos.get("nombre", "Grafo"), datos.get("dirigido", True)


#  PROBLEMA 1: 
def dijkstra(grafo, origen):
    distancias = {v: float("inf") for v in grafo}
    previos = {v: None for v in grafo}
    distancias[origen] = 0

    visitados = set()
    cola = [(0, origen)]

    while cola:
        dist_actual, actual = heapq.heappop(cola)

        if actual in visitados:
            continue
        visitados.add(actual)

        for vecino, peso in grafo[actual]:
            nueva_dist = dist_actual + peso
            if nueva_dist < distancias[vecino]:
                distancias[vecino] = nueva_dist
                previos[vecino] = actual
                heapq.heappush(cola, (nueva_dist, vecino))

    return distancias, previos


def reconstruir_camino(previos, origen, destino):
   
    if previos[destino] is None and destino != origen:
        return None  # no alcanzable

    camino = []
    actual = destino
    while actual is not None:
        camino.append(actual)
        actual = previos[actual]
    camino.reverse()

    if camino[0] != origen:
        return None
    return camino


def mostrar_resultados_dijkstra(grafo, origen, distancias, previos):
    subtitulo(f"Resultados de Dijkstra desde '{origen}'")

    # Ordenar por distancia para lectura clara
    destinos = sorted(
        (v for v in grafo if v != origen),
        key=lambda v: (distancias[v] == float("inf"), distancias[v])
    )

    for destino in destinos:
        dist = distancias[destino]
        if dist == float("inf"):
            error(f"{destino:<15} -> NO ALCANZABLE desde {origen}")
        else:
            camino = reconstruir_camino(previos, origen, destino)
            camino_str = f"{Color.NARANJA} -> {Color.RESET}".join(camino)
            print(
                f"  {Color.AZUL}{destino:<15}{Color.RESET} "
                f"{Color.GRIS}distancia:{Color.RESET} {Color.AMARILLO}{dist:<5}{Color.RESET} "
                f"{Color.GRIS}camino:{Color.RESET} {camino_str}"
            )


#  PROBLEMA 2:
def tsp_backtracking(grafo, origen):
    vertices = list(grafo.keys())
    n = len(vertices)

    mejor = {"ruta": None, "costo": float("inf")}

    def backtrack(actual, visitados, ruta, costo_acumulado):
        # Poda: si ya superamos el mejor costo conocido, no seguir
        if costo_acumulado >= mejor["costo"]:
            return

        if len(visitados) == n:
            # Intentar cerrar el ciclo regresando al origen
            for vecino, peso in grafo[actual]:
                if vecino == origen:
                    costo_total = costo_acumulado + peso
                    if costo_total < mejor["costo"]:
                        mejor["costo"] = costo_total
                        mejor["ruta"] = ruta + [origen]
            return

        for vecino, peso in grafo[actual]:
            if vecino not in visitados:
                visitados.add(vecino)
                ruta.append(vecino)
                backtrack(vecino, visitados, ruta, costo_acumulado + peso)
                ruta.pop()
                visitados.remove(vecino)

    backtrack(origen, {origen}, [origen], 0)
    return mejor["ruta"], mejor["costo"]


def mostrar_resultados_tsp(ruta, costo, origen):
    subtitulo(f"Resultado del Problema del Viajero (TSP) desde '{origen}'")

    if ruta is None:
        error("No existe una ruta que visite todos los paises exactamente una vez "
              "y regrese al origen (no hay ciclo hamiltoniano en este grafo dirigido).")
        return

    ruta_str = f" {Color.NARANJA}→{Color.RESET} ".join(
        f"{Color.AZUL}{p}{Color.RESET}" for p in ruta
    )
    print(f"  {ruta_str}\n")
    info("Paises visitados", len(ruta) - 1, Color.BLANCO)
    info("Costo total de la ruta", costo, Color.AMARILLO)


#  PROGRAMA PRINCIPAL
def main():
    origen = "Japón"

    titulo("AGENCIA DE SEGURIDAD DEL REINO - LA CONQUISTA MUNDIAL DE M. BISON")

    if len(sys.argv) > 1:
        ruta_json = sys.argv[1]
    else:
        ruta_json, candidatos = buscar_grafo_json()
        if ruta_json is None:
            error("No se encontro 'grafo.json' en ninguna de estas ubicaciones:")
            for c in candidatos:
                print(f"    {Color.GRIS}- {c}{Color.RESET}")
            print(
                f"\n  {Color.GRIS}Solucion: coloque 'grafo.json' en alguna de las rutas de arriba, "
                f"o ejecute:{Color.RESET}\n"
                f"    {Color.AMARILLO}python main.py \"ruta\\a\\grafo.json\"{Color.RESET}"
            )
            sys.exit(1)
        ok(f"grafo.json localizado en: {ruta_json}")

    try:
        grafo, vertices, nombre, dirigido = cargar_grafo(ruta_json)
    except (FileNotFoundError, ValueError) as e:
        error(f"Error al cargar el grafo: {e}")
        sys.exit(1)

    ok(f"Grafo '{nombre}' cargado correctamente.")
    info("Vertices", len(vertices))
    info("Dirigido", dirigido)

    if origen not in grafo:
        error(f"El vertice de origen '{origen}' no existe en el grafo.")
        sys.exit(1)

    # ---------------- Problema 1: Dijkstra ----------------
    titulo("PROBLEMA 1: CAMINO MAS CORTO (DIJKSTRA)")
    distancias, previos = dijkstra(grafo, origen)
    mostrar_resultados_dijkstra(grafo, origen, distancias, previos)

    # ---------------- Problema 2: TSP ----------------
    titulo("PROBLEMA 2: RUTA OPTIMA (PROBLEMA DEL VIAJERO)")
    ruta, costo = tsp_backtracking(grafo, origen)
    mostrar_resultados_tsp(ruta, costo, origen)

    print(f"\n{Color.NARANJA}{Color.BOLD}{'═' * 60}{Color.RESET}\n")


if __name__ == "__main__":
    main()