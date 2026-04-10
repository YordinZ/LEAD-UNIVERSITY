from estrategia_descuento import EstrategiaDescuento
class DescuentoEstudiante(EstrategiaDescuento):
    def aplicar_descuento(self, total):
        return total * 0.9