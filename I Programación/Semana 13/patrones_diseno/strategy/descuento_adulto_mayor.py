from estrategia_descuento import EstrategiaDescuento
class DescuentoAdultoMayor(EstrategiaDescuento):
    def aplicar_descuento(self, total):
        return total * 0.8