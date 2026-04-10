from descuento_adulto_mayor import DescuentoAdultoMayor
from descuento_estudiante import DescuentoEstudiante
from descuento_normal import DescuentoNormal
# Contexto
class Compra:
    def __init__(self, total, estrategia):
        self.total = total
        self.estrategia = estrategia

    def calcular_total(self):
        return self.estrategia.aplicar_descuento(self.total)

# Uso
compra1 = Compra(100, DescuentoNormal())
compra2 = Compra(100, DescuentoEstudiante())
compra3 = Compra(100, DescuentoAdultoMayor())

print("Normal:", compra1.calcular_total())
print("Estudiante:", compra2.calcular_total())
print("Adulto mayor:", compra3.calcular_total())