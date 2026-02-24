class Curso:
    def __init__(self, nombre, profesor):
        self.__nombre = nombre
        self.__profesor = profesor

    # ---- getters ----
    def get_nombre(self):
        return self.__nombre

    def get_profesor(self):
        return self.__profesor

    # ---- str ----
    def __str__(self):
        return f"Curso: {self.__nombre} | Profesor: {self.__profesor}"