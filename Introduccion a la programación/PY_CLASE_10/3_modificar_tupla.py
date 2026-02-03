tupla1 = ("manzana", "fresa", "uva")
#tupla1[0] = "papaya"
lista = list(tupla1)
lista[0] = "papaya"

tupla1 = tuple(lista)
print(tupla1)

print("\n----------------------------------------------------------------")
#Sobreescribir la tupla2, borra el conetnido complementa y crea uno nuevo.
tupla2 = ("manzana", "fresa", "uva")
tupla3 = ("naranja", )
tupla2 += tupla3 #tupla2 = tupla2 + tupla3
print(tupla2)

print("\n----------------------------------------------------------------")
tupla2 = ("manzana", "fresa", "uva")
tupla3 = tupla2 * 2
print(tupla3)

print("\n----------------------------------------------------------------")
#Eliminar la tupla por completo
del tupla2
#print(tupla2)