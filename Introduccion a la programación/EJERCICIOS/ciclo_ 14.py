saludos = {
    1: "¡Hola! 😊",
    2: "¡Buenos días! ☀️",
    3: "¡Buenas tardes! 🌅", 
    4: "¡Buenas noches! 🌙",
    5: "¡Adiós! 😴"
}

while True:
    print("\nOpciones: 1-Hola, 2-Buenos días, 3-Buenas tardes, 4-Buenas noches, 5-¿Cómo estás?, 0-Salir")
    
    opcion = int(input("Seleccione una opción: "))
    
    if opcion == 0:
        print("¡Programa terminado!")
        break
    elif opcion in saludos:
        print(saludos[opcion])
    else:
        print("Opción desconocida!")