suma = 0
contador = 0

num = int(input('Introduzca un numero: '))
while num != 0:
    suma += num # Acumular la suma
    contador += 1    
    num = int(input('Introduzca otro numero: '))

if contador > 0:
    promedio = suma / contador
    print(f"El promedio de los {contador} números es: {promedio:.2f}")
else:
    print("No se introdujeron números para calcular el promedio")