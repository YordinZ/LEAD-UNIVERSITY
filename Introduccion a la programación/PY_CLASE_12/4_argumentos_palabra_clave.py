'''
Argumentos de palabra clave arbitrarias, **kwargs
No sabemos cuántos arggumentos de palabra clave se pasarán a la función
agregan: ** antes del nombre del parametro cuando se define la función

La función va a recibir un diccionario.
'''
def saludo(**personas):
    print(f"Nombre: {personas['nombre']}, Apellido: {personas['apellido']}, Edad: {personas['edad']}")

saludo(nombre="Gaudy", apellido="Monge", edad=30, lugar="Alajuela")
saludo(nombre="Daniel", apellido="Fallas", edad=14)

dic = {
    "nombre":"Gaudy",
    "apellido":"Fallas"
}

print(dic["nombre"])