import os
# personajes = [
#     "Ryu,90,85,80",
#     "Ken,88,82,78",
#     "ChunLi,80,95,85",
#     "Guile,85,88,84",
#     "Zangief,95,70,92"
# ]
# os.makedirs("output", exist_ok=True)
# with open("output/fighters.dat", "wb") as f:
#     for p in personajes:
#         registro = p.ljust(32)  # tamaño fijo 32 bytes
#         f.write(registro.encode("utf-8"))

TAM = 32

indice = 0  # ChunLi

with open("output/fighters.dat", "rb") as f:
    f.seek(indice * TAM)
    data = f.read(TAM)

print(data.decode().strip())