# Cada instrucción individual vale: 1
a = b + c        # 1
mostrarMenu()    # 1
x = x + 1        # 1


#Bloques de código - La suma de todas sus instrucciones
a = b + c        # 1
mostrarMenu()    # 1
x = x + 1        # 1
# 1+1+1=3

# Un IF vale: El costo de evaluar la condición + El costo del cuerpo del IF
if variable > limite:   # 1
    a = b + c           # 1
    mostrarMenu()       # 1

# 1+1+1=3

# El costo de un ciclo se calcula como: 
# (Costo del bloque interno) × (Cantidad de iteraciones)
for variable in range(n):   # n veces
    a = b + c               # 1
    mostrarMenu()           # 1
# n × (1 + 1) = 2n

