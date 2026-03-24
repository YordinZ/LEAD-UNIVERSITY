from .transporte import Transporte


class Bicicleta(Transporte):
    def __init__(self, marca, modelo, color, velocidad_maxima, num_marchas):
        super().__init__(marca, modelo, color, velocidad_maxima)
        self.num_marchas = num_marchas

    @property
    def num_marchas(self):
        return self.__num_marchas

    @num_marchas.setter
    def num_marchas(self, valor):
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("El número de marchas debe ser un entero positivo.")
        self.__num_marchas = valor

    def __str__(self):
        return f"[Bicicleta] {super().__str__()} | Marchas: {self.__num_marchas}"


class Cuadraciclo(Transporte):
    def __init__(self, marca, modelo, color, velocidad_maxima, cilindrada):
        super().__init__(marca, modelo, color, velocidad_maxima)
        self.cilindrada = cilindrada

    @property
    def cilindrada(self):
        return self.__cilindrada

    @cilindrada.setter
    def cilindrada(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("La cilindrada debe ser un número positivo.")
        self.__cilindrada = float(valor)

    def __str__(self):
        return f"[Cuadraciclo] {super().__str__()} | Cilindrada: {self.__cilindrada} cc"


class Patineta(Transporte):
    def __init__(self, marca, modelo, color, velocidad_maxima, es_electrica=False):
        super().__init__(marca, modelo, color, velocidad_maxima)
        self.es_electrica = es_electrica

    @property
    def es_electrica(self):
        return self.__es_electrica

    @es_electrica.setter
    def es_electrica(self, valor):
        if not isinstance(valor, bool):
            raise ValueError("El valor de es_electrica debe ser True o False.")
        self.__es_electrica = valor

    def __str__(self):
        electrica = "Sí" if self.__es_electrica else "No"
        return f"[Patineta] {super().__str__()} | Eléctrica: {electrica}"
