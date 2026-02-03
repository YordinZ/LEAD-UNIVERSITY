numeros = input("Introducir una lista de números separados por coma: ")
print(numeros) #Texto

print(numeros.split(",")) #-> Toma un texto y lo conviente a una lista por medio de un separador

lista_enteros = [int(x) for x in numeros.split(",")] 
print(lista_enteros)

print("--------------------------------")
nombres = input("Introducir una lista de nombres separados por coma: ")
lista_nombres = nombres.split(",")
print(lista_nombres)