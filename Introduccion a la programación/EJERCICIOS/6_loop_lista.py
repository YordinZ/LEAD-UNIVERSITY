print("--------------------------------")
#Para el while vamos a usar siempre los indices
mi_lista = ["manzana", "uva", "fresa"]
i = 0
while i < len(mi_lista):
    print(mi_lista[i])
    i = i + 1

print("--------------------------------")
'''
Bucles utilizando la comprensión de lista
Comprehension
'''

frutas = ["manzana", "uva", "fresa", "papaya", "mango", "melon"]
#[LO_DEVUELVE = FOR varible in elemento IF xxxx]
[print(x) for x in frutas] 

print("--------------------------------")
[print(x) for x in frutas if "a" in x]