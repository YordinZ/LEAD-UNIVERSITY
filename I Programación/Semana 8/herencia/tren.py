from transporte import MedioTransporte
class Tren(MedioTransporte):
    def __init__(self, marca, velocidad_maxima, cantidad_vagones):
        super().__init__(marca, velocidad_maxima)
        self.__cantidad_vagones = cantidad_vagones

    @property
    def cantidad_vagones(self):
        return self.__cantidad_vagones

    @cantidad_vagones.setter
    def cantidad_vagones(self, nuevos_vagones):
        if nuevos_vagones <= 0:
            raise ValueError("El tren debe tener al menos un vagón.")
        self.__cantidad_vagones = nuevos_vagones

    def anunciar_estacion(self):
        print("Próxima estación en 5 minutos.")

    def __str__(self):
        return f"{super().__str__()}, Vagones: {self.cantidad_vagones}"