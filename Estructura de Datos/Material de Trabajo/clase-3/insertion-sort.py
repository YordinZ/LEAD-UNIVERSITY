# Pseudocódigo del algoritmo de ordenamiento por inserción (insertion sort)
# for i in range(1, n):

#     v = A[i]
#     j = i - 1

#     while j >= 0 and A[j] > v:

#         A[j + 1] = A[j]
#         j = j - 1

#     A[j + 1] = v


def insertion_sort(arr):

    # Empezamos desde el segundo elemento
    for i in range(1, len(arr)):

        actual = arr[i]
        j = i - 1

        # Mover elementos mayores una posición adelante
        while j >= 0 and arr[j] > actual:
            arr[j + 1] = arr[j]
            j -= 1

        # Insertar el elemento en su posición correcta
        arr[j + 1] = actual

    return arr


# Ejemplo
numeros = [10, 7, 8, 9, 1, 5, 14, 21, 3, 12, 35, 47, 2, 6, 4, 11]

print("Original:", numeros)

insertion_sort(numeros)

print("Ordenado:", numeros)