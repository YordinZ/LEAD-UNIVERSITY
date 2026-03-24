class Empleado:
    """
    Clase padre que representa a un empleado del zoológico.

    Atributos:
        nombre (str): Nombre completo del empleado.
        edad (int): Edad del empleado en años.
        salario (float): Salario mensual del empleado en colones/dólares.

    Todos los atributos son privados y se acceden mediante @property y setters
    que aplican validaciones básicas.
    """

    def __init__(self, nombre, edad, salario):
        # Se usan los setters para aplicar validaciones desde el inicio
        self.nombre  = nombre
        self.edad    = edad
        self.salario = salario

    def __str__(self):
        return (f"Nombre: {self.__nombre} | "
                f"Edad: {self.__edad} | "
                f"Salario: ${self.__salario:,.2f}")

    # --- nombre ---
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if not isinstance(nuevo_nombre, str) or nuevo_nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = nuevo_nombre.strip().title()

    # --- edad ---
    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, nueva_edad):
        if not isinstance(nueva_edad, int) or nueva_edad <= 0:
            raise ValueError("La edad debe ser un número entero mayor que 0.")
        self.__edad = nueva_edad

    # --- salario ---
    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, nuevo_salario):
        if not isinstance(nuevo_salario, (int, float)) or nuevo_salario < 0:
            raise ValueError("El salario no puede ser negativo.")
        self.__salario = float(nuevo_salario)
