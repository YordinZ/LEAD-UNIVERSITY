from .animal import Animal


class Reptil(Animal):
    def __init__(self, nombre, raza, genero, es_venenoso=False):
        super().__init__(nombre, raza, genero)
        self.es_venenoso = es_venenoso

    @property
    def es_venenoso(self):
        return self.__es_venenoso

    @es_venenoso.setter
    def es_venenoso(self, valor):
        if not isinstance(valor, bool):
            raise ValueError("es_venenoso debe ser True o False.")
        self.__es_venenoso = valor

    def __str__(self):
        venenoso = "Sí" if self.__es_venenoso else "No"
        return f"[Reptil] {super().__str__()} | Venenoso: {venenoso}"


class Mamifero(Animal):
    def __init__(self, nombre, raza, genero, domestico=True):
        super().__init__(nombre, raza, genero)
        self.domestico = domestico

    @property
    def domestico(self):
        return self.__domestico

    @domestico.setter
    def domestico(self, valor):
        if not isinstance(valor, bool):
            raise ValueError("domestico debe ser True o False.")
        self.__domestico = valor

    def __str__(self):
        dom = "Sí" if self.__domestico else "No"
        return f"[Mamífero] {super().__str__()} | Doméstico: {dom}"


class Ave(Animal):
    def __init__(self, nombre, raza, genero, puede_volar=True):
        super().__init__(nombre, raza, genero)
        self.puede_volar = puede_volar

    @property
    def puede_volar(self):
        return self.__puede_volar

    @puede_volar.setter
    def puede_volar(self, valor):
        if not isinstance(valor, bool):
            raise ValueError("puede_volar debe ser True o False.")
        self.__puede_volar = valor

    def __str__(self):
        vuela = "Sí" if self.__puede_volar else "No"
        return f"[Ave] {super().__str__()} | Vuela: {vuela}"


class Pez(Animal):
    def __init__(self, nombre, raza, genero, agua_salada=False):
        super().__init__(nombre, raza, genero)
        self.agua_salada = agua_salada

    @property
    def agua_salada(self):
        return self.__agua_salada

    @agua_salada.setter
    def agua_salada(self, valor):
        if not isinstance(valor, bool):
            raise ValueError("agua_salada debe ser True o False.")
        self.__agua_salada = valor

    def __str__(self):
        agua = "Sí" if self.__agua_salada else "No"
        return f"[Pez] {super().__str__()} | Agua salada: {agua}"


class Anfibio(Animal):
    def __init__(self, nombre, raza, genero, habitat="tierra y agua"):
        super().__init__(nombre, raza, genero)
        self.habitat = habitat

    @property
    def habitat(self):
        return self.__habitat

    @habitat.setter
    def habitat(self, valor):
        if not isinstance(valor, str) or valor.strip() == "":
            raise ValueError("El hábitat no puede estar vacío.")
        self.__habitat = valor.strip().lower()

    def __str__(self):
        return f"[Anfibio] {super().__str__()} | Hábitat: {self.__habitat}"
