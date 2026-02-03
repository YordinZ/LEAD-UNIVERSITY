# """
# Escriba un programa que tome un numero entero positivo y calcule la suma de sus digitos.
# 1. Lea el numero entero positivo.
# 2. declarar variables para la suma de los digitos.
# 3. hacer un ciclo que recorra los digitos del numero usando la técnia de módulo 10 para obtener el dígito de las unidades e ir haciendo dvisioión entera para deshacer de los que ya fueron usados.
# 4. retornar la variable suma.

# """

def suma_digitos(numero):
    suma = 0
    while numero > 0:
        suma += numero % 10
        numero = numero // 10
    return suma

numero = int(input("Ingrese un numero entero positivo: "))
print("La suma es: ", suma_digitos(numero))





"""
Cree un programa que pida al usuario un número entero y determine si es un número primo
"""


def es_primo(numero):
    contador = numero
    cantidad_divisores = 0
    while contador > 0:
        if numero % contador == 0:
            cantidad_divisores += 1
        contador -= 1
    if cantidad_divisores > 2:
        return False
    else: 
        return True   
         
numero2 = int(input("ingrese un numero entero positivo"))
print(f"el numero{numero2} es: {es_primo(numero2)}")
