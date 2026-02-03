texto = input("ingresar valores separados por coma: ")
numero = {int(x) for x in texto.split(",")}
print(numero)