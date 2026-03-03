from avion import Avion
from carro import Carro
from tren import Tren


def main():
    carro1 = Carro("Toyota", 180, 4)
    avion1 = Avion("Boeing", 900, 12000)
    tren1 = Tren("Siemens", 250, 10)

    print(carro1)
    carro1.tocar_bocina()
    carro1.moverse()

    print()

    print(avion1)
    avion1.despegar()
    avion1.moverse()

    print()

    print(tren1)
    tren1.anunciar_estacion()
    tren1.moverse()

if __name__ == "__main__":
    main()