import os

def duplicar_archivo(nombre_entrada, nombre_salida):
    ruta_entrada = os.path.join("data", nombre_entrada) # os.path nos indica en que path se encuentra la ejecución
    ruta_salida = os.path.join("output", nombre_salida)

    try:
        with open(ruta_entrada, "rb") as archivo_entrada: #rb indica que va a leer bytes
            with open(ruta_salida, "wb") as archivo_salida: #wb indica que va a escribir bytes
                
                while True:
                    bloque = archivo_entrada.read(1024)  # read recibe cuantos bytes leer, esto nos permite leer en bloque
                    
                    if not bloque:
                        break
                    
                    archivo_salida.write(bloque)

        print("Archivo duplicado correctamente")

    except FileNotFoundError:
        print("Error: archivo de entrada no existe")

    except Exception as e:
        print("Error:", e)


def main():
    nombre_entrada = input("Nombre del archivo de entrada: ")
    nombre_salida = input("Nombre del archivo de salida: ")

    duplicar_archivo(nombre_entrada, nombre_salida)


if __name__ == "__main__":
    main()