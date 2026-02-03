num = input('Ingrese I serie de numeros: ').split(',')
num2 = input('Ingrese II serie de numeros: ').split(',')

num = [int(i) for i in num] #Paso de texto a numero
num2 = [int(i) for i in num2]

numeros_repetidos = [] #Almacena numeros que se repitan
for x in num:
    if x in num2 and x not in numeros_repetidos:
        numeros_repetidos.append(x) # Agrega elementos a la lista

if numeros_repetidos:
    print('Números que se repiten en ambas series:', numeros_repetidos)
else:
    print('No hay números repetidos')

"""
numeros = [int(input(f"Número {i+1}: ")) for i in range(10)]
t_numeros=tuple(numeros)
buscar = int(input("Número a buscar: "))

if buscar in t_numeros:
    print(f"Está en la posición {t_numeros.index(buscar)}")
else:
    print("No está en la lista.")
"""