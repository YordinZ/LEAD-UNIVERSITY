# def palindromo(texto):
#     texto= texto.lower()
#     return texto == texto [::-1]

# palabra= input('Ingrese una palabra: ')

# if palindromo(palabra):
#     print('Es un palindromo')

# else:
#     print('No es un palindromo')

#OTRA FORMA DE HACERLO
texto= input('Ingrese una palabra: ').lower()

palindromo= True
distancia= len(texto)

for x in range(distancia // 2):
    if texto[x] != texto[distancia - 1 - x]:
        palindromo = False
        break

if palindromo:
    print('Es un palindromo')

else:
    print('No es un palindromo')