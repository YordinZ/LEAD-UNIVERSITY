# Pseudocódigo del algoritmo de ordenamiento por selección (selection sort)
# for i in range(n - 1):

#     min_index = i

#     for j in range(i + 1, n):

#         if A[j] < A[min_index]:

#             min_index = j

#     swap(A[i], A[min_index])

def selection_sort(arr):
    n = len(arr)

    for i in range(n):

        # Suponemos que el menor está en la posición actual
        min_index = i

        # Buscar el menor elemento restante
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Intercambiar el menor encontrado
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# Ejemplo
numeros = [10, 7, 8, 9, 1, 5, 14, 21, 3, 12, 35, 47, 2, 6, 4, 11]

print("Original:", numeros)

selection_sort(numeros)

print("Ordenado:", numeros)
