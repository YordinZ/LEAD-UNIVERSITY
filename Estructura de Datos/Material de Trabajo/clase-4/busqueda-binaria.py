def busqueda_binaria(lista, valor):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2

        if lista[medio] == valor:
            return medio
        elif valor < lista[medio]:
            fin = medio - 1
        else:
            inicio = medio + 1

    return -1