dic1 = {
    "marca": "Ford",
    "modelo": "Mustang",
    "año": 1964,
    "colores": ["rojo", "blanco", "azul"]
}

modelo = dic1["modelo"]
print(modelo)

print("\n----------------------------------------------------------------")
#get = devuelve el valro de una llave (key)
marca = dic1.get("marca")
print(marca)
print("\n----------------------------------------------------------------")
#key = devuelve una lista con todas las claves (llaves, key)
llaves = dic1.keys()
print(llaves)

print("\n----------------------------------------------------------------")
#items() = devuelve cada elemento de un diccionario como una tupla en una lista [(key, value), (key, value)]
items = dic1.items()
print(items)

print("\n----------------------------------------------------------------")
#modificar o agregar un valor que no existe podemos hacerlo por medio de las claves (llaves, key)
dic1 = {
    "marca": "Ford",
    "modelo": "Mustang",
    "año": 1964
}

dic1["color"] = "Blanco"
print(dic1)

dic1["año"] = 2025
print(dic1)

print("\n----------------------------------------------------------------")
#update = actualizar un valor de una llave, sino existe la agrega
dic1.update({"modelo": "Explorer", "color": "azul", "puertas": 5})
print(dic1)