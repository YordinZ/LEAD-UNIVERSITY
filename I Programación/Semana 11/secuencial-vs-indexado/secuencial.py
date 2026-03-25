def buscar(nombre):
    diccionario = {}
    with open("data/indice.txt", "r") as ind:
        for linea in ind:
            n, pos = linea.strip().split(",")
            diccionario[n] = pos

    with open("data/indexado-ejemplo.txt", "r") as datos:
        posicion = diccionario[nombre]
        lineas = datos.readlines()
        print(lineas[int(posicion)])

buscar("Luis")