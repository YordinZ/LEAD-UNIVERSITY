num = int(input('Ingrese un numero entero positivo: '))

if num <= 0:
    print("El número debe ser un entero positivo.")
else:
    suma_divisores = 0
    i=1 
    while i <= num // 2:
        if num % i == 0:
            suma_divisores += i
        i += 1

    # Comparamos la suma con el número original
    if suma_divisores == num:
        print(f"¡El número {num} es un número perfecto!")
    else:
        print(f"El número {num} no es un número perfecto.")