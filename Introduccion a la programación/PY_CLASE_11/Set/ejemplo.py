'''
#Ejercicio 1
dic1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} 

suma= sum(dic1.values())
print(f'La suma de los elementos del diccionario es: {suma}')
'''
#Ejercicio 2
dic1= {0: 'pera', 1: 'uva', 2: 'fresa', 3: 'melón', 4: 'kiwi', 5: 'piña', 6: 
'banano', 7: 'limón', 8: 'manzana', 9: 'naranja', 10: 'mango' }

clave = int(input('Introduzca la clave: ')) 

if clave in dic1:
    dic1.pop(clave)
    print(f'Clave {clave} eliminada')
else:
    print(f'Clave {clave} no encontrada')

print(f' Diccionario actualizado: {dic1}')