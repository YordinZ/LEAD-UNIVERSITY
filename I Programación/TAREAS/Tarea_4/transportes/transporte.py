class Transporte:
    """
    Clase padre que representa un medio de transporte dentro del zoológico.

    Atributos:
        marca (str): Marca del vehículo o transporte.
        modelo (str): Modelo específico del transporte.
        color (str): Color del transporte (debe ser un color válido de la lista).
        velocidad_maxima (float): Velocidad máxima en km/h.

    Todos los atributos son privados y se acceden mediante @property y setters
    con validaciones básicas.
    """

    COLORES_VALIDOS = {"rojo", "azul", "verde", "negro", "blanco", "amarillo", "gris", "naranja"}

    def __init__(self, marca, modelo, color, velocidad_maxima):
        # Se usan los setters para aplicar validaciones desde el inicio
        self.marca            = marca
        self.modelo           = modelo
        self.color            = color
        self.velocidad_maxima = velocidad_maxima

    def __str__(self):
        return (f"Marca: {self.__marca} | "
                f"Modelo: {self.__modelo} | "
                f"Color: {self.__color} | "
                f"Vel. máx.: {self.__velocidad_maxima} km/h")

    # --- marca ---
    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, valor):
        if not isinstance(valor, str) or valor.strip() == "":
            raise ValueError("La marca no puede estar vacía.")
        self.__marca = valor.strip().capitalize()

    # --- modelo ---
    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, valor):
        if not isinstance(valor, str) or valor.strip() == "":
            raise ValueError("El modelo no puede estar vacío.")
        self.__modelo = valor.strip().capitalize()

    # --- color ---
    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, valor):
        if not isinstance(valor, str) or valor.strip().lower() not in self.COLORES_VALIDOS:
            raise ValueError(f"Color debe ser uno de: {self.COLORES_VALIDOS}")
        self.__color = valor.strip().lower()

    # --- velocidad_maxima ---
    @property
    def velocidad_maxima(self):
        return self.__velocidad_maxima

    @velocidad_maxima.setter
    def velocidad_maxima(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("La velocidad máxima debe ser un número positivo.")
        self.__velocidad_maxima = float(valor)
