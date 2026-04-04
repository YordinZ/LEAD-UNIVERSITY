# Con Exception capturamos muchos tipos de errores
try:
    num = input("Ingrese un número: ")
    x = int(num)
    y = 5 / x
except Exception:
    print("Error general")

#si quiere ser más específico debo poner varios tipos de excepciones
try:
    x = int(input("Ingrese un número:"))
    print(10 / x)
except ValueError:
    print("Debes ingresar un número")
except ZeroDivisionError:
    print("No puedes dividir entre cero")


# siempre debo poner las más específicas de primero y de último las más generales
try:
    x = int(input("Ingrese un número:"))
    print(10 / x)
except Exception:
    print("Excepción general") # Exception es más general que ValueError y ZeroDivision, entonces solo se captura esta parte
except ValueError:
    print("Debes ingresar un número")
except ZeroDivisionError:
    print("No puedes dividir entre cero")