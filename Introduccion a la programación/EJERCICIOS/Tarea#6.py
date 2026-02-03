temperatura= int(input('Ingrese la temperatura en grados: '))
if temperatura > 10:
    print('Hace mucho frio')

elif temperatura >= 10 and temperatura <= 15:
    print('Hace poco frio')

elif temperatura >= 16 and temperatura <= 24:
    print('Hace una temperatura normal')

elif temperatura >= 25 and temperatura <= 30: 
    print('Hace poco calor')

else:
    print('Hace mucho calor')