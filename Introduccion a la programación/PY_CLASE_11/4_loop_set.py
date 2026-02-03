'''set1 = {"manzana", "uva", "pera"}

for fruta in set1:
    print(fruta)

print("\n----------------------------------------------------------------")

if "uva" in set1:
    print("Si la uva esta en el set")'''

#EJERCICIO 6    
num= input('Introduzca una serie de numeros: ').split(',')
num= [int(n.strip()) for n in num] #Convierto en una serie de lista de Python

num_set= set(num)

maximo= max(num_set)
minimo= min(num_set)

print(f'Serie de numeros: {num_set}')
print(f'MAXIMO: {maximo}')
print(f'MINIMO: {minimo}')

#EJERCICIO 7
# Primer set
num1 = input('Introduzca la primera serie de números: ').split(',')
num1 = [int(num.strip()) for num in num1]
num_set1 = set(num1)

# Segundo set
num2 = input('Introduzca la segunda serie de números: ').split(',')
num2 = [int(num.strip()) for num in num2]
num_set2 = set(num2)

# Unión de los dos sets (puedes usar cualquiera de estas opciones)
num_set3 = num_set1.union(num_set2)  # Opción 1: usando el método union()
# num_set3 = num_set1 | num_set2     # Opción 2: usando el operador |

print(f"Primer set: {num_set1}")
print(f"Segundo set: {num_set2}")
print(f"Unión de los sets: {num_set3}")