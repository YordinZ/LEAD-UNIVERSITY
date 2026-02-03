dic1 = {
    "marca": "Ford",
    "modelo": "Mustang",
    "año": 1964
}

for key in dic1:
    print(key) #Me devuelve la llave
    print(dic1[key]) #Me devuelve el valor

print("--------------------------------")
#.keys() -> Obtenemos las litas de keys, claves, llaves
for key in dic1.keys():
    print(key) #Me devuelve la llave
    print(dic1[key]) #Me devuelve el valor

print("--------------------------------")
#.values() -> Me muestre los valores
for valor in dic1.values():
    print(valor)

print("--------------------------------")
#items: devuelve una lista de tuplas con clave: valor [(key, value), (key, value)]
for clave, valor in dic1.items():
    print(clave, valor)