PI= 3.1416

def volumen_esfera(radio):
    return (4/3) * PI * radio**3 #V=3/4​πr3

def calcular_volumen_esfera():
    radio = float(input("Ingrese el radio de la esfera: "))
    volumen = (4/3) * PI * radio**3
    print(f"El volumen de la esfera es: {volumen:.2f}")