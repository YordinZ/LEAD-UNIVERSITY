class Teclado:
    def escribir(self):
        return "Escribiendo con teclado físico"


class Computadora:
    def __init__(self):
        self.teclado = Teclado()

    def usar(self):
        print(self.teclado.escribir())

# La clase Computadora depende directamente de Teclado.
# Si luego quieres usar un teclado virtual, debes modificar la clase.