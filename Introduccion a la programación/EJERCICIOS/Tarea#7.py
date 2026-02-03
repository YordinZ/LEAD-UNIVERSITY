angulo1 = float(input("Ingrese el primer ángulo: "))
angulo2 = float(input("Ingrese el segundo ángulo: "))
angulo3 = float(input("Ingrese el tercer ángulo: "))

# Verificar si la suma es 180°
suma_angulos = angulo1 + angulo2 + angulo3

if suma_angulos == 180:
    print("SI se puede formar un triángulo con estos ángulos")
else:
    print("NO se puede formar un triángulo con estos ángulos")
    print(f"La suma de los ángulos es {suma_angulos}°, pero debe ser 180°")