PI= 3.1416

def volumen_cubo(lado):
    return lado**3 #V=a3

def calcular_volumen_cubo():
    lado = float(input("Ingrese el lado del cubo: "))
    volumen = volumen_cubo(lado)
    print(f"El volumen del cubo es: {volumen:.2f}")