registro_usuarios = {
    'Juan': {
        'edad': 25,
        'libros_prestados': ['Cien años de soledad', '1984']
    },
    'María': {
        'edad': 30,
        'libros_prestados': ['Don Quijote de la Mancha', 'El señor de los anillos']
    },
    'Carlos': {
        'edad': 20,
        'libros_prestados': ['Orgullo y prejuicio', 'El hobbit']
    }
}

precios_libros = {
    'Cien años de soledad': 15,
    '1984': 12,
    'Don Quijote de la Mancha': 20,
    'El señor de los anillos': 25,
    'Orgullo y prejuicio': 10,
    'El hobbit': 18
}


def calcular_valor_prestamos(registro_usuarios, precios_libros):
    total= 0

    for usuario, datos in registro_usuarios.items():
        libros= datos['libros_prestados']
        for libro in libros:
            if libro in precios_libros:
                total+= precios_libros[libro]
            
            else:
                print(f'Advertencia: No hay precio registrado para {libro}')
    return total

def usuario_con_mas_libros(registro_usuarios):
    usuario_max = None
    cantidad_max = 0

    for usuario, datos in registro_usuarios.items():
        cantidad_libros = len(datos['libros_prestados'])

        if cantidad_libros > cantidad_max:
            cantidad_max = cantidad_libros
            usuario_max = usuario

    return usuario_max

def agregar_libro_usuario(registro_usuarios, nombre_usuario, nombre_libro):
    if nombre_usuario in registro_usuarios:
        registro_usuarios[nombre_usuario]['libros_prestados'].append(nombre_libro)
    else:
        print(f"El usuario '{nombre_usuario}' no existe en el registro.")


if __name__ == '__main__':
    resultado = calcular_valor_prestamos(registro_usuarios, precios_libros)
    print(resultado)
