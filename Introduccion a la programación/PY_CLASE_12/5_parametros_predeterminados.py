'''
valor de parámetro predeterminado
Definimos un valor para el parámetro en caso de que no venga
'''

def saludo(nombre="Karla", edad=None):
    print(f"Hola {nombre}, edad {edad}")

saludo("Gustavo", 29)
saludo(edad=19, nombre="María")
saludo()