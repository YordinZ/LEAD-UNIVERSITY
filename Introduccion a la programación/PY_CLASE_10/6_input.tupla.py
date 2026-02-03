texto = input("Ingrese un texto: ")
tupla = tuple(texto)
print(tupla)

print("\n================================")
texto = input("ingrese una serie de números separados por coma: ")

lista = texto.split(",")
tupla_numero = tuple(int(i)  for i in texto.split(","))
print(tupla_numero)