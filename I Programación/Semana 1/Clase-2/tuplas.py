# Se declaran con paréntesis
dias = ("lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo")
print("Días de la semana:", dias)

# Se pueden acceder por medio de corchetes es inidcando el índice del elemento
# Los índices comienzan en 0
print("Primer día:", dias[0])
print("Cuarto día:", dias[3])

#__len__()) nos dice cuantos elementos hay en la tupla
print("total de días", dias.__len__())

# Si se tratan de editar da error en python
#dias[1] = "Tuesday"
