serie= input('Serie de numeros: ').split(',')
serie= [int(numero.strip()) for numero in serie] #Convierto en una serie de lista de Python

ance= True
desc= True

for serie2 in range(1, len(serie)):
    if serie[serie2] < serie[serie2-1]:
        ance= False 
    