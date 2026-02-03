num1 = int(input('Introduzca el primer numero (entero): '))
num2 = int(input('Introduzca el segundo numero: (entero)'))

# Verificar si el divisor es cero
if num2 == 0:
    print("¡ERROR! No se puede dividir entre cero.")
else:
    # Realizar la división
    resultado = num1 / num2
    print(f'El resultado de {num1} ÷ {num2} = {resultado}')