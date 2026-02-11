PI= 3.1416

def volumen_paralelepipedo(largo, ancho, altura):
    return largo * ancho * altura #V=l*a*h

def calcular_volumen_paralelepipedo():
    largo = float(input("Ingrese el largo del paralelepipedo: "))
    ancho = float(input("Ingrese el ancho del paralelepipedo: "))
    altura = float(input("Ingrese la altura del paralelepipedo: "))
    volumen = volumen_paralelepipedo(largo, ancho, altura)
    print(f"El volumen del paralelepipedo es: {volumen:.2f}")