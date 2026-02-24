class Libro:
    def __init__(self, nombre: str, paginas: int, autor: str):
        self.__nombre = nombre
        self.__paginas = paginas
        self.__autor = autor

    def get_nombre(self):
        return self.__nombre

    def get_paginas(self):
        return self.__paginas

    def get_autor(self):
        return self.__autor

    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_paginas(self, paginas):
        if paginas > 0:
            self.__paginas = paginas
        else:
            print("Error: el número de páginas debe ser mayor que 0")

    def set_autor(self, autor):
        self.__autor = autor

    
    def __str__(self):
        return (
            f"Libro: '{self.__nombre}' | "
            f"Autor: {self.__autor} | "
            f"Páginas: {self.__paginas}"
        )