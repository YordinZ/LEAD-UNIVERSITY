class Trabajador:
    def trabajar(self):
        pass


class Comedor:
    def comer(self):
        pass


class Persona(Trabajador, Comedor):
    def trabajar(self):
        print("La persona está trabajando")

    def comer(self):
        print("La persona está comiendo")


class Robot(Trabajador):
    def trabajar(self):
        print("El robot está trabajando")

persona = Persona()
persona.trabajar()
persona.comer()

robot = Robot()
robot.trabajar()