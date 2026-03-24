print("======================================")
# ejemplo leer todo el archivo
with open("data/jujutsu-kaisen.txt", "r") as jujutsu:
    texto = jujutsu.read()
    print(texto)


print("======================================")

# ejemplo leer solo la primera línea
with open("data/jujutsu-kaisen.txt", "r") as jujutsu:
    texto = jujutsu.readline()
    print(texto)
    #texto = jujutsu.readline()
    #print(texto)

print("======================================")


# ejemplo leer todas las líneas
with open("data/jujutsu-kaisen.txt", "r") as jujutsu:
    texto = jujutsu.readlines()
    print(texto)

print("======================================")