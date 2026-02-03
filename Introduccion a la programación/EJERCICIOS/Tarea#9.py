PRECIO_LIBRO = 20

def calcular_compra_libros(cantidad):
    """Calcula toda la compra en una función"""
    if cantidad < 0:
        return "Error: Cantidad no válida"
    
    # Determinar descuento
    if cantidad > 30:
        descuento = 40
    elif cantidad > 20:
        descuento = 20
    elif cantidad > 10:
        descuento = 10
    else:
        descuento = 0
    
    # Cálculos
    subtotal = cantidad * PRECIO_LIBRO
    monto_descuento = subtotal * descuento / 100
    total = subtotal - monto_descuento
    
    return f"""
Libros: {cantidad}
Subtotal: ${subtotal:.2f}
Descuento: {descuento}%
Ahorro: ${monto_descuento:.2f}
TOTAL: ${total:.2f}
"""

# Uso simple
try:
    cant = int(input("Cantidad de libros: "))
    print(calcular_compra_libros(cant))
except:
    print("Error en la entrada")