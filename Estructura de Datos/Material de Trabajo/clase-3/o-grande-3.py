def heapify(arr, n, i):
    mayor = i
    izquierda = 2 * i + 1
    derecha = 2 * i + 2

    # Verificar hijo izquierdo
    if izquierda < n and arr[izquierda] > arr[mayor]:
        mayor = izquierda
    # Verificar hijo derecho
    if derecha < n and arr[derecha] > arr[mayor]:
        mayor = derecha
    # Si el mayor no es la raíz
    if mayor != i:
        arr[i], arr[mayor] = arr[mayor], arr[i]

        # Aplicar heapify recursivamente
        heapify(arr, n, mayor)


def heap_sort(arr):
    n = len(arr)
    # Construir el max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # Extraer elementos uno por uno
    for i in range(n - 1, 0, -1):
        # Mover la raíz al final
        arr[i], arr[0] = arr[0], arr[i]

        # Reorganizar el heap
        heapify(arr, i, 0)


numeros = [12, 11, 13, 5, 6, 7]

print("Lista original:")
print(numeros)

heap_sort(numeros)

print("Lista ordenada:")
print(numeros)