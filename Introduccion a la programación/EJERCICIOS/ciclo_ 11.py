num = int(input('Introduzca un numero: '))
pasos = 0

print(f"Secuencia para el número {num}:")

while num != 1:
    pasos += 1
    
    if num % 2 == 0:
        resultado = num // 2
        print(f"Paso {pasos}: {num} es par → {num} / 2 = {resultado}")
    
    else:
        resultado = (num * 3) + 1
        print(f"Paso {pasos}: {num} es impar → ({num} * 3) + 1 = {resultado}")
    
    num = resultado

print(f"\n¡Se llegó a 1 en {pasos} pasos!")