contador = 0

num = int(input('Introduzca un numero: '))
while num != 1:
    contador += 1    
    num = int(input('Introduzca otro numero: '))

print(f"Tardó {contador} pasos en llegar a 1")