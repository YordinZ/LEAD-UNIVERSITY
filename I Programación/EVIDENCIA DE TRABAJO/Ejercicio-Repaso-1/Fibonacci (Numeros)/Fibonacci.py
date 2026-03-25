num= int(input('Ingrese un numero entero: '))
   
if num <= 0:
    print('Valor invalido')

else:
    num1= 0
    num2= 1

    print('......Numeros Fibonacci......\n')
    for x in range(num):
        print(num1)
        num1, num2= num2, num1 + num2
