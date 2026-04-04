edad = input("Digite la edad")

#Incorrecto
if edad >= 18 and tiene_licencia and no_tiene_multas and paso_examen_teorico and paso_examen_practico:
    print("Puede conducir")


#Correcto
if (
    edad >= 18
    and tiene_licencia
    and no_tiene_multas
    and paso_examen_teorico
    and paso_examen_practico
):
    print("Puede conducir")