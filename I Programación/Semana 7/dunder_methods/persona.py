class Persona:
    def __init__(self, nombre: str, edad: int, pais: str):
        self.nombre = nombre
        self.edad = edad
        self.pais = pais

    def presentarse(self):
        print(
            "Hola, mi nombre es", self.nombre,
            "tengo", self.edad, "años",
            "y soy de", self.pais
        )

    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False

    def es_costarricense(self):
        return self.pais == "Costa Rica"
    
    def __str__(self):
        return f"{self.nombre} ({self.edad} años) - País: {self.pais}"

    def __repr__(self):
        return (
            f"Persona(nombre='{self.nombre}', "
            f"edad={self.edad}, "
            f"pais='{self.pais}')"
        )

    def __len__(self):
        return self.edad