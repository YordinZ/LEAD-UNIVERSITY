class Vehiculo:
    def __init__(self, marca, model):
        self._marca = marca
        self._modelo = model

    def moverse(self):
        print("Moverse")

    @property
    def marca(self):
        return self._marca
    
    @property
    def modelo(self):
        return self._modelo

class Carro(Vehiculo):
    pass

class Bote(Vehiculo):
    def moverse(self):
        super().moverse()
        print("Zarpar!")

class Avion(Vehiculo):
    def moverse(self):
        print("Volar!")

carro1 = Carro("Ford", "Mustang")       
bote1 = Bote("Ibiza", "Touring 20") 
avion1 = Avion("Boeing", "747")     

for x in (carro1, bote1, avion1):
  print(x.marca, x.modelo)
  x.moverse()