#Clase documentada al estilo google
class Perro:
    """Representa un perro con atributos básicos y comportamientos simples.

    Esta clase modela un perro con información sobre su identidad,
    alimentación, estado de vacunación y accesorios como collar.
    """

    def __init__(self, nombre: str, color: str, raza: str, tipo_alimento: str):
        """Inicializa una nueva instancia de Perro.

        Args:
            nombre (str): Nombre del perro.
            color (str): Color del perro.
            raza (str): Raza del perro.
            tipo_alimento (str): Tipo de alimento que consume.
        """
        self.__nombre = nombre
        self.__color = color
        self.__raza = raza
        self.__tipo_alimento = tipo_alimento
        self.__tiene_vacunas = False
        self.__tamano_collar = None
        self.__color_collar = None

    @property
    def nombre(self) -> str:
        """str: Obtiene el nombre del perro."""
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        """Actualiza el nombre del perro.

        Args:
            nuevo_nombre (str): Nuevo nombre del perro.

        Raises:
            ValueError: Si el nombre está vacío.
        """
        if not nuevo_nombre:
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = nuevo_nombre

    @property
    def color(self) -> str:
        """str: Obtiene el color del perro."""
        return self.__color

    @color.setter
    def color(self, nuevo_color: str) -> None:
        """Actualiza el color del perro.

        Args:
            nuevo_color (str): Nuevo color del perro.

        Raises:
            ValueError: Si el color está vacío.
        """
        if not nuevo_color:
            raise ValueError("El color no puede estar vacío.")
        self.__color = nuevo_color

    @property
    def raza(self) -> str:
        """str: Obtiene la raza del perro."""
        return self.__raza

    @raza.setter
    def raza(self, nueva_raza: str) -> None:
        """Actualiza la raza del perro.

        Args:
            nueva_raza (str): Nueva raza del perro.

        Raises:
            ValueError: Si la raza está vacía.
        """
        if not nueva_raza:
            raise ValueError("La raza no puede estar vacía.")
        self.__raza = nueva_raza

    @property
    def tipo_alimento(self) -> str:
        """str: Obtiene el tipo de alimento del perro."""
        return self.__tipo_alimento

    @tipo_alimento.setter
    def tipo_alimento(self, nuevo_tipo: str) -> None:
        """Actualiza el tipo de alimento del perro.

        Args:
            nuevo_tipo (str): Nuevo tipo de alimento.

        Raises:
            ValueError: Si el tipo de alimento está vacío.
        """
        if not nuevo_tipo:
            raise ValueError("El tipo de alimento no puede estar vacío.")
        self.__tipo_alimento = nuevo_tipo

    @property
    def tiene_vacunas(self) -> bool:
        """bool: Indica si el perro tiene vacunas aplicadas."""
        return self.__tiene_vacunas

    @property
    def tamano_collar(self) -> str:
        """Optional[str]: Tamaño del collar asignado al perro."""
        return self.__tamano_collar

    @property
    def color_collar(self) -> str:
        """Optional[str]: Color del collar asignado al perro."""
        return self.__color_collar

    def presentarse(self) -> None:
        """Imprime en consola la información del perro."""
        print(
            f"Hola, soy {self.__nombre}, "
            f"soy de color {self.__color}, "
            f"mi raza es {self.__raza}, "
            f"como alimento de tipo {self.__tipo_alimento}, "
            f"¿tengo vacunas? {self.__tiene_vacunas}"
        )

    def vacunar(self) -> None:
        """Marca al perro como vacunado."""
        self.__tiene_vacunas = True

    def poner_collar(self, tamano: str, color: str) -> None:
        """Asigna un collar al perro.

        Args:
            tamano (str): Tamaño del collar (por ejemplo, 'S', 'M', 'L').
            color (str): Color del collar.
        """
        self.__tamano_collar = tamano
        self.__color_collar = color

    def ladra_amigo(self) -> None:
        """Simula el ladrido del perro."""
        print("guau guau guau!")

