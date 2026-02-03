numero = int(input("Ingrese un número entero: "))

ultimo_digito = numero % 10  # obtiene el último número

if ultimo_digito == 4 or ultimo_digito == -4:
    print("El número termina en 4.")
else:
    print("El número no termina en 4.")