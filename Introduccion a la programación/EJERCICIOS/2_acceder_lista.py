'''
Indices Positivos de la lista siempre comienzan en 0
Van de izquierda a derecha
'''
#           0           1       2
frutas = ["manzana", "uva", "fresa"]
print(frutas)
print(frutas[0])
print(frutas[2])

print("--------------------------------")

#Indices negativos - derecha a izquierda
#           -3         -2       -1
frutas = ["manzana", "uva", "fresa"]
print(frutas[-3])
print(frutas[-1])

'''
Rango de indices
[2:5] -> indice 2 (incluido) y termina uno antes del indicado 5 -> [4]
'''
print("--------------------------------")
frutas = ["manzana", "fresa", "uva", "mango", "naranaja", "kiwi", "piña", "banano", "sandia", "melocoton"]
print(frutas[2:5])
print(frutas[2:3])

print("--------------------------------")
#Omitir el primer valor del rango, lo que implica que va a iniciar en 0
print(frutas[:6]) # 0 -> 5
print(frutas[-4:-1])

print("--------------------------------")
#Omitir el último valor final. Siempre toma el indice inicial y va hasta el final
print(frutas[3:])

print("--------------------------------")
#Imprime toda la lista
print(frutas[:])

print("--------------------------------")
'''
Rangos negativos
Incluye el primer elemento y llega hasta uno antes del ultimo indicado
Derecha a izquierda
'''

frutas = ["manzana", "fresa", "uva", "mango", "naranja", "kiwi", "piña", "banano", "sandia", "melocoton"]
print(frutas[-4:-1])

print("--------------------------------")
'''
Verificar si un elemento existe en la lista
'''

if "uva" in frutas:
    print("Sì, esta en las frutas")

if "carambola" in frutas:
    print("Sì, esta en las frutas")
else:
    print("No esta en las frutas")