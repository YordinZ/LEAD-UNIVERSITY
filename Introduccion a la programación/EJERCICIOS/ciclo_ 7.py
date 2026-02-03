num= int(input('Ingrese un numero: '))
cont= 0
suma_pares= 0

while cont <= num:
    
    if cont % 2 == 0:
        print(f'{suma_pares} + {cont} = {suma_pares + cont}')
        suma_pares += cont
    cont+= 1
    
print(f'La suma de todos los números pares entre 0 y {num} es: {suma_pares}')