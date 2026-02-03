# Ejemplo Función simple
def deme_un_nombre():
    return "Naruto"

# Ejecutando y asignando una función simple
nombre = deme_un_nombre()
print(nombre)

# Ejemplo función con parámetros
def sumar(a, b):
    return a + b
# Ejecutando con parámetros
resultado = sumar(2, 4)
print("Resultado:", resultado)


# Ejemplo de una función llamando a otra función y a otro procedimiento

def procedimiento_hola():
    print("Hola soy un procedimiento")

def llamar_otros():
    procedimiento_hola()
    resultado = sumar(4, 3)
    print("Resultado:", resultado)
    return resultado + 9
    

resultado_llamar_otros = llamar_otros()
print("Resultado llamar otros:", resultado_llamar_otros)