estudiantes = [
 {'nombre': 'Ana', 'curso': 'Matemáticas', 'calificacion': 85},
 {'nombre': 'Luis', 'curso': 'Física', 'calificacion': 90},
] 

def mejorar_calificacion(estudiantes):
    resultado= {}
    for estudiante in estudiantes:
        nueva_calificacion = estudiante['calificacion'] + 3
        resultado[estudiante['nombre']] = nueva_calificacion
    return resultado

def promedio_calificacion(estudiantes):
    total = 0
    for estudiante in estudiantes:
        total += estudiante['calificacion']
    return total / len(estudiantes)

if __name__ == '__main__':
    resultado = promedio_calificacion(estudiantes)
    print(resultado)