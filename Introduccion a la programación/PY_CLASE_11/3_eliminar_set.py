#remove -> elimina un elemento, pero si no existe, genera un error. 
set1 = {"manzana", "uva", "pera"}
set1.remove("uva")
print(set1)

print("\n----------------------------------------------------------------")
#discard() -> elimina un elemento, pero si no existe, NO genera un error. 
set1 = {"manzana", "uva", "pera", "fresa"}
set1.discard("uva")
set1.discard("kiwi")
print(set1)

print("\n----------------------------------------------------------------")
#pop = elimina un elemento, no se sabe cuál elemento, y retorna el elemento que elimina
set1 = {"manzana", "uva", "pera", "fresa"}
print(set1)
fruta = set1.pop()
print(set1)
print(fruta)
print("\n----------------------------------------------------------------")
#clear limpia el conjunto (set)
set1 = {"manzana", "uva", "pera", "fresa"}
set1.clear()
print(set1)

print("\n----------------------------------------------------------------")
#del elmina todo el set incluiso de memoria
del set1
#print(set1)