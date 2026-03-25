class Animal:
    def mover(self):
        print("El animal se mueve")

class Perro(Animal):
    def mover(self):
        print("El perro corre")

class Pez(Animal):
    def mover(self):
        print("El pez nada")
    

def mover_animal(animal: Animal):
    animal.mover()

mover_animal(Perro())
mover_animal(Pez())