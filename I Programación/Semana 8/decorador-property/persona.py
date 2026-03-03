class Persona:
    def __init__(self, nombre: str, edad: int):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @property
    def edad(self):
        return self._edad

    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        self._nombre = nuevo_nombre

    @edad.setter
    def edad(self, nueva_edad: int):
        self._edad = nueva_edad