class EdadInvalidaError(Exception):
    def __init__(self, edad):
        self.edad = edad
        super().__init__(f"Edad inválida: {edad}")