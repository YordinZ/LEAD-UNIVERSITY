from persona import Persona
class Carro:
    def __init__(self, marca: str, modelo: str, color: str,  kilometraje: int, dueno: Persona):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.dueno = dueno
        self.encendido = False
        self.kilometraje = kilometraje

    def encender(self):
        self.encendido = True
        print("El carro está encendido")

    def apagar(self):
        self.encendido = False
        print("El carro está apagado")

    def describir(self):
        print(
            "Carro:", self.marca,
            self.modelo,
            "- Color:", self.color,
            "- Dueño:", self.dueno.nombre
        )
    def __len__(self):
        return self.kilometraje
    
    def __str__(self):
        return (
            f"Vehículo {self.marca} {self.modelo} | "
            f"Color: {self.color} | "
            f"Dueño: {self.dueno.nombre} | "
            f"Kilometraje: {self.kilometraje} km | "
            f"Encendido: {'Sí' if self.encendido else 'No'}"
        )

    def __repr__(self):
        return (
            f"Vehiculo(marca='{self.marca}', "
            f"modelo='{self.modelo}', "
            f"color='{self.color}', "
            f"dueno={repr(self.dueno)}, "
            f"kilometraje={self.kilometraje}, "
            f"encendido={self.encendido})"
        )