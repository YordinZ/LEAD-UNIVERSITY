import time


# =========================
# Algoritmo 2
# =========================
def algoritmo2(n):

    total = 0
    suma_pares = 0
    suma_impares = 0

    # Operaciones constantes
    a = 10
    b = 20
    c = a + b

    for i in range(n):

        total += i

        if i % 2 == 0:
            suma_pares += i
        else:
            suma_impares += i

        x = i * 2
        y = x + 5
        z = y / 2

    promedio = total / n

    return promedio + suma_pares + suma_impares


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

medir_tiempo(algoritmo2, n)

