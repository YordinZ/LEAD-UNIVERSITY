num= int(input('Introduzca un numero: '))
numeros= []

while num != 0:  
    numeros.append(num)
    num= int(input('Introduzca otro numero: '))

print("Números introducidos (sin el 0 final):", numeros)

