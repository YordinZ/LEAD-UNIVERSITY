import random
import string

def generar_letra(): # Función para generar una letra mayúscula aleatoria
    return random.choice(string.ascii_uppercase)

def generar_palabra_random(longitud=7): # Función para generar una palabra aleatoria de una longitud dada
    return "".join(generar_letra() for _ in range(longitud))
