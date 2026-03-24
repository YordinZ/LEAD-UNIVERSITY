archivo = open("data/datos.txt", "r")

# el for va a leer línea por línea el archivo
for linea in archivo:
    print(linea)

archivo.close()


# si se usa with open no requiere llamar close
with open("data/hello.txt", "r") as otro:

    # el for va a leer línea por línea el archivo
    for linea in otro:
        print(linea)
