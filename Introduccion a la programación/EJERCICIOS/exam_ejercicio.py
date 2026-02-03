input('Introduzca su nombre: ')

nota1= float(input('Introduzca su I nota: '))
nota2= float(input('Introduzca su II nota: '))

promedio= (nota1 + nota2) / 2
if promedio >= 70:
    print(f'Usted esta Aprobado, su nota es {promedio}')

elif promedio >= 60 and promedio <= 69:
    print(f'Usted tiene que ir a Convocatoria, su nota es {promedio}')

else: 
    print(f'Usted esta Reprobado, su nota es {promedio}')