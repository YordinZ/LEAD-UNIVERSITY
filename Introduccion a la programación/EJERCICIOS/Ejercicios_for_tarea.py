#Ejercicio 1
for num in range(1, 21, 2): #IMPARES
    print(num)

#Ejercicio 2    
cont= 0
lis= [2, 4, 6, 8, 10]

for num in lis:
    cont+= 1
    print(num)
print(f'El total de numeros son {cont}')

#Ejercicio 3
numeros = [5, -3, 8, 0, -2, 7] 
cont= 0

for num in numeros:
    if num > 0: #0 es neutro
        cont+= num
        print(num)
print(f'El total de numeros positivos son {cont}')

#Ejercicio 4
num= int(input('Introduzca un numero: '))

for x in range(1, 11):
    resultado= num*x
    print(f'El numero {num}*{x} = {resultado}')

#Ejercicio 5
numeros = [1, 2, 3, 4, 5] 

for x in numeros:
    mult= x*2
    print(f'{x} * 2 = {mult}')

#Ejercicio 6
numeros = [4, 7, 2, 9, 10, 15]

for x in numeros:
    if x % 2 == 0:
        print(x)

#Ejercicio 7
for x in range(1,11):
    if x == 7:
        break
    print(x)

#Ejercicio 8
numeros = [1, 3, 5, 8, 9, 11]

for x in numeros:
    if x % 2 == 0:
        break
    print(x)

#Ejercicio 9
numeros = [5, -3, 2, -1, 7, -8]
for x in numeros:
    if x < 0:
        continue
    print(x)

#Ejercicio 10
numeros = [12, 75, 150, 180, 145, 525, 50]
for num in numeros:
    if num > 500:
        break
    if num > 150:
        continue
    if num % 5 == 0:
        print(num)
        
#Ejercicio 11
numero=5
for x in range(1, numero + 1):
    print(f"{x}", x * x * x)

