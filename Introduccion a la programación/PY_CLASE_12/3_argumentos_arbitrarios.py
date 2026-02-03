'''
Argumentos de palabra clave
argumentos se pueden enviar como clave = valor (parametro = valor)
De esta manera no importa como pases yo los valores.
'''

def saludo_estudiantes(estudiante1, estudiante2, estudiante3):
    print(f"Hola Estudiante 1: {estudiante1}")
    print(f"Hola Estudiante 2: {estudiante2}")
    print(f"Hola Estudiante 3: {estudiante3}")

saludo_estudiantes ("Facundo", "Kendall", "Fiorella")
print("---------------------------------------")

saludo_estudiantes(estudiante3="Sebastian", estudiante1="Yordin", estudiante2="Daniel")
'''
Argumentos arbitrarios, *args
Si no sabemos cuántos argumentos se pasarán a la función.
Se agrega un * antes del nombre del parámetro cuando se define la función. 

De esta manera la función puede recibir una TUPLA de argumentos
'''

def saludo(*nombres):
     for n in nombres:
          print(f"Hola {n}")

saludo("Ana", "Kendall", "Fiorella", "Santiago", "Daniel")