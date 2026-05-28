import time


# =========================
# Algoritmo 1
# =========================
def algoritmo1(n):

    contador = 0
    suma = 0

    # Operaciones constantes
    a = 5
    b = 7
    c = a * b

    for i in range(n):

        for j in range(n):

            contador += 1

            suma += i + j

            x = i * j
            y = x + 100
            z = y / 3

            if x % 2 == 0:
                suma += 1
            else:
                suma -= 1

    promedio = suma / (n * n)

    return contador + promedio



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

medir_tiempo(algoritmo1, n)




