def encriptacion_cesar(texto, n):
    abecedario = "abcdefghijklmnopqrstuvwxyz"
    resultado = ""

    for letra in texto:
        if letra in abecedario:
            indice = abecedario.index(letra)
            nuevo_indice = (indice + n) % len(abecedario)
            resultado += abecedario[nuevo_indice]
        else:
            resultado += letra  # espacios u otros símbolos

    return resultado