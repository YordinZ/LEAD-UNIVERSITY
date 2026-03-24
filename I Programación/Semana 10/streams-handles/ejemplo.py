archivo = open("data/datos.txt", "r")   # handle

linea = archivo.readline()         # usa stream

print(linea)

archivo.close()                    # cerrar stream
