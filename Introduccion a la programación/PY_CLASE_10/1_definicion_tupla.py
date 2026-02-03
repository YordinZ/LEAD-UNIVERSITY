'''
- Permiten duplicados
- Es ordenada (indices)
- Inmutable (No se puede cambiar o alterar)
- ()
- El primer indice siempre es 0 [0]
'''

tupla = ("manzana", "mango", "uva", "pera")
print(tupla)
print(len(tupla))

print("\n================================")
# Para crear una tupla con un solo elemento, debe agregar una coma al final del elemento.
#sino se coloca la coma, entonces Python lo interpreta como un string y no como tupla
tupla1 = ("manzana",)
print(tupla1)

print("\n================================")
#Permite elementos distinos
tupla = ("abc", 1, 1.3, True)
print(tupla)