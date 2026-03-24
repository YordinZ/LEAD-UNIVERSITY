import json

with open("data/datos.json", "r") as f:
    datos = json.load(f)

print(datos)
print(datos["nombre"])


with open("output/datos2.json", "w") as f:
   json.dump({"nombre": "carlos", "edad": 30}, f)
