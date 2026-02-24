class Estudiante:
    def __init__(self, nombre):
        self.__nombre = nombre

    # ---- getter ----
    def get_nombre(self):
        return self.__nombre

    # ---- setter ----
    def set_nombre(self, nombre):
        self.__nombre = nombre

    # ---- str ----
    def __str__(self):
        return f"Estudiante: {self.__nombre}"