# MergeSort(A, p, r)

# if p >= r:
#     return

# q = (p + r) // 2

# MergeSort(A, p, q)
# MergeSort(A, q + 1, r)

# Merge(A, p, q, r)



def merge_sort(arr):

    # Caso base
    if len(arr) <= 1:
        return arr

    # Dividir el arreglo en dos mitades
    mitad = len(arr) // 2
    izquierda = arr[:mitad]
    derecha = arr[mitad:]

    # Llamadas recursivas
    merge_sort(izquierda)
    merge_sort(derecha)

    i = 0  # índice izquierda
    j = 0  # índice derecha
    k = 0  # índice arreglo principal

    # Mezclar las dos mitades ordenadas
    while i < len(izquierda) and j < len(derecha):

        if izquierda[i] < derecha[j]:
            arr[k] = izquierda[i]
            i += 1
        else:
            arr[k] = derecha[j]
            j += 1

        k += 1

    # Copiar elementos restantes
    while i < len(izquierda):
        arr[k] = izquierda[i]
        i += 1
        k += 1

    while j < len(derecha):
        arr[k] = derecha[j]
        j += 1
        k += 1

    return arr


# Ejemplo
numeros = [10, 7, 8, 9, 1, 5, 14, 21, 3, 12, 35, 47, 2, 6, 4, 11]

print("Original:", numeros)

merge_sort(numeros)

print("Ordenado:", numeros)