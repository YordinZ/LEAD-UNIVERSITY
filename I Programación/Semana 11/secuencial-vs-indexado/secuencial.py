

def buscar(nombre):
    with open("data/secuencial.txt", "r", encoding="utf-8") as file:
        for line in file:
            persona = line.strip().split(",")
            if persona[0] == nombre:
                print("Encontrado:", persona)
                break

buscar("Pedro")