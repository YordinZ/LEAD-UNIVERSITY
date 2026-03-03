def saludar(nombre):
    return f"Hola {nombre}"

def main():
    print("Bienvenido al programa")
    nombre = input("Digite su nombre: ")
    mensaje = saludar(nombre)
    print(mensaje)

# Punto de entrada del programa, no se ejecuta si se importa como módulo
if __name__ == "__main__":
    main()