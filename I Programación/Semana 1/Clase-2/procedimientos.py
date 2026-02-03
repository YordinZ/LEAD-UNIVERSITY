# Ejemplo procedimiento simple
def imprimir_hola():
    print("Hola Mundo")

# Ejecutando al procedimiento simple
imprimir_hola()

# Ejemplo procedimiento con un parámetro
def imprimir_hola_nombre(nombre):
    print("Hola ", nombre)


# Ejecutando con parámetros
imprimir_hola_nombre("Mundo")

# Ejemplo de un procedimiento llamando a otro
def llamar_otros():
    print("Voy a llamar a otros procedimientos")
    imprimir_hola_nombre("otro")
    imprimir_hola()

llamar_otros()

# Si se trata de asignar un procedimiento a una variable se obtiene un atributo de tipo None
llamar_otros_resultado = llamar_otros()
print(llamar_otros_resultado, type(llamar_otros_resultado))