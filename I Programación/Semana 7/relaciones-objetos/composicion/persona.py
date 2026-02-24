from corazon import Corazon
class Persona:
    def __init__(self, nombre: str, edad: int, pais: str):
        self.__nombre = nombre
        self.__edad = edad
        self.__pais = pais
        self.__corazon = Corazon()

    
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_pais(self):
        return self.__pais

    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_edad(self, edad):
        if edad >= 0:
            self.__edad = edad
        else:
            print("Error: la edad no puede ser negativa")

    def set_pais(self, pais):
        self.__pais = pais

    
    def presentarse(self):
        print(
            "Hola, mi nombre es", self.get_nombre(),
            "tengo", self.get_edad(), "años",
            "y soy de", self.get_pais()
        )
        print('Mi corazón late')
        self.__corazon.latir()

    def es_mayor_de_edad(self):
        return self.get_edad() >= 18

    def es_costarricense(self):
        return self.get_pais() == "Costa Rica"

    # -------- STR & REPR --------
    def __str__(self):
        return f"{self.get_nombre()} ({self.get_edad()} años) - País: {self.get_pais()}"

    def __repr__(self):
        return (
            f"Persona(nombre='{self.get_nombre()}', "
            f"edad={self.get_edad()}, "
            f"pais='{self.get_pais()}')"
        )
  
 