from .empleado import Empleado


class Administrador(Empleado):
    def __init__(self, nombre, edad, salario, departamento):
        super().__init__(nombre, edad, salario)
        self.departamento = departamento

    @property
    def departamento(self):
        return self.__departamento

    @departamento.setter
    def departamento(self, nuevo_depa):
        if not isinstance(nuevo_depa, str) or nuevo_depa.strip() == "":
            raise ValueError("El departamento no puede estar vacío.")
        self.__departamento = nuevo_depa.strip().title()

    def __str__(self):
        return f"[Administrador] {super().__str__()} | Departamento: {self.__departamento}"


class Conserje(Empleado):
    TURNOS_VALIDOS = {"mañana", "tarde", "noche"}

    def __init__(self, nombre, edad, salario, turno):
        super().__init__(nombre, edad, salario)
        self.turno = turno

    @property
    def turno(self):
        return self.__turno

    @turno.setter
    def turno(self, nuevo_turno):
        if not isinstance(nuevo_turno, str) or nuevo_turno.strip().lower() not in self.TURNOS_VALIDOS:
            raise ValueError(f"Turno inválido. Opciones: {self.TURNOS_VALIDOS}")
        self.__turno = nuevo_turno.strip().lower()

    def __str__(self):
        return f"[Conserje] {super().__str__()} | Turno: {self.__turno}"


class Veterinario(Empleado):
    def __init__(self, nombre, edad, salario, especialidad):
        super().__init__(nombre, edad, salario)
        self.especialidad = especialidad

    @property
    def especialidad(self):
        return self.__especialidad

    @especialidad.setter
    def especialidad(self, nueva_esp):
        if not isinstance(nueva_esp, str) or nueva_esp.strip() == "":
            raise ValueError("La especialidad no puede estar vacía.")
        self.__especialidad = nueva_esp.strip().title()

    def __str__(self):
        return f"[Veterinario] {super().__str__()} | Especialidad: {self.__especialidad}"


class Guardian(Empleado):
    def __init__(self, nombre, edad, salario, zona):
        super().__init__(nombre, edad, salario)
        self.zona = zona

    @property
    def zona(self):
        return self.__zona

    @zona.setter
    def zona(self, nueva_zona):
        if not isinstance(nueva_zona, str) or nueva_zona.strip() == "":
            raise ValueError("La zona no puede estar vacía.")
        self.__zona = nueva_zona.strip().title()

    def __str__(self):
        return f"[Guardian] {super().__str__()} | Zona: {self.__zona}"
