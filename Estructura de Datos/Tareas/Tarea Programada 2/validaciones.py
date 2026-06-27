"""
Modulo de validaciones de entrada.

Centraliza la lectura y validacion de datos desde teclado para que
los modulos de logica (n_reinas.py, subconjuntos.py) no repitan
codigo de manejo de errores.
"""


def solicitar_entero_positivo(mensaje, permitir_cero=False):
    """Solicita un entero al usuario, repitiendo hasta que sea valido.

    Args:
        mensaje: texto que se muestra al usuario.
        permitir_cero: si es True, acepta 0 como valor minimo valido.

    Returns:
        El entero ingresado por el usuario.
    """
    limite_inferior = 0 if permitir_cero else 1
    while True:
        entrada = input(mensaje).strip()
        try:
            valor = int(entrada)
        except ValueError:
            print("Entrada invalida. Debe ingresar un numero entero.")
            continue

        if valor < limite_inferior:
            print(f"El valor debe ser mayor o igual a {limite_inferior}.")
            continue

        return valor


def solicitar_lista_enteros(mensaje):
    """Solicita una lista de enteros separados por espacios o comas.

    Los recursos del reino se tratan como cantidades no negativas.

    Args:
        mensaje: texto que se muestra al usuario.

    Returns:
        Lista de enteros ingresados por el usuario.
    """
    while True:
        entrada = input(mensaje).strip().replace(",", " ")
        partes = entrada.split()

        if not partes:
            print("Debe ingresar al menos un numero.")
            continue

        try:
            numeros = [int(parte) for parte in partes]
        except ValueError:
            print("Entrada invalida. Use solo numeros enteros separados por espacios o comas.")
            continue

        if any(numero < 0 for numero in numeros):
            print("Los recursos deben ser cantidades no negativas.")
            continue

        return numeros


def confirmar(mensaje):
    """Solicita una respuesta si/no al usuario.

    Args:
        mensaje: pregunta que se muestra al usuario.

    Returns:
        True si la respuesta fue afirmativa, False en caso contrario.
    """
    while True:
        respuesta = input(mensaje + " (s/n): ").strip().lower()
        if respuesta in ("s", "si"):
            return True
        if respuesta in ("n", "no"):
            return False
        print("Respuesta invalida. Ingrese 's' o 'n'.")
