import csv

datos = []

with open("data/personas.csv", "r", newline="", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)

    for fila in lector:
        if fila[0] == "Luis":
            fila[2] = "1000"
        datos.append(fila)

with open("data/personas.csv", "w", newline="", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerows(datos)

print("Archivo modificado")