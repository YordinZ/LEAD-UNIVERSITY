# FORMULA: m = (y₂ - y₁) / (x₂ - x₁)
x1 = float(input('Introduzca x del I punto: '))
y1 = float(input('Introduzca y del I punto: '))

x2 = float(input('Introduzca x del II punto: '))
y2 = float(input('Introduzca y del II punto: '))

# Verificar si la recta es vertical
if x2 - x1 == 0:
    print(f'La recta que pasa por ({x1},{y1}) y ({x2},{y2}) es VERTICAL (pendiente indefinida)')
else:
    pendiente = (y2 - y1) / (x2 - x1)
    print(f'La pendiente de la recta que pasa por ({x1},{y1}) y ({x2},{y2}) es: {pendiente:.2f}')