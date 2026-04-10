class Ave:
    def comer(self):
        print("El ave está comiendo")


class AveVoladora(Ave):
    def volar(self):
        print("El ave está volando")


class Paloma(AveVoladora):
    pass


class Pinguino(Ave):
    def nadar(self):
        print("El pingüino está nadando")

paloma = Paloma()
paloma.comer()
paloma.volar()

pinguino = Pinguino()
pinguino.comer()
pinguino.nadar()