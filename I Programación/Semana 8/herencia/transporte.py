class MedioTransporte:
    def __init__(self, marca, velocidad_maxima):
        self.__marca = marca
        self.__velocidad_maxima = velocidad_maxima

    # Getter marca
    @property
    def marca(self):
        return self.__marca

    # Setter marca
    @marca.setter
    def marca(self, nueva_marca):
        if nueva_marca.strip() == "":
            raise ValueError("La marca no puede estar vacía.")
        self.__marca = nueva_marca

    # Getter velocidad
    @property
    def velocidad_maxima(self):
        return self.__velocidad_maxima

    # Setter velocidad
    @velocidad_maxima.setter
    def velocidad_maxima(self, nueva_velocidad):
        if nueva_velocidad <= 0:
            raise ValueError("La velocidad debe ser mayor que 0.")
        self.__velocidad_maxima = nueva_velocidad

    def moverse(self):
        print("El medio de transporte se está moviendo.")

    def __str__(self):
        return f"Marca: {self.marca}, Velocidad máxima: {self.velocidad_maxima} km/h"