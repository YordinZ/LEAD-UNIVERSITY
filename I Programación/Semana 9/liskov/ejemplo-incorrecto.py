class Empleado:
    def trabajar(self):
        print("El empleado está trabajando")

    def programar(self):
        print("El empleado está programando")

class Programador(Empleado):
    def programar(self):
        print("El programador escribe código")

class Gerente(Empleado):
    def programar(self):
        raise Exception("El conserje no programa")

def iniciar_trabajo(emp: Empleado):
    emp.trabajar()
    emp.programar()


e1 = Programador()
e2 = Gerente()

iniciar_trabajo(e1)  
iniciar_trabajo(e2) # causa una excepción porque el gerente no programa