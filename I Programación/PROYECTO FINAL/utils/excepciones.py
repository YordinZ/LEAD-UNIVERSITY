"""
utils/excepciones.py
Excepciones personalizadas y salida de emergencia global.
"""

class SalidaForzada(Exception):
    """Se lanza cuando el usuario escribe 'salir' en cualquier prompt."""
    pass


# Override global de input() para capturar 'salir' en cualquier punto
_input_original = input

def input(prompt: str = '') -> str:
    respuesta = _input_original(prompt)
    if respuesta.strip().lower() == 'salir':
        raise SalidaForzada()
    return respuesta
