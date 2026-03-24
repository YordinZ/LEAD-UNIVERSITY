def buscar(nombre):
    with open("data/indice.txt", "r") as ind:
        for linea in ind:
            n, pos = linea.strip().split(",")

            if n == nombre:
                pos = int(pos)

                with open("data/indexado-ejemplo.txt", "r") as datos:
                    lineas = datos.readlines()
                    print(lineas[pos])

buscar("Luis")