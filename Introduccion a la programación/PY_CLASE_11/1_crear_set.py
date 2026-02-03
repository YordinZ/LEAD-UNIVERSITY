'''
- Pueden almacenar valores de distintos tipos (int, str, bool, float)
- Colección desordenada, no tiene indices. No tiene [0]
- Los elementos no se pueden modificar, pero si se pueden eliminar y agregar nuevos elementos.
- NO PERMITEN VALORES DUPLICADOS

Tupla= ()
List= []
set= () {} random, elemento desordenados
diccionario= {}
'''

set1 = {"manzana", "pera", "uva"}
print(set1)

print("\n----------------------------------------------------------------")
set1 = {"manzana", "pera", "uva", "uva", "uva", "manzana", "piña"}
print(set1)
print(len(set1))

print("\n----------------------------------------------------------------")
set1 = {"manzana", 123, 3.0, True}
print(set1)

print("\n----------------------------------------------------------------")
set1 = set(("manzana", "kiwi", "fresa"))
print(set1)