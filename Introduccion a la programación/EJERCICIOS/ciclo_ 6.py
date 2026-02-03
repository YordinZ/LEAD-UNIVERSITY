num1= int(input('Introduzca un I numero: '))
num2= int(input('Introduzca un II numero: '))

if num1 < num2:
    cont=num1

    while cont<= num2:
        print(f'TU NUMERO: {num1} es menor que {num2} || Número actual: {cont}')
        cont+=1

elif num2 < num1:
    cont=num2

    while cont<= num1:
        print(f'TU NUMERO: {num2} es menor que {num1} || Número actual: {cont}')
        cont+=1
else:
    print(f'Los números son iguales: {num1}')