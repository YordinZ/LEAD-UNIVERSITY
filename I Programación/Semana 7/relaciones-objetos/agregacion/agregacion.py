from estudiante import Estudiante
from universidad import Universidad
def main():
   
    frodo = Estudiante("Frodo Bolsón")
    sam = Estudiante("Samwise Gamyi")
    merry = Estudiante("Meriadoc Brandigamo")
    pippin = Estudiante("Peregrin Tuk")
    bilbo = Estudiante("Bilbo Bolsón")

   
    u_mordor = Universidad()
    u_minastirith = Universidad()
    u_lacomarca = Universidad()

   
    u_lacomarca.agregar_estudiante(frodo)
    u_lacomarca.agregar_estudiante(sam)
    u_lacomarca.agregar_estudiante(bilbo)
    u_lacomarca.agregar_estudiante(merry)
    u_lacomarca.agregar_estudiante(pippin)

    u_minastirith.agregar_estudiante(merry)
    u_minastirith.agregar_estudiante(pippin)

    u_mordor.agregar_estudiante(
        Estudiante("Gollum (no es hobbit, pero insistió)")
    )

    
    print("🏡 Universidad de La Comarca")
    print(u_lacomarca)

    print("🏰 Universidad de Minas Tirith")
    print(u_minastirith)

    print("🔥 Universidad de Mordor")
    print(u_mordor)

main()