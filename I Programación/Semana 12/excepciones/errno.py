import errno
try:
    archivo = open("datos.txt")
except OSError as e:
    if e.errno == 2:
        print("El archivo no existe")
    elif e.errno == 13:
        print("No tienes permisos")
    else:
        print("Error desconocido:", e.errno)


try:
    open("datos.txt")
except OSError as e:
    if e.errno == errno.ENOENT:
        print("Archivo no encontrado")