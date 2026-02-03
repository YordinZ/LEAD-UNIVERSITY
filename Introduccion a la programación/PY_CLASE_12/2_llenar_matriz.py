n = 4 #numero de filas
m = 2 # numero de columnas

matriz = []
for i in range(n): # 0 1
    a = [0] * m
    matriz.append(a)

print(matriz)

for i in range (len(matriz)): #range (2) -> 0 1 -> Filas
    for j in range(len(matriz[i])):#Columnas -> Listas internas range (3) -> 0 1 2
        print(f"[f,c] [{i}][{j}]")
        matriz[i][j] = int(input("Ingrese un valor: "))

print(matriz)
print(matriz[4][1])
'''
[ c        0 1   2
f = 0    [10, 12], 
f = 1    [14, 15, 16]
        [12 13 14 13 38 29 ]
]

[f,c] [0][0]
Ingrese un valor: 10
[f,c] [0][1]
Ingrese un valor: 12
[f,c] [0][2]
Ingrese un valor: 13
[f,c] [1][0]
Ingrese un valor: 14
[f,c] [1][1]
Ingrese un valor: 15
[f,c] [1][2]
Ingrese un valor: 16
'''
