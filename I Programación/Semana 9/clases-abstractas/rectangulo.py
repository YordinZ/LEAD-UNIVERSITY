from figura import Figura
class Rectangulo(Figura):

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura