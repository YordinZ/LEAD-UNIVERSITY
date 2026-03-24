import json

datos = []
# 1. Lectura de archivo en formato JSON
with open("data/personas.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

print("Datos originales: ", datos)

# 2. Agregar una nueva persona
nueva_persona = {
    "nombre": "Oscar",
    "edad": 19
}

datos.append(nueva_persona)
datos[1]["edad"] = 26 # Modificar un elemento

# 3. Sobrescribir el archivo con los datos modificados
with open("data/personas.json", "w", encoding="utf-8") as archivo:
    json.dump(datos, archivo, indent=4, ensure_ascii=False)

print("Archivo actualizado correctamente")