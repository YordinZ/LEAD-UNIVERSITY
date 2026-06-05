def buscar_numero(lista, objetivo):
    for numero in lista:
        if numero == objetivo:
            return True
    return False


numeros = [4, 8, 15, 16, 23, 42]

print(buscar_numero(numeros, 4))   # Lo encuentra rápido -> mejor caso
print(buscar_numero(numeros, 42))  # Tiene que recorrer casi toda la lista -> caso promedio
print(buscar_numero(numeros, 100)) # Recorre toda la lista -> peor caso