import time


# =========================
# Algoritmo 4
# =========================
def algoritmo4(n):

    # Operaciones constantes
    a = 1
    b = 2
    c = a + b

    if n <= 1:
        return n

    x = n * 2
    y = x + 10
    z = y / 2

    return algoritmo4(n - 1) + algoritmo4(n - 2)


# =========================
# Medición de tiempo
# =========================
def medir_tiempo(funcion, n):

    inicio = time.perf_counter()

    resultado = funcion(n)

    fin = time.perf_counter()

    tiempo = fin - inicio

    print(f"\n{funcion.__name__}")
    print(f"n = {n}")
    print(f"Resultado = {resultado}")
    print(f"Tiempo = {tiempo:.8f} segundos")


# =========================
# Programa principal
# =========================

n = int(input("Ingrese el valor de n: "))

medir_tiempo(algoritmo4, n)
