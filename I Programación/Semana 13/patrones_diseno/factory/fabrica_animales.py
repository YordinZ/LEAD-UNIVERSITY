from gato import Gato
from perro import Perro
from vaca import Vaca

# Fábrica
class FabricaAnimales:
    @staticmethod
    def crear_animal(tipo):
        if tipo == "perro":
            return Perro()
        elif tipo == "gato":
            return Gato()
        elif tipo == "vaca":
            return Vaca()
        else:
            raise ValueError("Tipo de animal no válido")

# Uso
animal1 = FabricaAnimales.crear_animal("perro")
animal2 = FabricaAnimales.crear_animal("gato")
animal3 = FabricaAnimales.crear_animal("vaca")

print(animal1.hacer_sonido())
print(animal2.hacer_sonido())
print(animal3.hacer_sonido())