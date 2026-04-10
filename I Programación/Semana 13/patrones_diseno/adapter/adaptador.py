from reproductor_nuevo import ReproductorNuevo
from reproductor_viejo import ReproductorViejo
# Adaptador
class Adaptador:
    def __init__(self, reproductor_viejo):
        self.reproductor_viejo = reproductor_viejo

    def reproducir(self):
        return self.reproductor_viejo.play()

# Uso
#el sistema espera reproducir()
# la clase vieja solo tiene play()
# el adaptador recibe el objeto viejo y “traduce” la llamada
viejo = ReproductorViejo()
adaptado = Adaptador(viejo)

print(adaptado.reproducir())