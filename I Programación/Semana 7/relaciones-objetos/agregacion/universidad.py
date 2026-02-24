
class Universidad:
    def __init__(self):
        self.__estudiantes = []

    # ---- getter ----
    def get_estudiantes(self):
        return self.__estudiantes

    # ---- setter / acción ----
    def agregar_estudiante(self, estudiante):
        self.__estudiantes.append(estudiante)

    # ---- str ----
    def __str__(self):
        if not self.__estudiantes:
            return "Universidad sin estudiantes"

        texto = "Universidad - Lista de estudiantes:\n"
        for e in self.__estudiantes:
            texto += f"- {e}\n"
        return texto