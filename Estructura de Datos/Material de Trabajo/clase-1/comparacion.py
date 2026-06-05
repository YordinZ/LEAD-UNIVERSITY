import time

numeros = list(range(1000000))

inicio = time.time()

999999 in numeros

fin = time.time()

print(fin - inicio)


# otra forma de hacerlo
numeros_set = set(numeros)

inicio = time.time()

999999 in numeros_set

fin = time.time()

print(fin - inicio)