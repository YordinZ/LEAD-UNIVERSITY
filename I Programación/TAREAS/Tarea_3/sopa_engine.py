import random
from .Letras_aleatorios_colores import generar_letra, generar_palabra_random

def crear_matriz(n=15):
    return [[None for _ in range(n)] for _ in range(n)]

def cabe(palabra, grid, fila, col, dr, dc):
    n = len(grid)
    for k, ch in enumerate(palabra):
        r = fila + dr*k
        c = col + dc*k
        if r < 0 or r >= n or c < 0 or c >= n:
            return False
        if grid[r][c] is not None and grid[r][c] != ch:
            return False
    return True

def colocar(palabra, grid, intentos=200):
    dirs = [(0,1), (1,0), (0,-1), (-1,0)]
    n = len(grid)

    for _ in range(intentos):
        dr, dc = random.choice(dirs)
        fila = random.randint(0, n-1)
        col = random.randint(0, n-1)

        if cabe(palabra, grid, fila, col, dr, dc):
            for k, ch in enumerate(palabra):
                r = fila + dr*k
                c = col + dc*k
                grid[r][c] = ch
            return True
    return False

def rellenar(grid):
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j] is None:
                grid[i][j] = generar_letra()

def generar_sopa(palabras_usuario, n=15, cantidad_random=10):
    palabras_usuario = [p.strip().upper()[:n] for p in palabras_usuario if p.strip()]
    palabras_usuario = palabras_usuario[:15]

    palabras_random = []
    for _ in range(cantidad_random):
        L = random.randint(5, min(9, n))
        palabras_random.append(generar_palabra_random(L))

    grid = crear_matriz(n)

    for p in palabras_usuario:
        colocar(p, grid)
    for p in palabras_random:
        colocar(p, grid)

    rellenar(grid)
    return grid, palabras_usuario, palabras_random
