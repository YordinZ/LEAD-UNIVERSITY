''' 
#Ejercicio 1
numbers = [10, 12,13, 16, 20, 
21, 26, 39, 40,49,50,54,56,70,94,57, 120, 230] 

for x in numbers:
    if x <100:
        print(x)

#Ejercicio 2
edadxperro= int(input('Ingrese la edad de su perro en años humanos: '))
perro= 10.5
perrov2= 4

if edadxperro <=2:
    print(f'Su perro tiene {perro*edadxperro} años en años perro')

else:
    # Para más de 2 años: 2 años × 10.5 - años restantes × 4
    anos_perro = (2 * perro) + ((edadxperro - 2) * perrov2)
    print(f'Su perro tiene {anos_perro} años en años perro')

#Ejercicio 3
numeros = [100, 2, 6, 79, 24, 12, 157, 7, 1, 6, 8, 2, 7, 9]
mayor = numeros[0]
for num in numeros:
    if num > mayor:
        mayor = num  
print("Número mayor:", mayor)
'''
#Ejercicio 6
palabras= []

while True:
    text = input('Ingrese una frase: ')
    
    if text.lower() == 'stop':
        break  #CERRAR
    else:
        palabras.append(text) #AGREGA A LA LISTA!

print(','.join(palabras)) #Une todas las palabras con comas