"""
Tarea Programada 2: Agencia de Seguridad del Reino
Menu interactivo principal.

Ejecutar con: python main.py
"""

from n_reinas import ejecutar_n_reinas
from subconjuntos import ejecutar_subconjuntos


def mostrar_menu():
    print("\n" + "." * 50)
    print("AGENCIA DE SEGURIDAD DEL REINO")
    print("." * 50)
    print()
    print("1. Vigilancia del Castillo (N-Reinas)")
    print("2. Gestion de Recursos del Reino (Subconjuntos)")
    print("3. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opcion: ").strip()

        if opcion == "1":
            ejecutar_n_reinas()
        elif opcion == "2":
            ejecutar_subconjuntos()
        elif opcion == "3":
            print("\nFin del programa. Hasta pronto.")
            break
        else:
            print("\nOpcion invalida. Intente nuevamente.")


if __name__ == "__main__":
    main()
