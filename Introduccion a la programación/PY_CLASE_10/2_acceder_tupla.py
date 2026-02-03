tupla1 = ("naranja", "mango", "uva", "kiwi", "fresa", "mango", "pera", "papaya")
print(tupla1[0])
print(tupla1[1])
print(tupla1[3])

print("\n================================")
print(tupla1[-1])

print("\n================================")
#Rango de indices [2:5] es el 2 incluido y el 5 no se considera
print(tupla1[2:5])

print("\n================================")
#Indice 0 hasta el 4 (sin incluir)
print(tupla1[:4])

print("\n================================")
#Indice 5 hasta el último elemento
print(tupla1[5:])

print("\n================================")
#Indice -4 hasta el -1 (sin incluirlo)
print(tupla1[-4:-1])