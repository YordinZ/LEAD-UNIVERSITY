from abc import ABC, abstractmethod
import os

# ── Clase abstracta ──────────────────────────────────────────
class Figura(ABC):
    @abstractmethod #obliga a todas las subclases a implementar volumen()
    def volumen(self):
        pass #significa que no tiene cuerpo — solo declara que el método debe existir

# ── Subclases ─────────────────────────────────────────────────
class Cubo(Figura):
    def __init__(self, lado):
        self.lado = lado

    def volumen(self):
        return self.lado ** 3

class Paralelepipedo(Figura):
    def __init__(self, largo, ancho, alto):
        self.largo = largo
        self.ancho = ancho
        self.alto = alto

    def volumen(self):
        return self.largo * self.ancho * self.alto

class Cilindro(Figura):
    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura

    def volumen(self):
        return 3.1416 * self.radio ** 2 * self.altura

class Esfera(Figura):
    def __init__(self, radio):
        self.radio = radio

    def volumen(self):
        return (4/3) * 3.1416 * self.radio ** 3

class Cono(Figura):
    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura

    def volumen(self):
        return (1/3) * 3.1416 * self.radio ** 2 * self.altura

# ── Principio de Sustitución de Liskov ───────────────────────
def imprimir_volumen(figura: Figura):
    print(f"El volumen de {figura.__class__.__name__} es: {figura.volumen():.2f}")

# ── Utilidades ────────────────────────────────────────────────
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def volver_a_menu():
    input("\nPresione Enter para volver al menú...")

# ── Main ──────────────────────────────────────────────────────
def main():
    # Objetos predefinidos de cada figura
    figuras = { #objetos predefinidos para cada figura, con dimensiones arbitrarias
        '1': Cubo(3),
        '2': Paralelepipedo(2, 3, 4),
        '3': Cilindro(3, 5),
        '4': Esfera(3),
        '5': Cono(3, 5)
    }

    while True:
        clear()
        print("..... Calculadora de Volúmenes .....")
        print("1. Volumen del Cubo")
        print("2. Volumen del Paralelepípedo")
        print("3. Volumen del Cilindro")
        print("4. Volumen de la Esfera")
        print("5. Volumen del Cono")
        print("6. Salir")
        opcion = input("\nSeleccione una opción: ")

        if opcion in figuras:
            clear()
            imprimir_volumen(figuras[opcion])   #Liskov
            volver_a_menu()
        elif opcion == '6':
            clear()
            print("Hasta luego.")
            break
        else:
            print("Opción no válida.")
            volver_a_menu()

if __name__ == "__main__":
    main()