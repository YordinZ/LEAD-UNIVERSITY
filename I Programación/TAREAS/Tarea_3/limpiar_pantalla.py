import os

def clear(): # Función para limpiar la pantalla
    os.system('cls' if os.name == 'nt' else 'clear')
