#Ejercicio 1
"""
palabras= input('Ingrese una serie de palabras: ').split(',')
palabras= [palabra.strip() for palabra in palabras] # Eliminar espacios en blanco alrededor de las palabras 
#Remueve espacios #NO ES NECESARIO, SIMPLEMENTE ESTETICA
cont= 0
palabras_largas= [] #Almacena numeros que se repitan

for palabra in palabras:
    if len(palabra) > 5: #Devuelve de texto a numero
        cont+=1
        palabras_largas.append(palabra) # Agrega elementos a la lista

print('Palabras con más de 5 letras:', ', '.join(palabras_largas))
print('Resultado:', cont)


#Ejercicio 2
numeros= input('Ingrese una serie de numeros: ').split(',')
numeros= [int(numero.strip()) for numero in numeros] #Convierto en una serie de lista de Python

cuadrados= []
for numero in numeros:
    cuadrados.append(numero ** 2)   

# RESULTADO
print('Lista original:', numeros)
print('Resultado:', cuadrados)

#Ejercicio 3
numeros= input('Ingrese una serie de numeros: ').split(',')
numeros= [int(numero.strip()) for numero in numeros] #Convierto en una serie de lista de Python

ascedente= True
descendente= True

for i in range(1, len(numeros)):
    if numeros[i] < numeros[i-1]:
        ascedente= False
    
    elif numeros[i] > numeros[i-1]:
        descendente= False

print('Lista: ', numeros)
print('Resultado:', ascedente or descendente)
"""
#Ejercicio 4
numeros= input('Ingrese una serie de numeros: ').split(',')
numeros= [int(numero) for numero in numeros] #Convierto en una serie de lista de Python

num= int(input('Ingrese un numero: '))
resultado= numeros[:num] #Toma los primeros N de elementos
        
print('Lista original:', numeros)
print('N= ', num)
print('Resultado:', resultado)
