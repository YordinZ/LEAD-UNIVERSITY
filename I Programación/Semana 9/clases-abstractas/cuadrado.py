from figura import Figura
class Cuadrado(Figura):

    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado