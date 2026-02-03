'''
return = devolver valores de la función (nos dan las papitas)
Permite devolver un valor de en la función
'''

def sumatoria_lista (lista_numeros):
    suma = 0
    for x in lista_numeros:
        suma = suma + x
    
    return suma

lista = [3,5,6,8,9]
resultado = sumatoria_lista(lista)

print(resultado)