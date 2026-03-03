from persona import Persona

def main():
    andres = Persona("Andres", 20)
    luana = Persona("Luana", 36)
    imprimir_persona(andres)
    imprimir_persona(luana)
    luana.nombre = "Luana María"
    imprimir_persona(luana)

def imprimir_persona(individuo: Persona):
    print(f"Hola {individuo.nombre} su edad es {individuo.edad}")

if __name__ == "__main__":
    main()