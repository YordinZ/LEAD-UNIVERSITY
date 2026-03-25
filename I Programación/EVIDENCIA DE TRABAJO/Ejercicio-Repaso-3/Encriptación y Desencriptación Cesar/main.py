import desencriptar_cesar as dc
import encriptacion_cesar as ec

def main():
    print(".....Encriptación y Desencriptación César.....")
    print("1. Encriptar")
    print("2. Desencriptar")

    opcion = int(input("\nSeleccione una opción: "))

    if opcion == 1:
        texto = input("Ingrese el texto a encriptar: ")
        n = int(input("Ingrese el número de desplazamiento: "))
        resultado = ec.encriptacion_cesar(texto, n)
        print(f"Texto encriptado: {resultado}")
    elif opcion == 2:
        texto = input("Ingrese el texto a desencriptar: ")
        n = int(input("Ingrese el número de desplazamiento: "))
        resultado = dc.desencriptar_cesar(texto, n)
        print(f"Texto desencriptado: {resultado}")
    else:
        print("Opción inválida")

if __name__ == "__main__":
    main()