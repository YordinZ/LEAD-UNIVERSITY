# solucion simple
numeros = [5, 2, 8, 1]

ordenados = sorted(numeros)

print(ordenados)


#solucion manual
numeros = [5, 2, 8, 1]

for i in range(len(numeros)):
    for j in range(len(numeros) - 1):
        if numeros[j] > numeros[j + 1]:
            temp = numeros[j]
            numeros[j] = numeros[j + 1]
            numeros[j + 1] = temp

print(numeros)