#1. Ordenamiento burbuja
print()
print('Ordenamiento burbuja')
arr = [5, 99, 10, 88, 168, 40, 2, 3]

n = len(arr)
comparaciones = 0
intercambios = 0

for i in range(n - 1):
    for j in range(n - 1 - i):
        comparaciones += 1
        if arr[j] < arr[j + 1]:  # para ordenar de mayor a menor
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            intercambios += 1

print("Arreglo ordenado (mayor a menor):", arr)
print(f"Comparaciones: {comparaciones}")
print(f"Intercambios:  {intercambios}")


#2. Ordenamiento por selección
print()
print('Ordenamiento por seleccion')
arr = [89, 4, 23, 12, 1, 99, 50, 2, 33]

n = len(arr)
comparaciones = 0
intercambios = 0

for i in range(n - 1):
    min_idx = i
    for j in range(i + 1, n):
        comparaciones += 1
        if arr[j] < arr[min_idx]:
            min_idx = j
    if min_idx != i:
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        intercambios += 1

print("Arreglo ordenado (menor a mayor):", arr)
print(f"Comparaciones: {comparaciones}")
print(f"Intercambios:  {intercambios}")


#3. Ordenamiento por merge sort
print()
print('Ordenamiento por merge sort')
arr = [123, 10, 140, 11, 4, 2, 78, 25, 12, 70]

comparaciones = 0
intercambios  = 0   

def merge_sort(arr):
    global comparaciones, intercambios
    if len(arr) <= 1:
        return arr
    mid   = len(arr) // 2
    left  = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    global comparaciones, intercambios
    result = []
    i = j  = 0
    while i < len(left) and j < len(right):
        comparaciones += 1
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
        intercambios += 1
    for x in left[i:]:
        result.append(x); intercambios += 1
    for x in right[j:]:
        result.append(x); intercambios += 1
    return result

sorted_arr = merge_sort(arr)

print("Arreglo original:         ", arr)
print("Arreglo ordenado (HP asc):", sorted_arr)
print(f"Comparaciones: {comparaciones}")
print(f"Escrituras:    {intercambios}")

#Código de búsqueda binaria en Python
arr = [1, 2, 4, 12, 23, 33, 50, 89, 99]

buscar = 50

inicio = 0
final = len(arr) - 1

while inicio <= final:
    medio = (inicio + final) // 2

    if arr[medio] == buscar:
        print(f"Valor encontrado en la posición {medio}")
        break

    elif buscar > arr[medio]:
        inicio = medio + 1

    else:
        final = medio - 1