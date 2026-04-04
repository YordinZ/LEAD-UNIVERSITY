
edad = input ("Ingrese la edad")

if edad < 0:
    raise ValueError("La edad no puede ser negativa")


# Se puede usar dentro de un try Except
try:
    numero = int(input("Número: "))
    if numero < 0:
        raise ValueError("No se permiten negativos")
except ValueError as e:
    print("Error:", e)

#También se puede volver a lanzar una excepción para que sea atajada más adelante
try:
    x = int("abc")
except ValueError:
    print("Hubo un error")
    raise  # vuelve a lanzar el mismo error