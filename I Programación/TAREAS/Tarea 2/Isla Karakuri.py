import base_de_datos as bd

def menu():
    print("\n.....Bienvenido a la Isla Karakuri.....")
    print("1. Agregar persona")
    print("2. Imprimir personas")
    print("3. Indicar la persona con mayor indice de masa corporal (IMC)")
    print("4. Calculo de la media del salario")
    print("5. Calculo de la varianza del salario")
    print("6. Calculo de la media de la altura")
    print("7. Encontrar la persona más alta")
    print("8. Encontrar la persona más pesada")
    print("9. Salir")


def calcular_media(lista_numeros):
    if len(lista_numeros) == 0:
        return None
    return sum(lista_numeros) / len(lista_numeros)


def calcular_varianza_muestral(lista_numeros):
    # Varianza muestral: sum((x - media)^2) / (n - 1)
    n = len(lista_numeros)
    if n < 2:
        return None
    media = calcular_media(lista_numeros)
    suma = 0
    for x in lista_numeros:
        suma += (x - media) ** 2
    return suma / (n - 1)


def calcular_imc(peso, altura):
    if altura <= 0: #fallar si altura es 0 o negativa
        return None
    return peso / (altura ** 2)


def pedir_float_positivo(mensaje): #VERIFICAR QUE EL NUMERO SEA POSITIVO
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                print("Debe ser mayor que 0.")
                continue
            return valor
        except ValueError:
            print("Debe ingresar un número válido.")


def pedir_float_no_negativo(mensaje): #VERIFICAR QUE EL NUMERO SEA NO NEGATIVO
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("No puede ser negativo.")
                continue
            return valor
        except ValueError:
            print("Debe ingresar un número válido.")


def agregar_persona():
    identificacion = input("Identificación: ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")

    edad = pedir_float_positivo("Edad: ")
    salario = pedir_float_no_negativo("Salario: ")

    ocupacion = input("Ocupación: ")
    altura = pedir_float_positivo("Altura (m): ")
    peso = pedir_float_positivo("Peso (kg): ")

    persona = {
        "identificacion": identificacion,
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "salario": salario,
        "ocupacion": ocupacion,
        "altura": altura,
        "peso": peso
    }

    bd.personas.append(persona)
    print("Persona agregada correctamente.")


def imprimir_personas():
    if len(bd.personas) == 0:
        print("No hay personas registradas.")
        return

    for p in bd.personas:
        print(
            f'{p["identificacion"]} | {p["nombre"]} {p["apellido"]} | '
            f'Edad: {p["edad"]} | Salario: {p["salario"]} | Ocupación: {p["ocupacion"]} | '
            f'Altura: {p["altura"]} | Peso: {p["peso"]}'
        )


def persona_mayor_imc():
    if len(bd.personas) == 0:
        print("No hay personas registradas.")
        return

    mayor = max(bd.personas, key=lambda p: calcular_imc(p["peso"], p["altura"]))
    imc_mayor = calcular_imc(mayor["peso"], mayor["altura"])
    print(f'Persona con mayor IMC: {mayor["nombre"]} {mayor["apellido"]} (IMC={imc_mayor:.2f})')


def media_salario():
    if len(bd.personas) == 0:
        print("No hay personas registradas.")
        return

    salarios = [p["salario"] for p in bd.personas]
    media = calcular_media(salarios)
    print(f"Media del salario: {media:.2f}")


def varianza_salario():
    if len(bd.personas) < 2:
        print("Se necesitan al menos 2 personas.")
        return

    salarios = [p["salario"] for p in bd.personas]
    varianza = calcular_varianza_muestral(salarios)
    print(f"Varianza del salario: {varianza:.2f}")


def media_altura():
    if len(bd.personas) == 0:
        print("No hay personas registradas.")
        return

    alturas = [p["altura"] for p in bd.personas]
    media = calcular_media(alturas)
    print(f"Media de la altura: {media:.2f}")


def persona_mas_alta():
    if len(bd.personas) == 0:
        print("No hay personas registradas.")
        return

    mas_alta = max(bd.personas, key=lambda p: p["altura"])
    print(f'Persona más alta: {mas_alta["nombre"]} {mas_alta["apellido"]} ({mas_alta["altura"]} m)')


def persona_mas_pesada():
    if len(bd.personas) == 0:
        print("No hay personas registradas.")
        return

    mas_pesada = max(bd.personas, key=lambda p: p["peso"])
    print(f'Persona más pesada: {mas_pesada["nombre"]} {mas_pesada["apellido"]} ({mas_pesada["peso"]} kg)')


def main():
    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_persona()
        elif opcion == "2":
            imprimir_personas()
        elif opcion == "3":
            persona_mayor_imc()
        elif opcion == "4":
            media_salario()
        elif opcion == "5":
            varianza_salario()
        elif opcion == "6":
            media_altura()
        elif opcion == "7":
            persona_mas_alta()
        elif opcion == "8":
            persona_mas_pesada()
        elif opcion == "9":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
