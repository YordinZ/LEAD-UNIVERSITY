num = int(input('Introduzca un numero (entero): '))

if num == 0:
    print(f'El número {num} es CERO')
    
elif (num % 2 == 0 or num % 2 == 1) and num >= 0:
    print(f'El número {num} es POSITIVO')
else:
    print(f'El número {num} es NEGATIVO')
