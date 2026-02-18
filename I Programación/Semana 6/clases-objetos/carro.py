class Carro:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.encendido = False

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
            "- Color:", self.color
        )
