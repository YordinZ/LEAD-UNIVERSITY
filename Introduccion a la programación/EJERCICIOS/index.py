"""
¿QUÉ ES INDEX()?
Index es un método para buscar un valor y que devuelva el indice
de ese elemento de la lista.
"""

productos = [
    'arroz',      # 0
    'zanahoria',  # 1
    'papa',       # 2
    'cebolla',    # 3
    'tomate',     # 4
    'pimiento',   # 5
    'ajo',        # 6
    'perejil',    # 7
    'pollo',      # 8
    'carne',      # 9
    'pescado',    # 10
    'huevos',     # 11
    'leche',      # 12
    'queso',      # 13
    'yogur',      # 14
    'pan',        # 15
    'harina',     # 16
    'azúcar',     # 17
    'aceite',     # 18
    'vinagre',    # 19
    'sal',        # 20
    'pimienta',   # 21
    'limón',      # 22
    'naranja',    # 23
    'manzana',    # 24
    'plátano',    # 25
    'fresa',      # 26
    'uva',        # 27
    'pasta',      # 28
    'atún'        # 29
]

producto_buscado = 'naranja'
indice = productos.index(producto_buscado) #productos_index= productos.index('zanahoria')
print(f"'{producto_buscado}' encontrado en el índice: {indice}")
