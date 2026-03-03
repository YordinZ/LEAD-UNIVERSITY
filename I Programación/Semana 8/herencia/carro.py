from transporte import MedioTransporte
class Carro(MedioTransporte):
    def __init__(self, marca, velocidad_maxima, puertas):
        super().__init__(marca, velocidad_maxima)
        self.__puertas = puertas

    @property
    def puertas(self):
        return self.__puertas

    @puertas.setter
    def puertas(self, nuevas_puertas):
        if nuevas_puertas <= 0:
            raise ValueError("El carro debe tener al menos una puerta.")
        self.__puertas = nuevas_puertas

    def tocar_bocina(self):
        print("¡Beep beep!")

    def __str__(self):
        return f"{super().__str__()}, Puertas: {self.puertas}"