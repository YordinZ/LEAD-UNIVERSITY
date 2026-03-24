texto = "Hola"

for c in texto:
    print(c, ord(c)) # devuelve el código ASCII

print(chr(65)) #convierte de ascii a caracter


text = "Hello"

with open("output/ascii-file.txt", "w", encoding="ascii") as f:
    f.write(text)
    # f.write("Cañón") # falla porque ñ y ó no están disponibles en ascii