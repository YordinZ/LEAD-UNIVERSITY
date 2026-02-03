#count() = devuelve el número de veces que aparece un valor en una tupla

tupla1 = ("naranja", "banano", "uva", "kiwi", "fresa", "banano", "pera", "papaya", "banano", "pera", "papaya")
b = tupla1.count("banano")
print(b)

print("\n================================")
#index = encontra la primera aparición del valor especificado, sino no lo encuentra genera un excepción.
b = tupla1.index("banano")
print(b)

b = tupla1.index("banano", 2)
print(b)

b = tupla1.index("banano", tupla1.index("banano") + 1)
print(b)