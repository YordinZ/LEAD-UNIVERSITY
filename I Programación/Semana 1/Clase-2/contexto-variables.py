# Variable con contexto local. nombre no puede usarse fuera de imprimir_nombre
def imprimir_nombre():
    nombre = "Pedro"
    print(nombre)

# Esto ocasiona un error debido a que pedro no está definido fuera de la función imprimir_nombre
# print(nombre)

# Variable con contexto enclosing
def funcion_externa():
    mensaje = "Hola"   

    def funcion_interna():
        print(mensaje)  

    funcion_interna()

#Llamado a función externa
funcion_externa()

# Ejemplo nonlocal
def crear_contador():
    total = 0

    def incrementar():
        nonlocal total 
        total += 1 #sin el nonlocal no se puede hacer esta asignación
        return total
    return incrementar

contador = crear_contador()
print (contador())
print (contador())


# Variable global
numero = 10
def mostrar():
    print(numero)

mostrar()

# variable global
nuevo_contador = 0

def incrementar_nuevo():
    global nuevo_contador
    nuevo_contador += 1

incrementar_nuevo()
print(nuevo_contador)

# Ejemplo de built-in print y len son funciones built-in
print(len("Hola"))