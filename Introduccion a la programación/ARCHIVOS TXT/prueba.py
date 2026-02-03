'''
OPEN (RUTA. MODO) dos parametros

1. Ruta del archivo= ruta/nombre_archivo.txt
2. Modo de apertura:
'r'= leer, valor por defecto (Si el archivo no existe da error)
'a'= agregar, si el archivo no exite lo crea, agregar los datos
'w'= escribir, si el archivo existe lo sobre escribe, sino existe lo crea
'x'= crear, crea un archivo nuevo
'''

# Escritura del archivo
with open('archivo.txt', 'w') as archivo:
    archivo.write('1\n')
    archivo.write('18\n')

    lista = ['Alajuela\n', 'Cartago\n', 'Heredia\n', 'Puntarenas\n']
    archivo.writelines(lista)

# Lectura y separación por líneas
with open('archivo.txt', 'r') as archivo:
    contenido_archivo = archivo.read()

lista_provincias = contenido_archivo.splitlines()
print(lista_provincias)