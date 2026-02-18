class Perro:
    def __init__(self, nombre, color, raza):
        self.nombre = nombre
        self.color = color
        self.raza = raza

    def presentarse(self):
        print(
            "Hola, soy", self.nombre,
            "soy de color", self.color,
            "y mi raza es", self.raza
        )