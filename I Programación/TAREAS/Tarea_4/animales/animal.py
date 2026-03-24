class Animal:
    """
    Clase padre que representa un animal del zoológico.

    Atributos:
        nombre (str): Nombre del animal.
        raza (str): Raza o especie del animal.
        genero (str): Género del animal ('macho' o 'hembra').

    Todos los atributos son privados y se acceden mediante @property y setters
    con validaciones básicas.
    """

    GENEROS_VALIDOS = {"macho", "hembra"}

    def __init__(self, nombre, raza, genero):
        # Se usan los setters para aplicar validaciones desde el inicio
        self.nombre = nombre
        self.raza   = raza
        self.genero = genero

    def __str__(self):
        return (f"Nombre: {self.__nombre} | "
                f"Raza: {self.__raza} | "
                f"Género: {self.__genero}")

    # --- nombre ---
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or valor.strip() == "":
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = valor.strip().capitalize()

    # --- raza ---
    @property
    def raza(self):
        return self.__raza

    @raza.setter
    def raza(self, valor):
        if not isinstance(valor, str) or valor.strip() == "":
            raise ValueError("La raza no puede estar vacía.")
        self.__raza = valor.strip().capitalize()

    # --- genero ---
    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, valor):
        if not isinstance(valor, str) or valor.strip().lower() not in self.GENEROS_VALIDOS:
            raise ValueError(f"Género debe ser: {self.GENEROS_VALIDOS}")
        self.__genero = valor.strip().lower()
