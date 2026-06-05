#Pseudocódigo de QuickSort
# QuickSort(A, p, r)

# if p >= r:
#     return

# q = Partition(A, p, r)

# QuickSort(A, p, q - 1)
# QuickSort(A, q + 1, r)


def quick_sort(arr):

    # Caso base
    if len(arr) <= 1:
        return arr

    # Elegir pivote
    pivote = arr[len(arr) // 2]

    menores = []
    iguales = []
    mayores = []

    # Dividir elementos
    for x in arr:
        if x < pivote:
            menores.append(x)
        elif x > pivote:
            mayores.append(x)
        else:
            iguales.append(x)

    # Recursión
    return quick_sort(menores) + iguales + quick_sort(mayores)


# Ejemplo
numeros = [10, 7, 8, 9, 1, 5, 14, 21, 3, 12, 35, 47, 2, 6, 4, 11]

print("Original:", numeros)

ordenado = quick_sort(numeros)

print("Ordenado:", ordenado)