class Trabajador:
    def trabajar(self):
        pass

    def comer(self):
        pass


class Robot(Trabajador):
    def trabajar(self):
        print("El robot está trabajando")

    def comer(self):
        raise Exception("El robot no come")
    
# El Robot está obligado a implementar comer(), aunque no lo necesita.