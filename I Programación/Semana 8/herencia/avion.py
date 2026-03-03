from transporte import MedioTransporte
class Avion(MedioTransporte):
    def __init__(self, marca, velocidad_maxima, altitud_maxima):
        super().__init__(marca, velocidad_maxima)
        self.__altitud_maxima = altitud_maxima

    @property
    def altitud_maxima(self):
        return self.__altitud_maxima

    @altitud_maxima.setter
    def altitud_maxima(self, nueva_altitud):
        if nueva_altitud <= 0:
            raise ValueError("La altitud debe ser mayor que 0.")
        self.__altitud_maxima = nueva_altitud

    def despegar(self):
        print("El avión está despegando.")

    def __str__(self):
        return f"{super().__str__()}, Altitud máxima: {self.altitud_maxima} m"