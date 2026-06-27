"""
Problema 2: Gestion de Recursos del Reino (Suma de Subconjuntos)

Para cada recurso se decide, en orden, si se incluye o no en el
subconjunto actual. La lista se ordena previamente para poder
descartar una rama completa en cuanto la suma parcial supera el
objetivo (poda).
"""

from validaciones import solicitar_lista_enteros, solicitar_entero_positivo, confirmar


def backtracking_subconjuntos(recursos, objetivo, indice, subconjunto_actual, suma_actual, soluciones):
    """Explora todos los subconjuntos posibles a partir de 'indice'.

    Args:
        recursos: lista de recursos disponibles (ordenada ascendente).
        objetivo: suma que se desea alcanzar.
        indice: posicion desde la cual se siguen evaluando recursos.
        subconjunto_actual: subconjunto que se esta construyendo.
        suma_actual: suma acumulada del subconjunto actual.
        soluciones: lista acumuladora de subconjuntos validos.
    """
    if suma_actual == objetivo:
        soluciones.append(list(subconjunto_actual))
        # No se hace return: se sigue explorando para hallar otras
        # combinaciones distintas que tambien sumen el objetivo.

    for i in range(indice, len(recursos)):
        nueva_suma = suma_actual + recursos[i]

        if nueva_suma > objetivo:
            continue  # poda: el resto de la lista solo puede aumentar la suma

        subconjunto_actual.append(recursos[i])
        backtracking_subconjuntos(recursos, objetivo, i + 1, subconjunto_actual, nueva_suma, soluciones)
        subconjunto_actual.pop()  # backtrack: deshacer la decision


def mostrar_soluciones(soluciones):
    """Imprime cada subconjunto encontrado."""
    for subconjunto in soluciones:
        print(subconjunto)


def ejecutar_subconjuntos():
    """Flujo interactivo del Problema 2."""
    print("\n=== Problema 2: Gestion de Recursos del Reino (Subconjuntos) ===")

    continuar = True
    while continuar:
        recursos = solicitar_lista_enteros(
            "Ingrese los recursos disponibles separados por espacios o comas: "
        )
        objetivo = solicitar_entero_positivo(
            "Ingrese la cantidad objetivo: ", permitir_cero=True
        )

        recursos_ordenados = sorted(recursos)
        soluciones = []
        backtracking_subconjuntos(recursos_ordenados, objetivo, 0, [], 0, soluciones)

        print()
        if soluciones:
            print("Subconjuntos encontrados:\n")
            mostrar_soluciones(soluciones)
        else:
            print("No existe ninguna solucion para la combinacion ingresada.")

        print(f"\nTotal de soluciones: {len(soluciones)}")

        continuar = confirmar("\n¿Desea probar con otra lista u otro objetivo?")


if __name__ == "__main__":
    ejecutar_subconjuntos()
