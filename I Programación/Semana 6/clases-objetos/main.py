from carro import Carro
from perro import Perro
from persona import Persona

def crear_perros():
    firulais = Perro("Firulais", "Cafe", "Zaguate")
    snoopy = Perro("Snoopy", "Blanco", "Beagle")
    firulais.presentarse()
    snoopy.presentarse()

def crear_personas():
    charlie = Persona("Charlie Brown", 10, "USA")
    tommy = Persona("Tommy PIckles", 10, "USA")
    charlie.presentarse()
    tommy.presentarse()

def crear_carros():
    rav4 = Carro("Toyota", "Rav4", "Gris")
    crv = Carro("Honda", "CRV", "Azul")
    rav4.encender()
    rav4.apagar()
    crv.encender()
    crv.apagar()

def main():
    print("=====================================")
    crear_perros()
    print("=====================================")
    crear_personas()
    print("=====================================")
    crear_carros()
    print("=====================================")
    
main()