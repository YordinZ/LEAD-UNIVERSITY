class Perro:
    def __init__(self, nombre, color, raza, tipo_alimento):
        self.nombre = nombre
        self.color = color
        self.raza = raza
        self.tipo_alimento = tipo_alimento
        self.tiene_vacunas = False

    def presentarse(self):
        print(
            "Hola, soy", self.nombre,
            "soy de color", self.color,
            "y mi raza es", self.raza,
            "como alimento de tipo,", self.tipo_alimento,
            "tiene vacunas?,", self.tiene_vacunas,
        )
    def vacunar(self):
        self.tiene_vacunas = True

    def poner_collar(self, tamano, color):
        self.tamano_collar = tamano
        self.color_collar = color