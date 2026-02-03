range(3)
'''
Los argumentos: 
- Para pasar información a la función
- El valor que se envia cuando se llama a la función
Los parámetros: 
- Son las variables que están dentro de los parentesis en las funciones.
'''
#def nombre_funcion(parámetro1)
def saludo(nombre, apellido, edad):
    print(f"Hola {nombre} {apellido}, Edad: {edad}")

saludo("Sharleth", "Tafalla", 10) #->Argumento
saludo ("Juan", "Rojas", 12)

print("---------------------------------------")
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