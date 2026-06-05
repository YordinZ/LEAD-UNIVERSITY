# busqueda binaria tiempo O(log n)
def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if lista[medio] == objetivo:
            return True
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return False


numeros = [1, 3, 5, 7, 9, 11, 13, 15]

print(busqueda_binaria(numeros, 11))