import math

def jump_search(lista, valor):
    n = len(lista)

    # Tamaño óptimo del salto
    salto = int(math.sqrt(n))

    # Encontrar el bloque donde podría estar el valor
    inicio = 0
    fin = salto

    while inicio < n and lista[min(fin, n) - 1] < valor:
        inicio = fin
        fin += salto

        if inicio >= n:
            return -1

    # Búsqueda lineal dentro del bloque
    while inicio < min(fin, n):
        if lista[inicio] == valor:
            return inicio
        inicio += 1

    return -1


# Ejemplo de uso
numeros = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]

posicion = jump_search(numeros, 15)

if posicion != -1:
    print(f"Elemento encontrado en la posición {posicion}")
else:
    print("Elemento no encontrado")