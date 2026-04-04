import random
import os


# ── Colores ANSI ──────────────────────────────────────────────
VERDE    = '\033[92m'
AMARILLO = '\033[93m'
ROJO     = '\033[91m'
CYAN     = '\033[96m'
GRIS     = '\033[90m'
RESET    = '\033[0m'
NEGRITA  = '\033[1m'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def pausar():
    input(f'{NEGRITA}Presiona Enter para continuar...{RESET}')


class Operaciones:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sumar(self):
        return self.num1 + self.num2

    def restar(self):
        return self.num1 - self.num2

    def multiplicar(self):
        return self.num1 * self.num2

    def dividir(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return 'Error: División por cero no permitida'


def generar_operaciones():
    clear()
    print('Generador de Operaciones')
    try:
        num1 = float(input('Ingrese el primer número: '))
        num2 = float(input('Ingrese el segundo número: '))
        operacion = Operaciones(num1, num2)
        print(f'Suma:          {operacion.sumar()}')
        print(f'Resta:         {operacion.restar()}')
        print(f'Multiplicación:{operacion.multiplicar()}')
        print(f'División:      {operacion.dividir()}')
    except ValueError:
        print('Error: Por favor ingrese números válidos.')
    pausar()


def cuantos_ejercicios_generar():
    clear()
    print('Generador de Operaciones')

    try:
        print('¿Cuántos ejercicios deseas generar?')
        cant_suma   = int(input(f'{GRIS}Suma:{RESET} '))
        cant_resta  = int(input(f'{AMARILLO}Resta:{RESET} '))
        cant_multi  = int(input(f'{CYAN}Multiplicación:{RESET} '))
        cant_div    = int(input(f'{ROJO}División:{RESET} '))
    except ValueError:
        print('Por favor ingresa solo números.')
        return

    # ── Generar todos los pares de números UNA SOLA VEZ ──────────────────
    ejercicios = {
        'SUMA':           [(random.randint(1,100), random.randint(1,100)) for _ in range(cant_suma)],
        'RESTA':          [(random.randint(1,100), random.randint(1,100)) for _ in range(cant_resta)],
        'MULTIPLICACION': [(random.randint(1,100), random.randint(1,100)) for _ in range(cant_multi)],
        'DIVISION':       [(random.randint(1,100), random.randint(1,100)) for _ in range(cant_div)],
    }

    operadores = {
        'SUMA': '+', 'RESTA': '-', 'MULTIPLICACION': '*', 'DIVISION': '/'
    }


    def calcular(op, a, b):
        o = Operaciones(a, b)
        return {'SUMA': o.sumar, 'RESTA': o.restar,
                'MULTIPLICACION': o.multiplicar, 'DIVISION': o.dividir}[op]()

    # ── Construir contenido de ambos archivos ─────────────────────────────
    lineas_practica  = []
    lineas_respuestas = []

    for tipo, pares in ejercicios.items():
        for i, (a, b) in enumerate(pares, start=1):
            simbolo    = operadores[tipo]
            resultado  = calcular(tipo, a, b)

            lineas_practica.append(f'{tipo} {i}')
            lineas_practica.append(f'{a} {simbolo} {b} = ___')
            lineas_practica.append('')

            lineas_respuestas.append(f'{tipo} {i}')
            lineas_respuestas.append(f'{a} {simbolo} {b} = {resultado}')
            lineas_respuestas.append('')

    # ── Escribir archivos ─────────────────────────────────────────────────
    # with open('practica.txt', 'w', encoding='utf-8') as f:
    #     f.write('\n'.join(lineas_practica))

    # with open('respuestas.txt', 'w', encoding='utf-8') as f:
    #     f.write('\n'.join(lineas_respuestas))

# ── Escribir archivos - Ruta directamente en la carpeta -──────────────────
    base_dir = os.path.dirname(os.path.abspath(__file__))

    with open(os.path.join(base_dir, 'practica.txt'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(lineas_practica))

    with open(os.path.join(base_dir, 'respuestas.txt'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(lineas_respuestas))

    clear()
    print(f'{VERDE}✔ Archivos generados exitosamente:{RESET}')
    print('   • practica.txt   → ejercicios sin resolver')
    print('   • respuestas.txt → ejercicios resueltos')
    print()
    pausar()


if __name__ == '__main__':
    cuantos_ejercicios_generar()