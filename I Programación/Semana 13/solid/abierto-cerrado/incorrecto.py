#Ejemplo incorrecto cada vez que agregamos un cliente nuevo hay que modificar la clase
class CalculadoraDescuento:
    def calcular(self, tipo_cliente, total):
        if tipo_cliente == "regular":
            return total * 0.05
        elif tipo_cliente == "vip":
            return total * 0.10
        elif tipo_cliente == "premium":
            return total * 0.15