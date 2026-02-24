from carro import Carro
from persona import Persona
def main():
    frank = Persona("Frank Martin", 38, "USA")
    rav4 = Carro("Toyota", "Rav4", "Gris", 256, frank)
    
    toretto = Persona("Dominick Toretto", 35, "USA")
    crv = Carro("Honda", "CRV", "Azul", 300,  toretto)

    print(rav4)
    print(len(rav4))

    print(crv)
    print(len(crv))
    print(repr(crv))

    print(toretto)
    print(len(toretto))
    print(len(frank))
    print(repr(toretto))

main()