# Se declaran con corchetes
numeros = [1, 2, 3, 4]
print("Números", numeros)

# Se pueden acceder por medio de corchetes es inidcando el índice del elemento
# Los índices comienzan en 0
print("Primer número", numeros[0])
print("Tercer número", numeros[2])

# Append se usa para agregar un elemento al final
numeros.append(5)
print("Números: ", numeros)

#__len__()) nos dice cuantos elementos hay en la tupla
print("total de números", numeros.__len__())

# Remove se usa para eliminar un elemento de la lista
numeros.remove(5)
print("Números: ", numeros)

# Pop se usa para eliminar un elemento de la lista, puede ser por índice, por defecto remueve el último
numeros.pop()
print("Números: ", numeros)


# Pueden combinar tipos de datos
lista_combinada = [1, "Hola", 3, "Mundo", True]
print("Lista Combinada: ", lista_combinada)
