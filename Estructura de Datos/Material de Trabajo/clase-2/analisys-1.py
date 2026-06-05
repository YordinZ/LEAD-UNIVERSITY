n = int(input("Ingrese el número de iteraciones: "))

suma = 0
producto = 1

for i in range(1, n + 1):
    suma += i
    producto *= i
    print(f"Iteración {i}: suma parcial = {suma}, producto parcial = {producto}")

print(f"Total de iteraciones: {n}")
print(f"Suma total: {suma}")
print(f"Producto total: {producto}")
