class DispositivoEntrada:
    def escribir(self):
        pass


class TecladoFisico(DispositivoEntrada):
    def escribir(self):
        return "Escribiendo con teclado físico"


class TecladoVirtual(DispositivoEntrada):
    def escribir(self):
        return "Escribiendo con teclado virtual"


class Computadora:
    def __init__(self, dispositivo):
        self.dispositivo = dispositivo

    def usar(self):
        print(self.dispositivo.escribir())


# La computadora ya no depende de una clase específica, 
# sino de cualquier objeto que tenga el comportamiento esperado.

teclado1 = TecladoFisico()
pc1 = Computadora(teclado1)
pc1.usar()

teclado2 = TecladoVirtual()
pc2 = Computadora(teclado2)
pc2.usar()