class Profesor:
    def __init__(self, nombre):
        self.__nombre = nombre

    # ---- getter ----
    def get_nombre(self):
        return self.__nombre

    # ---- str ----
    def __str__(self):
        return f"{self.__nombre}"