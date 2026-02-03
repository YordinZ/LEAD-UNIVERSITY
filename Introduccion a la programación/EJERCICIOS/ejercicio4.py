num1 = float(input('Introduzca el primer numero: '))
num2 = float(input('Introduzca el segundo numero: '))
num3 = float(input('Introduzca el tercer numero: '))

if num1 >= num2 and num1 >= num3:
    print(f'El número mayor es: {num1}')
elif num2 >= num1 and num2 >= num3:
    print(f'El número mayor es: {num2}')
else:
    print(f'El número mayor es: {num3}')

'''
mayor = max(num1, num2, num3)
    print(f'El número mayor es: {mayor}')
'''