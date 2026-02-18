def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return None
    return a / b


def evaluar_expresion(expresion):
    numeros = []
    operadores = []
    numero_actual = ''

    for caracter in expresion:
        if caracter.isdigit() or caracter == '.':
            numero_actual += caracter
        elif caracter in '+-*/':
            if numero_actual == '':
                return 'Error: Expresión inválida.'
            numeros.append(float(numero_actual))
            operadores.append(caracter)
            numero_actual = ''
        else:
            return 'Error: Carácter inválido.'

    if numero_actual == '':
        return 'Error: Expresión inválida.'

    numeros.append(float(numero_actual))
    
    # Validaciones
    if len(numeros) - 1 != len(operadores):
        return 'Error: Expresión inválida.'

    for n in numeros:
        if n < 0:
            return 'Error: No se permiten números negativos.'

    resultado = numeros[0]

    for i in range(len(operadores)):
        operador = operadores[i]
        numero = numeros[i + 1]

        if operador == '+':
            resultado = suma(resultado, numero)
        elif operador == '-':
            resultado = resta(resultado, numero)
        elif operador == '*':
            resultado = multiplicacion(resultado, numero)
        elif operador == '/':
            resultado = division(resultado, numero)
            if resultado is None:
                return 'Error: No se puede dividir entre cero.'

    return resultado


def main():
    print('\n..................... CALCULADORA .....................\n')
    expresion = input('Ingrese la operación matemática: ').replace(' ', '')
    resultado = evaluar_expresion(expresion)

    if isinstance(resultado, str):
        print(resultado)
    else:
        print('Resultado:', resultado)


if __name__ == '__main__':
    main()