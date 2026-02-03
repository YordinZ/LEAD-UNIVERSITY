# Cambiar mayúsculas por minúsculas
texto = "Hola Mundo"
print(texto.upper())

# Reemplazar texto
print ("Hola mundo".replace("mundo", "Python"))

# Buscar texto
programacion = "programacion"

indice = programacion.find("gra")   
print("Índice: ", indice)

# Dividir por texto
frase = "Python es facil"
lista = frase.split(" ")
print("Lista:", lista)

# Recorrer letra por letra
letras = "Hola"

for letra in letras:
    print(letra)

# Recorrer por posición
for i in range(len(letras)):
    print(letras[i])


# Ejemplo de f strings
nombre = "Clara"
edad = 20

mensaje = f"Hola {nombre}, tienes {edad} años"
print (mensaje)