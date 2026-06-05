# Hash Table sencilla con función hash personalizada

TAMANO_TABLA = 10

# Tabla hash
tabla = [None] * TAMANO_TABLA


def funcion_hash(nombre):
    """
    Suma los códigos ASCII de cada letra
    y calcula la posición dentro de la tabla.
    """
    suma = 0

    for letra in nombre:
        suma += ord(letra)

    return suma % TAMANO_TABLA


def insertar(nombre):
    posicion = funcion_hash(nombre)
    tabla[posicion] = nombre


def buscar(nombre):
    posicion = funcion_hash(nombre)

    if tabla[posicion] == nombre:
        return True

    return False


# Insertar datos
insertar("Ana")
insertar("Juan")
insertar("Pedro")

print(tabla)

# Buscar elemento
nombre = input("Nombre a buscar: ")

if buscar(nombre):
    print("Elemento encontrado")
else:
    print("Elemento no encontrado")

