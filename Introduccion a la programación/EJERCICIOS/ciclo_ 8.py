num = int(input('Ingrese un número: '))
cont = 0
multiplos_de_3 = 0

while cont <= num:
    if cont % 3 == 0:  # Verificar si es múltiplo de 3
        multiplos_de_3 += 1
    cont += 1

print(f'Hay {multiplos_de_3} múltiplos de 3 entre 0 y {num}')