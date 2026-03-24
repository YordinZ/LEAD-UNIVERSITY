from pathlib import Path

Path("example/input/data").mkdir(parents=True, exist_ok=True)

archivo = open("example/input/data/datos.txt", "w")
archivo.write("Nuevo archivo")
archivo.close()