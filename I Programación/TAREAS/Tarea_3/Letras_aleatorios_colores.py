import random
import string

def generar_letra():
    return random.choice(string.ascii_uppercase)

def generar_palabra_random(longitud=7):
    return "".join(generar_letra() for _ in range(longitud))
