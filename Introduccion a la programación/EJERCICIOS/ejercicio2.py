#Fórmula del volumen de un cilindro: V = π × r² × h
diametro = float(input('Introduzca el diametro del cilindro: '))
altura = float(input('Introduzca la altura del cilindro: '))

# Calcular radio (diámetro / 2) y volumen
radio= diametro/2
volumen = 3.1416 * (radio ** 2) * altura

print(f'El volumen del cilindro es: {volumen:.2f}') #{volumen:.2f} simplifica para 2 digitos