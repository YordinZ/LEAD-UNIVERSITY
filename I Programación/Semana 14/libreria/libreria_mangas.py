class LibreriaDeMangas:
    def __init__(self):
        self.mangas = {
            "Naruto": 3,
            "One Piece": 5,
            "Attack on Titan": 2,
            "Demon Slayer": 4
        }

    def agregar_manga(self, nombre):
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre del manga debe ser un texto no vacío")

        nombre = nombre.strip()

        if nombre in self.mangas:
            self.mangas[nombre] += 1
        else:
            self.mangas[nombre] = 1

    def obtener_cantidad(self, nombre):
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre del manga debe ser un texto no vacío")

        nombre = nombre.strip()
        return self.mangas.get(nombre, 0)

    def existe_manga(self, nombre):
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre del manga debe ser un texto no vacío")

        nombre = nombre.strip()
        return nombre in self.mangas

    def eliminar_manga(self, nombre):
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre del manga debe ser un texto no vacío")

        nombre = nombre.strip()

        if nombre not in self.mangas:
            raise ValueError("El manga no existe en la librería")

        if self.mangas[nombre] > 1:
            self.mangas[nombre] -= 1
        else:
            del self.mangas[nombre]

    def obtener_todos_los_mangas(self):
        return self.mangas.copy()
    