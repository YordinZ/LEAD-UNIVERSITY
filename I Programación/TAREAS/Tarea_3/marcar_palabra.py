def buscar_palabra_coords(grid, palabra):
    palabra = palabra.upper()
    n = len(grid)

    direcciones = [
        (0, 1), (0, -1),
        (1, 0), (-1, 0),
        (1, 1), (1, -1),
        (-1, 1), (-1, -1),
    ]

    for fila in range(n):
        for col in range(n):
            for dr, dc in direcciones:
                coords = []
                ok = True

                for k, ch in enumerate(palabra):
                    r = fila + dr * k
                    c = col + dc * k

                    if not (0 <= r < n and 0 <= c < n):
                        ok = False
                        break
                    if grid[r][c] != ch:
                        ok = False
                        break

                    coords.append((r, c))

                if ok:
                    return coords

    return None


def marcar_palabra(grid, marcas, palabra, palabras_usuario, palabras_random):
    p = palabra.upper()
    coords = buscar_palabra_coords(grid, p)
    if coords is None:
        return False

    if p in palabras_usuario:
        color = 1  # verde
    elif p in palabras_random:
        color = 2  # rojo
    else:
        # si no está en ninguna lista, NO marcar (más estricto)
        return False

    for r, c in coords:
        marcas[r][c] = color

    return True
