def ignore_signos(palabra):
    signos = '.,;:!?()[]{}"\''  
    return palabra.strip(signos)

def ignore_palabras(palabra):
    palabras_ignoradas = {
        'el', 'la', 'de', 'y', 'a', 'un', 'una',
    }
    return palabra.lower() in palabras_ignoradas

def procesar_texto(texto):
    palabras = texto.split()
    palabras_limpias = []

    for p in palabras:
        p = ignore_signos(p).lower()
        if p and not ignore_palabras(p):   
            palabras_limpias.append(p)

    return palabras_limpias

def contar_frecuencias(palabras):
    frecuencia = {}
    for p in palabras:
        if p in frecuencia:
            frecuencia[p] += 1
        else:
            frecuencia[p] = 1
    return frecuencia

def top_n(frecuencia, n=5):
    items = list(frecuencia.items())
    items.sort(key=lambda x: (-x[1], x[0]))
    return items[:n]

def main():
    texto = input("\nIngrese un texto: ")
    palabras = procesar_texto(texto)

    total_palabras = len(palabras)
    palabras_unicas = len(set(palabras))

    frecuencia = contar_frecuencias(palabras)
    top5 = top_n(frecuencia, 5)

    print(f"\nCantidad total de palabras (sin contar palabras ignoradas): {total_palabras}")
    print(f"Cantidad de palabras únicas: {palabras_unicas}")
    print("\nTop 5 palabras más repetidas:")
    for palabra, freq in top5:
        print(f"{palabra} -> {freq}")  # formato como tu ejemplo

if __name__ == "__main__":
    main()
