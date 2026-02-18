class Persona:
    def __init__(self, nombre, edad, pais):
        self.nombre = nombre
        self.edad = edad
        self.pais = pais

    def presentarse(self):
        print(
            "Hola, mi nombre es", self.nombre,
            "tengo", self.edad, "años",
            "y soy de", self.pais
        )

    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False
