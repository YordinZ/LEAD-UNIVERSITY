from gato import Gato
from perro import Perro

def main():
    felix = Gato("Felix", "Negro", "Felino de gran tamaño", "Whiskas")
    firulais = Perro("Firulais", "Cafe", "Zaguate", "Super Perro")
    felix.presentarse()
    firulais.presentarse()
    print(firulais.nombre) # se puede acceder porque es un atributo público
    #print(felix.__nombre) # no se puede acceder porque es un atributo privado
    print(felix.get_nombre()) # no se puede acceder porque es un atributo privado

main()