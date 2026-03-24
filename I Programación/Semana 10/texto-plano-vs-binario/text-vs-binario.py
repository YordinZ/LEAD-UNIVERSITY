print("======================================")

# Lectura de archivo de texto
with open("data/mangas-vendidos.csv", "r") as mangas:
    texto = mangas.readline()
    print(texto)
 

print("======================================")

# Lectura de archivo de binario
with open("data/Shonen-Jump-Series.jpeg", "rb") as shonen:
    texto = shonen.readline()
    print(texto)
    #texto = jujutsu.readline()
    #print(texto)

print("======================================")
