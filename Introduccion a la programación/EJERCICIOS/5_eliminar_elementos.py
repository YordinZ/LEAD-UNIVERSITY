'''
DEL
'''
frutas = ["manzana", "fresa", "uva"]
del frutas[2]
print(frutas)

print("\n================================")
frutas = ["manzana", "uva", "fresa", "papaya", "mango", "melon"]
del frutas[1:4]
print(frutas)

print("\n================================")
frutas = ["manzana", "uva", "fresa", "papaya", "mango", "melon"]
del frutas
#print(frutas)

'''
.clear : limpiar la lista, pero no la elimina
'''
frutas = ["manzana", "uva", "fresa", "papaya", "mango", "melon"]
frutas.clear()
print(frutas)



'''
.remove(): elemina un elemento especifico
'''
frutas = ["manzana", "fresa", "uva"]
frutas.remove("uva")
print(frutas)

print("\n================================")

'''
.pop(): Eliminar un elemento de un indice especifico
-> Si no le indico el indice remueve el último.
Además devuelve el elemento
'''
frutas = ["manzana", "fresa", "uva"]
elemento = frutas.pop(1)
print(elemento)
print(frutas)

frutas = ["manzana", "fresa", "uva"]
frutas.pop()
print(frutas)