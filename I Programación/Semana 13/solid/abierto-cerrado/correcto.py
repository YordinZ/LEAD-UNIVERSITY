class Descuento:
    def calcular(self, total):
        pass


class DescuentoRegular(Descuento):
    def calcular(self, total):
        return total * 0.05


class DescuentoVIP(Descuento):
    def calcular(self, total):
        return total * 0.10


class DescuentoPremium(Descuento):
    def calcular(self, total):
        return total * 0.15

# Si quieres agregar otro descuento, creas otra clase:
# class DescuentoEstudiante(Descuento):
#     def calcular(self, total):
#         return total * 0.08

cliente = DescuentoVIP()
print(cliente.calcular(1000))