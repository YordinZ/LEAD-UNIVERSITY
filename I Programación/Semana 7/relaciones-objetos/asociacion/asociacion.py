from curso import Curso
from profesor import Profesor

def main():
    profesora = Profesor("Ada Lovelace")
    curso = Curso("Programación 1", profesora)

    print(curso)

main()
