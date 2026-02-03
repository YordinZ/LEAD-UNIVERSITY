def calificacion_a_letra(nota):
    """
    Convierte calificación numérica a letra en una sola función
    """
    if nota < 0 or nota > 100:
        print("Error: La calificación debe estar entre 0 y 100")

    if nota >= 90: return 'A', 'Excelente'
    elif nota >= 80: return 'B', 'Muy Bueno'
    elif nota >= 70: return 'C', 'Bueno'
    elif nota >= 60: return 'D', 'Aprobado'
    else: return 'F', 'Reprobado'

try:
    nota = float(input("Ingrese calificación (0-100): "))
    letra, desc = calificacion_a_letra(nota)
    print(f"{nota} → {letra} ({desc})")
except:
    print("Entrada inválida")