class Persona:
    def __init__(self, nombre: str, edad: int):
        self.__nombre = nombre
        self.__edad = edad

    # --- getters ---
    def get_nombre(self) -> str:
        return self.__nombre

    def get_edad(self) -> int:
        return self.__edad

    # --- setters ---
    def set_nombre(self, nombre: str) -> None:
        self.__nombre = nombre

    def set_edad(self, edad: int) -> None:
        self.__edad = edad

    # --- dunder methods ---
    def __str__(self) -> str:
        return f"Persona(nombre={self.__nombre}, edad={self.__edad})"

    def __len__(self) -> int:
        # Ejemplo: longitud del nombre
        return len(self.__nombre)

    # Método de ejemplo
    def hablar(self) -> None:
        print(f"Hola, mi nombre es {self.__nombre} y tengo {self.__edad} años.")


class Mascota:
    def __init__(self, nombre: str, tipo: str):
        self.__nombre = nombre
        self.__tipo = tipo

    # --- getters ---
    def get_nombre(self) -> str:
        return self.__nombre

    def get_tipo(self) -> str:
        return self.__tipo

    # --- setters ---
    def set_nombre(self, nombre: str) -> None:
        self.__nombre = nombre

    def set_tipo(self, tipo: str) -> None:
        self.__tipo = tipo

    # --- dunder methods ---
    def __str__(self) -> str:
        return f"Mascota(nombre={self.__nombre}, tipo={self.__tipo})"

    def __len__(self) -> int:
        # Ejemplo: longitud del nombre de la mascota
        return len(self.__nombre)

    def hablar(self) -> None:
        print(f"Soy {self.__nombre} y soy una {self.__tipo}.")


class Vehiculo:
    def __init__(self, marca: str, modelo: str, propietario=None):
        self.__marca = marca
        self.__modelo = modelo
        self.__propietario = propietario  # ASOCIACIÓN: referencia a Persona, pero no es parte de su vida (pueden existir por separado)

    # --- getters ---
    def get_marca(self) -> str:
        return self.__marca

    def get_modelo(self) -> str:
        return self.__modelo

    def get_propietario(self):
        return self.__propietario

    # --- setters ---
    def set_marca(self, marca: str) -> None:
        self.__marca = marca

    def set_modelo(self, modelo: str) -> None:
        self.__modelo = modelo

    def set_propietario(self, propietario) -> None:
        self.__propietario = propietario

    # --- dunder methods ---
    def __str__(self) -> str:
        if self.__propietario is None:
            return f"Vehiculo(marca={self.__marca}, modelo={self.__modelo}, propietario=None)"
        return f"Vehiculo(marca={self.__marca}, modelo={self.__modelo}, propietario={self.__propietario.get_nombre()})"

    def __len__(self) -> int:
        # Ejemplo: suma de longitudes de marca y modelo
        return len(self.__marca) + len(self.__modelo)

    def info(self) -> None:
        if self.__propietario:
            print(f"Este vehículo es un {self.__marca} {self.__modelo} y su dueño es {self.__propietario.get_nombre()}.")
        else:
            print(f"Este vehículo es un {self.__marca} {self.__modelo}.")


# COMPOSICIÓN: una Persona "posee" mascotas (vidas dependientes del dueño dentro del objeto)
class PersonaConMascotas:
    def __init__(self, nombre: str, edad: int):
        self.__persona = Persona(nombre, edad)
        self.__mascotas = []  # composición: se crean/guardan dentro del dueño

    # getters
    def get_persona(self) -> Persona:
        return self.__persona

    def get_mascotas(self) -> list:
        return self.__mascotas

    # acción (composición)
    def agregar_mascota(self, nombre: str, tipo: str) -> None:
        # La mascota se crea dentro: composición
        self.__mascotas.append(Mascota(nombre, tipo))

    def __str__(self) -> str:
        return f"{self.__persona} | Mascotas={len(self.__mascotas)}"

    def __len__(self) -> int:
        # Ejemplo: cantidad de mascotas
        return len(self.__mascotas)


# EJEMPLOS DE USO
if __name__ == "__main__":
    # 1) Ejemplo normal
    p1 = Persona("Carlos", 20)
    print(str(p1))
    print("len(Persona) =", len(p1))
    p1.hablar()

    print()

    # 2) COMPOSICIÓN (PersonaConMascotas crea Mascota dentro)
    dueño = PersonaConMascotas("Ana", 25)
    dueño.agregar_mascota("Luna", "gato")
    dueño.agregar_mascota("Max", "perro")

    print(str(dueño))
    print("len(PersonaConMascotas) =", len(dueño))
    for m in dueño.get_mascotas():
        print(str(m), "| len(Mascota) =", len(m))

    print()

    # 3) ASOCIACIÓN (Vehiculo referencia a Persona, pero ambos pueden existir por separado)
    v1 = Vehiculo("Toyota", "Corolla")       # vehículo sin dueño aún
    v1.set_propietario(p1)                  # asociación: se enlaza después

    print(str(v1))
    print("len(Vehiculo) =", len(v1))
    v1.info()