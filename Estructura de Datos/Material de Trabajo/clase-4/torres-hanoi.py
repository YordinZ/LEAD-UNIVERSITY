def torres_hanoi(n, origen, auxiliar, destino):
    # Caso base
    if n == 1:
        print(f"Mover disco 1 de {origen} a {destino}")
        return

    # Mover n-1 discos al poste auxiliar
    torres_hanoi(n - 1, origen, destino, auxiliar)

    # Mover el disco más grande al destino
    print(f"Mover disco {n} de {origen} a {destino}")

    # Mover los n-1 discos restantes al destino
    torres_hanoi(n - 1, auxiliar, origen, destino)


# Ejemplo: 3 discos
torres_hanoi(3, "A", "B", "C")