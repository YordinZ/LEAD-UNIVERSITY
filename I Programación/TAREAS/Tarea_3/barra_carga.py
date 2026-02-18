import os
import time

def loading_bar(duration=3.0, width=30): # Función para mostrar una barra de carga animada
    start = time.time()
    end = start + duration

    while True:
        now = time.time()
        if now >= end:
            break

        progress = (now - start) / duration
        fill = int(progress * width)

        bar = "#" * fill + "-" * (width - fill)
        pct = int(progress * 100)

        os.write(1, f"\rCargando: [{bar}] {pct:3d}%".encode("utf-8"))
        time.sleep(0.05)

    os.write(1, f"\rCargando: [{'#'*width}] 100%\n".encode("utf-8"))
