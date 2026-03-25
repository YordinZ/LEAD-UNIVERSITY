PI = 3.1416

def volumen_cilindro(radio, altura):
    return PI * radio**2 * altura #V=πr2h

def calcular_volumen_cilindro():
    radio = float(input("Ingrese el radio del cilindro: "))
    altura = float(input("Ingrese la altura del cilindro: "))
    volumen = volumen_cilindro(radio, altura)
    print(f"El volumen del cilindro es: {volumen:.2f}")