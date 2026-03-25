from figura import Figura
from cuadrado import Cuadrado
from rectangulo import Rectangulo
from triangulo import Triangulo

def principal():
    c = Cuadrado(4)
    r = Rectangulo(5, 3)

    print(c.area())
    print(r.area())

    # Falla porque es una clase abstracta y no se puede crear una instanciua
    # f = Figura()

    # Da error porque no tiene implementado area
    # t = Triangulo()
    # print(t.area())



if __name__ == "__main__":
    principal()