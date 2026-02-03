dic1 = {
    "marca": "Ford",
    "modelo": "Mustang",
    "año": 1964
}
#pop() = elimina un elemento con el nombre de la clave
dic1.pop("modelo")
print(dic1)

print("\n----------------------------------------------------------------")
dic1 = {
    "marca": "Ford",
    "modelo": "Mustang",
    "año": 1964
}
#popitem() = elimina el ultimo elemento insertado en el diccionario
dic1.popitem()
print(dic1)

print("\n----------------------------------------------------------------")
dic1 = {
    "marca": "Ford",
    "modelo": "Mustang",
    "año": 1964
}

#del podemos eliminar un elmento indica con el key
del dic1["marca"]
print(dic1)

print("\n----------------------------------------------------------------")
#clear = eliminar todas las llaves:valor
dic1.clear()
print(dic1)

print("\n----------------------------------------------------------------")
#del elmina todo el diccionario incluiso de memoria
del dic1
#print(dic1)