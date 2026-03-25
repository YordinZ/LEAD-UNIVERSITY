from libro import Libro
from calculadora import Calculadora
def principal():
    # Ejemplo métodos clase
    l1 = Libro("Harry Potter y la piedra filosofal")
    l2 = Libro("El Señor de los anillos: La comunidad del anillo")
    l3 = Libro("El arte de la guerra")

    Libro.mostrar_cantidad()

    #Ejemplo métodos estático
    
    print("Suma 4 + 3 = ", Calculadora.sumar(4, 3))
    print("División 6 / 2 = ", Calculadora.dividir(6, 2))


    Calculadora.sumar(4, 3)



if __name__ == "__main__":
    principal()