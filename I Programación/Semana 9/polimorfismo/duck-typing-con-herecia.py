class Deportista:

    def entrenar(self):
        print("El deportista entrena")


class Futbolista(Deportista):

    def entrenar(self):
        print("El futbolista practica tiros")


class Beisbolista(Deportista):

    def entrenar(self):
        print("El beisbolista batea")


class Atleta(Deportista):

    def entrenar(self):
        print("El atleta corre")


def iniciar_entrenamiento(deportista):
    deportista.entrenar()


f = Futbolista()
b = Beisbolista()
a = Atleta()

iniciar_entrenamiento(f)
iniciar_entrenamiento(b)
iniciar_entrenamiento(a)