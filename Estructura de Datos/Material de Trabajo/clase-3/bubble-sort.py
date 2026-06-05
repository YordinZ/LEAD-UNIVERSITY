# Pseudocódigo del algoritmo de ordenamiento burbuja (bubble sort)
# for i in range(n - 1):

#     for j in range(n - 1 - i):

#         if A[j + 1] < A[j]:

#             swap(A[j], A[j + 1]) #swap es una función que 
#                                 #intercambia los valores de A[j] y A[j + 1]


def bubble_sort(arr):
    n = len(arr)

    # Recorre todo el arreglo
    for i in range(n - 1):

        # Últimos elementos ya están ordenados
        for j in range(n - 1 - i):

            # Intercambia si están en el orden incorrecto
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

    return arr


# Ejemplo de uso
numeros = [10, 7, 8, 9, 1, 5, 14, 21, 3, 12, 35, 47, 2, 6, 4, 11]

print("Arreglo original:")
print(numeros)

bubble_sort(numeros)

print("Arreglo ordenado:")
print(numeros)