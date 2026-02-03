numeros = [6,5,3,8,4,2,5,4,11]

sumatoria = 0

for valor in numeros:
    if valor % 2 == 0:
        sumatoria = sumatoria + valor  #sumatoria += valor

print(f"La sumatoria es {sumatoria}")
print("La sumatoria es", sumatoria)