import os

os.makedirs("data2", exist_ok=True)

archivo = open("data2/datos.txt", "w")
archivo.write("Hola")
archivo.close()