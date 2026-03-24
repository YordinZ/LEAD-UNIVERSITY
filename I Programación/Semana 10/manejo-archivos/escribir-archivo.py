
personajes = ["Yuji", "Gojo", "Sukuna", "Maki", "Fushiguro", "Nobara", "Yuta"]

# escribir un nuevo archivo
with open("output/personajes-jujutsu.txt", "w") as archivo:
    for n in personajes:
        archivo.write(n + "\n")


nakamas = ["Zoro", "Nami", "Sanji", "Usopp", "Robin", "Chopper", "Franky", "Brook", "Jinbe"]
# modificar un archivo existinte
with open("output/nakamas.txt", "a") as archivo:
    for nakama in nakamas:
        archivo.write("\n"  + nakama )