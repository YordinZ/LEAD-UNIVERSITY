PI= 3.1416

def volumen_cono(radio, altura):
    return (PI * radio**2 * altura) / 3 #V=1/3​πr2h

def calcular_volumen_cono():
    radio = float(input("Ingrese el radio del cono: "))
    altura = float(input("Ingrese la altura del cono: "))
    volumen = volumen_cono(radio, altura)
    print(f"El volumen del cono es: {volumen:.2f}")