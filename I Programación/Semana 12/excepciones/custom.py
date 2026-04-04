from edad_invalida import EdadInvalidaError
from saldo_insuficiente import SaldoInsuficienteError

edad = input("Inserte la edad: ")
if edad < 0:
    raise EdadInvalidaError(edad)


def retirar(saldo, monto):
    if monto > saldo:
        raise SaldoInsuficienteError("No tienes suficiente dinero")
    return saldo - monto


try:
    retirar(100, 200)
except SaldoInsuficienteError as e:
    print(e)