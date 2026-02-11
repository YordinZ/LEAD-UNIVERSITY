# main.py
import cilindro as cld
import cono as cn
import cubo as cb
import esfera as ef
import paralelepipedo as plp

def main():
    print(".....Calculadora de volúmenes.....")
    print("1. Cilindro")
    print("2. Cono")
    print("3. Cubo")
    print("4. Esfera")
    print("5. Paralelepípedo")

    opcion = int(input("\nSeleccione una figura: "))

    if opcion == 1:
        cld.calcular_volumen_cilindro()
    elif opcion == 2:
        cn.calcular_volumen_cono()
    elif opcion == 3:
        cb.calcular_volumen_cubo()
    elif opcion == 4:
        ef.calcular_volumen_esfera()
    elif opcion == 5:
        plp.calcular_volumen_paralelepipedo()
    else:
        print("Opción inválida")

if __name__ == "__main__":
    main()