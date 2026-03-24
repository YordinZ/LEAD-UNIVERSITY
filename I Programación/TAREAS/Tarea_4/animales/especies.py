from .tipos_animal import Mamifero, Pez, Reptil, Ave, Anfibio


class Leon(Mamifero):
    """Clase específica que representa a un León (hereda de Mamifero)."""

    def __init__(self, nombre, genero, tamanio_melena="mediana"):
        super().__init__(nombre, "León africano", genero, domestico=False)
        self.tamanio_melena = tamanio_melena

    @property
    def tamanio_melena(self):
        return self.__tamanio_melena

    @tamanio_melena.setter
    def tamanio_melena(self, valor):
        opciones = {"pequeña", "mediana", "grande"}
        if not isinstance(valor, str) or valor.strip().lower() not in opciones:
            raise ValueError(f"Tamaño de melena debe ser: {opciones}")
        self.__tamanio_melena = valor.strip().lower()

    def __str__(self):
        return f"[León] {super().__str__()} | Melena: {self.__tamanio_melena}"


class Tiburon(Pez):
    """Clase específica que representa a un Tiburón (hereda de Pez)."""

    def __init__(self, nombre, genero, longitud_metros=3.0):
        super().__init__(nombre, "Tiburón blanco", genero, agua_salada=True)
        self.longitud_metros = longitud_metros

    @property
    def longitud_metros(self):
        return self.__longitud_metros

    @longitud_metros.setter
    def longitud_metros(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("La longitud debe ser un número positivo.")
        self.__longitud_metros = float(valor)

    def __str__(self):
        return f"[Tiburón] {super().__str__()} | Longitud: {self.__longitud_metros} m"


class Cocodrilo(Reptil):
    """Clase específica que representa a un Cocodrilo (hereda de Reptil)."""

    def __init__(self, nombre, genero, peso_kg=200.0):
        super().__init__(nombre, "Cocodrilo del Nilo", genero, es_venenoso=False)
        self.peso_kg = peso_kg

    @property
    def peso_kg(self):
        return self.__peso_kg

    @peso_kg.setter
    def peso_kg(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("El peso debe ser un número positivo.")
        self.__peso_kg = float(valor)

    def __str__(self):
        return f"[Cocodrilo] {super().__str__()} | Peso: {self.__peso_kg} kg"


class Aguila(Ave):
    """Clase específica que representa a un Águila (hereda de Ave)."""

    def __init__(self, nombre, genero, envergadura_cm=200.0):
        super().__init__(nombre, "Águila real", genero, puede_volar=True)
        self.envergadura_cm = envergadura_cm

    @property
    def envergadura_cm(self):
        return self.__envergadura_cm

    @envergadura_cm.setter
    def envergadura_cm(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("La envergadura debe ser un número positivo.")
        self.__envergadura_cm = float(valor)

    def __str__(self):
        return f"[Águila] {super().__str__()} | Envergadura: {self.__envergadura_cm} cm"


class Sapo(Anfibio):
    """Clase específica que representa a un Sapo (hereda de Anfibio)."""

    def __init__(self, nombre, genero, es_toxico=False):
        super().__init__(nombre, "Sapo común", genero, habitat="tierra y agua")
        self.es_toxico = es_toxico

    @property
    def es_toxico(self):
        return self.__es_toxico

    @es_toxico.setter
    def es_toxico(self, valor):
        if not isinstance(valor, bool):
            raise ValueError("es_toxico debe ser True o False.")
        self.__es_toxico = valor

    def __str__(self):
        toxico = "Sí" if self.__es_toxico else "No"
        return f"[Sapo] {super().__str__()} | Tóxico: {toxico}"
