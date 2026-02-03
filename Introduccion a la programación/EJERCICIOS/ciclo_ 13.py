# Leer el número de bloques
bloques = int(input('Introduzca el número de bloques: '))

# Validar que sea positivo
if bloques <= 0:
    print("El número debe ser positivo")
else:
    # Encontrar el máximo número de pisos completos
    pisos = 0
    suma = 0
    
    # Ir sumando pisos hasta que no quepan más bloques
    while suma + (pisos + 1) <= bloques:
        pisos += 1
        suma += pisos
    
    print(f"Con {bloques} bloques puedes construir {pisos} pisos completos")
    print(f"Distribución: {'-'.join(str(i) for i in range(pisos, 0, -1))}")
    print(f"Bloques usados: {suma}")
    print(f"Bloques sobrantes: {bloques - suma}")