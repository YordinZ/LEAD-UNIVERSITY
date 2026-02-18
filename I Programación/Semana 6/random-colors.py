import random
import string


letra = random.choice(string.ascii_lowercase)
print("\033[32m"+ letra +"\033[0m")
print(letra)

letra = random.choice(string.ascii_lowercase)
print(letra)
print("\033[31m" +letra +"\033[0m")

print("\033[31mEsto imprime en rojo\033[0m")
print("\033[32mEsto imprime en verde\033[0m")
print("\033[34mEsto imprime en azul\033[0m")