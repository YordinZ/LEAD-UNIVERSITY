personas= []
mascotas = []
vehiculos = []

def menu():
    while True:
        print("\n..... MENÚ .....")
        print("1. Crear persona")
        print("2. Crear mascota")
        print("3. Crear vehículo")
        print("4. Imprimir personas")
        print("5. Imprimir mascotas")
        print("6. Imprimir vehículos")
        print("7. Imprimir todas las entidades")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            edad = input("Edad: ")
            persona = Persona(nombre, edad)
            personas.append(persona)
            print("Persona creada correctamente.")

        elif opcion == "2":
            nombre = input("Nombre del dueño: ")
            tipo = input("Tipo de mascota: ")
            mascota = Mascota(nombre, tipo)
            mascotas.append(mascota)
            print("Mascota creada correctamente.")

        elif opcion == "3":
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            vehiculo = Vehiculo(marca, modelo)
            vehiculos.append(vehiculo)
            print("Vehículo creado correctamente.")

        elif opcion == "4":
            for p in personas:
                p.hablar()

        elif opcion == "5":
            for m in mascotas:
                m.hablar()

        elif opcion == "6":
            for v in vehiculos:
                v.info()

        elif opcion == "7":
            for p in personas:
                p.hablar()
            for m in mascotas:
                m.hablar()
            for v in vehiculos:
                v.info()

        elif opcion == "8":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hablar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")
    
class Mascota:
    def __init__(self, nombre_propietario, tipo):
        self.nombre_propietario = nombre_propietario
        self.tipo = tipo

    def hablar(self):
        print(f"Hola, soy una {self.tipo} y mi dueño es {self.nombre_propietario}.")

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def info(self):
        print(f"Este vehículo es un {self.marca} {self.modelo}.")

menu()
