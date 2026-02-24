class Gato:
    def __init__(self, nombre, color, raza, tipo_alimento):
        self.__nombre = nombre
        self.__color = color
        self.__raza = raza
        self.__tipo_alimento = tipo_alimento
        self.__tiene_vacunas = False

    def presentarse(self):
        print(
            "Hola, soy", self.get_nombre(),
            "soy de color", self.get_color(),
            "y mi raza es", self.get_raza(),
            "como alimento de tipo,", self.get_tipo_alimento(),
            "tiene vacunas?,", self.get_tiene_vacunas(),
        )
    def vacunar(self):
        self.set_tiene_vacunas(True)

    
     # ---- nombre ----
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    # ---- color ----
    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    # ---- raza ----
    def get_raza(self):
        return self.__raza

    def set_raza(self, raza):
        self.__raza = raza

    # ---- tipo_alimento ----
    def get_tipo_alimento(self):
        return self.__tipo_alimento

    def set_tipo_alimento(self, tipo_alimento):
        self.__tipo_alimento = tipo_alimento

    # ---- tiene_vacunas ----
    def get_tiene_vacunas(self):
        return self.__tiene_vacunas

    def set_tiene_vacunas(self, estado):
        self.__tiene_vacunas = estado