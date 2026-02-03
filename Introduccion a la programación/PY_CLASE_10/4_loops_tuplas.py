tupla1 = ("naranja", "mango", "uva", "kiwi", "fresa", "banano", "pera", "papaya")

for fruta in tupla1:
    print(fruta)

print("\n================================")
print(len(tupla1))

for i in range(len(tupla1)): #range(8) -> 0 1 2 3 4 5 6 7
    print(tupla1[i])

print("\n================================")
i = 0
while i < len(tupla1):
    print(tupla1[i])
    i+=1

print("\n================================")
tupla1 = ("naranja", "mango", "uva", "kiwi", "fresa", "banano", "pera", "papaya")

#LO DEVUELVE FOR X IN _____ CONDICION
tupla_frutas_a = tuple(fruta for fruta in tupla1 if "a" in fruta)
print(tupla_frutas_a)