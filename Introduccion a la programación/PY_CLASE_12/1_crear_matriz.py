#Definir la cantidad de filas y columnas
n = 3 #numero de filas -> Cantidad de listas internas
m = 2 #numero de columnas -> La cantidad de elementos de las sublista

matriz = [] #lista vacía

for i in range(n): #range (3) -> 0 1 2
    a = [0] * m
    matriz.append(a)

print(matriz)

#Número filas. Me esta dando el número de filas, o elementos de la matriz grande
print(len(matriz))

#El tamaño de las columnas, o la lista interna que seleccione dentro de los parentesis cuadrados
print(len(matriz[1]))
matriz[0][1] = 23
matriz[1][0] = 34
matriz[2][1] = 55

print(matriz)

matriz2 = [
            [2,3],
            [5, 6]
        ]

print(matriz2[1][1])

lista = [1,3,5]
lista[1] = 4
print(lista)
'''
[      0 1 
0    [0, 0], 
1    [0, 0], 
2    [0, 0]
    ]

[2][1] = 55
'''