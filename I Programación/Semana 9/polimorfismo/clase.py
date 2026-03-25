class Carro:
    def __init__(self, marca, model):
        self.marca = marca
        self.modelo = model

    def moverse(self):
        print("Manejar!")

class Bote:
    def __init__(self, marca, model):
        self.marca = marca
        self.modelo = model

    def moverse(self):
        print("Zarpar!")

class Avion:
    def __init__(self, marca, model):
        self.marca = marca
        self.modelo = model

    def moverse(self):
        print("Volar!")

carro1 = Carro("Ford", "Mustang")       
bote1 = Bote("Ibiza", "Touring 20") 
avion1 = Avion("Boeing", "747")     

for x in (carro1, bote1, avion1):
  x.moverse()