"""
Problema 1: Vigilancia del Castillo (N-Reinas)

Cada guardia ocupa una fila distinta del tablero. La posicion se
representa con una lista donde el indice es la fila y el valor
almacenado es la columna donde se ubica el guardia de esa fila.
Esto evita conflictos de fila automaticamente y solo es necesario
verificar columna y diagonales.
"""

from validaciones import solicitar_entero_positivo, confirmar


def es_posicion_segura(posiciones, fila, columna):
    """Verifica si un guardia en (fila, columna) es atacado por guardias
    ya colocados en filas anteriores (columna o diagonal).
    """
    for fila_anterior in range(fila):
        columna_anterior = posiciones[fila_anterior]

        if columna_anterior == columna:
            return False

        if abs(columna_anterior - columna) == abs(fila_anterior - fila):
            return False

    return True


def resolver_n_reinas(n, fila, posiciones, soluciones):
    """Coloca guardias fila por fila mediante Backtracking.

    Args:
        n: tamano del tablero.
        fila: fila actual a procesar.
        posiciones: lista con la columna asignada a cada fila.
        soluciones: lista acumuladora de soluciones completas.
    """
    if fila == n:
        soluciones.append(posiciones.copy())
        return

    for columna in range(n):
        if es_posicion_segura(posiciones, fila, columna):
            posiciones[fila] = columna
            resolver_n_reinas(n, fila + 1, posiciones, soluciones)
            posiciones[fila] = -1  # backtrack: deshacer la decision


def tablero_a_texto(posiciones, n):
    """Convierte una solucion en su representacion visual con Q y . """
    filas_texto = []
    for fila in range(n):
        celdas = ["Q" if posiciones[fila] == columna else "." for columna in range(n)]
        filas_texto.append(" ".join(celdas))
    return "\n".join(filas_texto)


def ejecutar_n_reinas():
    """Flujo interactivo del Problema 1."""
    print("\n=== Problema 1: Vigilancia del Castillo (N-Reinas) ===")

    continuar = True
    while continuar:
        n = solicitar_entero_positivo("Ingrese el tamano del tablero (N): ")

        posiciones = [-1] * n
        soluciones = []
        resolver_n_reinas(n, 0, posiciones, soluciones)

        if soluciones:
            print(f"\nSolucion encontrada para N = {n}:\n")
            print(tablero_a_texto(soluciones[0], n))
        else:
            print(f"\nNo existe ninguna solucion para N = {n}.")

        print(f"\nCantidad total de soluciones encontradas: {len(soluciones)}")

        continuar = confirmar("\n¿Desea resolver otro tamano de tablero?")


if __name__ == "__main__":
    ejecutar_n_reinas()
