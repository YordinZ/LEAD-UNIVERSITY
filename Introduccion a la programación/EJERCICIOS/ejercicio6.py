num = int(input('Introduzca un numero (entero): '))

# Programa para verificar 3 dígitos usando %
if num % 1000 >= 100 and num % 1000 <= 999:
    print(f'El número {num} tiene 3 dígitos')
else:
    print(f'El número {num} NO tiene 3 dígitos')