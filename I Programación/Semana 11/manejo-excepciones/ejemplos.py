
#Manejo general de excepciones
try:
    numero = int(input("Digite un número: "))
    print(10 / numero)
except:
    print("Ocurrió un error")


#Manejar múltiples Excepciones
try:
    numero = int(input("Digite un número: "))
    print(10 / numero)

except ZeroDivisionError:
    print("No se puede dividir entre cero")

except ValueError:
    print("Debe digitar un número")    