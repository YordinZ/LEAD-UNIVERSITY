import time

# =========================
# Algoritmo 3
# =========================
def algoritmo3(n):

    pasos = 0
    acumulador = 0

    # Operaciones constantes
    a = 100
    b = 200
    c = a + b

    while n > 1:

        acumulador += n

        x = n * 2
        y = x - 3
        z = y / 5

        if n % 2 == 0:
            acumulador += 10
        else:
            acumulador -= 5

        n = n // 2

        pasos += 1

    return pasos + acumulador

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

medir_tiempo(algoritmo3, n)
