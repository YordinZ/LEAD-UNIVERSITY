# Ejercicio 1
frutas = [ 
{'nombre': 'manzana', 'color': 'rojo'}, 
{'nombre': 'banano', 'color': 'amarillo'}, 
{'nombre': 'uva', 'color': 'morado'}, 
{'nombre': 'fresa', 'color': 'rojo'}, 
{'nombre': 'melocoton', 'color': 'naranja'}, 
{'nombre': 'mango', 'color': 'verde'}, 
{'nombre': 'pera', 'color': 'verde'}, 
{'nombre': 'coco', 'color': 'cafe'}, 
{'nombre': 'piña', 'color': 'amarillo'}, 
{'nombre': 'kiwi', 'color': 'verde'} 
] 

"""
    nombres= [] #lista vacia

    for fruta in frutas:
        nombres.append(fruta['nombre']) 
"""
def obtener_nombres(frutas):
    return [fruta['nombre'] for fruta in frutas]

def guardar_frutas(frutas, ruta= 'frutas.txt'):
    with open(ruta, 'w', encoding='utf-8') as archivo:
        archivo.write('NOMBRE - COLOR\n')
        
        for fruta in frutas:
            archivo.write(f"{fruta['nombre']} - {fruta['color']}\n")

print(obtener_nombres(frutas))
guardar_frutas(frutas, 'frutas.txt')

# Ejercicio 2
precios = { 
'agua': 1.00, 
'galleta': 0.75, 
'juguito': 1.50 
} 

carrito = { 
'agua': 2, 
'galleta': 3 
} 

def calcular_total(carrito, precios):
    resultado= 0

    for producto, cantidad in carrito.items(): #clave = producto, valor = cantidad
        precio= precios[producto]
        resultado+= precio * cantidad
    return resultado

def guardar_carrito(carrito, precios, ruta= 'carrito.txt'):
    resultado= 0

    with open(ruta, 'w', encoding='utf-8') as archivo:
        for producto, cantidad in carrito.items(): 
            precio= precios.get(producto)
            subtotal= precio * cantidad
            resultado+= subtotal
            
            archivo.write(f'{producto}, {cantidad}, {subtotal}\n')
        archivo.write(f'Resultado: {resultado}\n')
    return resultado
print(calcular_total(carrito, precios))
guardar_carrito(carrito, precios, 'carrito.txt')