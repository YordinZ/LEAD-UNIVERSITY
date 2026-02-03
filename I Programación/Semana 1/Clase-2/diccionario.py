# Se definen con llaves {}
persona = {
    "nombre": "Carlos",
    "edad": 30,
    "usuario": True
}

print("persona: ", persona) 

# Sus valores se pueden acceder con ["nombre de la llave/clave"]
print(persona["nombre"])

# se pueden agregar nuevos valores con ["nombre de la llave/clave"] = nuevo valor
persona["ciudad"] = "San José"
print("persona: ", persona) 

# se pueden modificar valores con ["nombre de la llave/clave"] = nuevo valor
persona["edad"] = 35
print("persona: ", persona) 



# Se pueden anidar un diccionario dentro de otro
persona_aumentada = {
    "nombre": "Andrés",
    "edad": 25,
    "usuario": True,
    "direccion": {
        "pais": "Costa Rica",
        "provincia": "Alajuela",
        "canton": "Alajuela",
        "distrito": "San Antonio"

    }
}

print("Persona: ", persona_aumentada)

# Para acceder un atributo anidado se usa doble []
print("Provicincia: ", persona_aumentada["direccion"]["provincia"])