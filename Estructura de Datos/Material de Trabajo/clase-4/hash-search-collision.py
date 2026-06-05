TAMANO_TABLA = 10

tabla = [[] for _ in range(TAMANO_TABLA)]


def funcion_hash(nombre):
    suma = 0

    for letra in nombre:
        suma += ord(letra)

    return suma % TAMANO_TABLA


def insertar(nombre, nota):
    posicion = funcion_hash(nombre)

    # Revisar si el estudiante ya existe
    for estudiante in tabla[posicion]:
        if estudiante[0] == nombre:
            estudiante[1] = nota
            return

    # Si no existe, se agrega a la lista
    tabla[posicion].append([nombre, nota])


def buscar(nombre):
    posicion = funcion_hash(nombre)

    for estudiante in tabla[posicion]:
        if estudiante[0] == nombre:
            return estudiante[1]

    return None


def mostrar_tabla():
    for i, posicion in enumerate(tabla):
        print(f"Posición {i}: {posicion}")


insertar("Ana", 95)
insertar("Naa", 88)   # Genera colisión con Ana
insertar("Juan", 90)
insertar("Pedro", 85)

mostrar_tabla()

nombre = input("Nombre a buscar: ")

resultado = buscar(nombre)

if resultado is not None:
    print(f"{nombre} encontrado. Nota: {resultado}")
else:
    print(f"{nombre} no encontrado.")