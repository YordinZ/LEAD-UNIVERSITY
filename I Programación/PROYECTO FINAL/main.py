"""
main.py
Punto de entrada de la Tienda de Videojuegos.
"""
import sys # Para manipular el path y manejar excepciones de salida
import os # Para obtener la ruta del archivo actual y asegurar que los módulos se importen correctamente

# Asegurar que el directorio raíz esté en el path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils.excepciones import SalidaForzada
from utils.colors import VERDE, NEGRITA, RESET
from ui.menus import menu


def salir():
    print(f"\n{VERDE}{NEGRITA}¡Hasta luego! 👋{RESET}\n")
    raise SystemExit(0)


if __name__ == "__main__":
    try:
        menu()
    except SalidaForzada:
        salir()
    except KeyboardInterrupt:
        print(f"\n{VERDE}{NEGRITA}Programa interrumpido. ¡Hasta luego! 👋{RESET}\n")
