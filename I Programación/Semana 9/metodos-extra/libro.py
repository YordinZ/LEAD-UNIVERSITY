class Libro:
    cantidad_libros = 0

    def __init__(self, titulo: str):
        self.titulo = titulo
        Libro.cantidad_libros += 1

    @classmethod
    def mostrar_cantidad(cls):
        print("Se han creado", cls.cantidad_libros, "libros")