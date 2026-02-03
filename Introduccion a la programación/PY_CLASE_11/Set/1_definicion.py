'''
colección ordenada * (key: value), modificar, y no admite duplicados en el key(llave, clave) 
'''

dic1 = {
    "marca": "Ford",
    "modelo": "Mustang",
    "año": 1964
}

print(dic1)
print(dic1["marca"])
print(len(dic1))

print("\n----------------------------------------------------------------")
#No admite duplicados en las llaves (key)
dic1 = {
    "marca": "Ford",
    "modelo": "Mustang",
    "año": 1964,
    "año": 2025
}
print(dic1)
print("\n----------------------------------------------------------------")
dic1 = {
    "marca": "Ford",
    "modelo": "Mustang",
    "año": 1964,
    "año_1": 1964
}
print(dic1)

print("\n----------------------------------------------------------------")
#Los diccionarios pueden tener cualquier tipo de dato:
dic1 = {
    "marca": "Ford",
    "modelo": "Mustang",
    "año": 1964, 
    "colores": ["rojo", "blanco", "azul"]
}
print(dic1["colores"])
print(dic1["colores"][1])

dic1["colores"][1] = "verde"
print(dic1["colores"])