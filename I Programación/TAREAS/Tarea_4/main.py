from empleados import Administrador, Conserje, Veterinario, Guardian
from transportes import Bicicleta, Cuadraciclo, Patineta
from animales import Reptil, Mamifero, Ave, Pez, Anfibio

# Listas globales
empleados   = []
transportes = []
animales    = []


# ─────────────────────────────────────────────
#  HELPERS
# ─────────────────────────────────────────────

def pedir(mensaje, tipo=str, opciones=None):
    """Solicita un dato al usuario, valida tipo y opciones permitidas."""
    while True:
        try:
            valor = tipo(input(f"  {mensaje}: ").strip())
            if opciones and str(valor).lower() not in opciones:
                print(f"  ⚠  Debe ser una de: {opciones}")
                continue
            return valor
        except ValueError:
            print(f"  ⚠  Entrada inválida. Se esperaba {tipo.__name__}.")

def separador(titulo=""):
    print("\n" + "═" * 55)
    if titulo:
        print(f"  {titulo}")
        print("═" * 55)

def listar(lista, nombre):
    separador(f"📋  {nombre}")
    if not lista:
        print("  (No hay registros aún)")
    for i, obj in enumerate(lista, 1):
        print(f"  {i}. {obj}")

def continuar():
    input("\n  Presiona Enter para continuar...")


# ─────────────────────────────────────────────
#  EMPLEADOS
# ─────────────────────────────────────────────

def agregar_administrador():
    separador("➕  Agregar Administrador")
    try:
        nombre       = pedir("Nombre")
        edad         = pedir("Edad", int)
        salario      = pedir("Salario", float)
        departamento = pedir("Departamento")
        empleados.append(Administrador(nombre, edad, salario, departamento))
        print("  ✅  Administrador agregado correctamente.")
    except ValueError as e:
        print(f"  ❌  Error: {e}")

def agregar_guardian():
    separador("➕  Agregar Guardián")
    try:
        nombre  = pedir("Nombre")
        edad    = pedir("Edad", int)
        salario = pedir("Salario", float)
        zona    = pedir("Zona")
        empleados.append(Guardian(nombre, edad, salario, zona))
        print("  ✅  Guardián agregado correctamente.")
    except ValueError as e:
        print(f"  ❌  Error: {e}")

def agregar_conserje():
    separador("➕  Agregar Conserje")
    try:
        nombre  = pedir("Nombre")
        edad    = pedir("Edad", int)
        salario = pedir("Salario", float)
        turno   = pedir("Turno (mañana/tarde/noche)", opciones={"mañana", "tarde", "noche"})
        empleados.append(Conserje(nombre, edad, salario, turno))
        print("  ✅  Conserje agregado correctamente.")
    except ValueError as e:
        print(f"  ❌  Error: {e}")

def agregar_veterinario():
    separador("➕  Agregar Veterinario")
    try:
        nombre       = pedir("Nombre")
        edad         = pedir("Edad", int)
        salario      = pedir("Salario", float)
        especialidad = pedir("Especialidad")
        empleados.append(Veterinario(nombre, edad, salario, especialidad))
        print("  ✅  Veterinario agregado correctamente.")
    except ValueError as e:
        print(f"  ❌  Error: {e}")

def menu_empleados():
    while True:
        separador("👤  Agregar Empleado")
        print("  1. Agregar Administrador")
        print("  2. Agregar Guardián")
        print("  3. Agregar Conserje")
        print("  4. Agregar Veterinario")
        print("  0. Volver al menú principal")
        opcion = input("\n  Selecciona una opción: ").strip()
        if   opcion == "1": agregar_administrador()
        elif opcion == "2": agregar_guardian()
        elif opcion == "3": agregar_conserje()
        elif opcion == "4": agregar_veterinario()
        elif opcion == "0": break
        else: print("  ⚠  Opción inválida.")
        continuar()


# ─────────────────────────────────────────────
#  TRANSPORTES
# ─────────────────────────────────────────────

COLORES = {"rojo", "azul", "verde", "negro", "blanco", "amarillo", "gris", "naranja"}

def agregar_bicicleta():
    separador("➕  Agregar Bicicleta")
    try:
        marca   = pedir("Marca")
        modelo  = pedir("Modelo")
        color   = pedir(f"Color {COLORES}", opciones=COLORES)
        vel     = pedir("Velocidad máxima (km/h)", float)
        marchas = pedir("Número de marchas", int)
        transportes.append(Bicicleta(marca, modelo, color, vel, marchas))
        print("  ✅  Bicicleta agregada correctamente.")
    except ValueError as e:
        print(f"  ❌  Error: {e}")

def agregar_cuadraciclo():
    separador("➕  Agregar Cuadraciclo")
    try:
        marca      = pedir("Marca")
        modelo     = pedir("Modelo")
        color      = pedir(f"Color {COLORES}", opciones=COLORES)
        vel        = pedir("Velocidad máxima (km/h)", float)
        cilindrada = pedir("Cilindrada (cc)", float)
        transportes.append(Cuadraciclo(marca, modelo, color, vel, cilindrada))
        print("  ✅  Cuadraciclo agregado correctamente.")
    except ValueError as e:
        print(f"  ❌  Error: {e}")

def agregar_patineta():
    separador("➕  Agregar Patineta")
    try:
        marca     = pedir("Marca")
        modelo    = pedir("Modelo")
        color     = pedir(f"Color {COLORES}", opciones=COLORES)
        vel       = pedir("Velocidad máxima (km/h)", float)
        electrica = pedir("¿Es eléctrica? (s/n)", opciones={"s", "n"})
        transportes.append(Patineta(marca, modelo, color, vel, electrica == "s"))
        print("  ✅  Patineta agregada correctamente.")
    except ValueError as e:
        print(f"  ❌  Error: {e}")

def menu_transportes():
    while True:
        separador("🚲  Agregar Medio de Transporte")
        print("  1. Agregar Bicicleta")
        print("  2. Agregar Cuadraciclo")
        print("  3. Agregar Patineta")
        print("  0. Volver al menú principal")
        opcion = input("\n  Selecciona una opción: ").strip()
        if   opcion == "1": agregar_bicicleta()
        elif opcion == "2": agregar_cuadraciclo()
        elif opcion == "3": agregar_patineta()
        elif opcion == "0": break
        else: print("  ⚠  Opción inválida.")
        continuar()


# ─────────────────────────────────────────────
#  ANIMALES
# ─────────────────────────────────────────────

GENEROS = {"macho", "hembra"}

def agregar_reptil():
    separador("➕  Agregar Reptil")
    try:
        nombre   = pedir("Nombre")
        raza     = pedir("Raza")
        genero   = pedir("Género (macho/hembra)", opciones=GENEROS)
        venenoso = pedir("¿Es venenoso? (s/n)", opciones={"s", "n"})
        animales.append(Reptil(nombre, raza, genero, venenoso == "s"))
        print("  ✅  Reptil agregado correctamente.")
    except ValueError as e:
        print(f"  ❌  Error: {e}")

def agregar_mamifero():
    separador("➕  Agregar Mamífero")
    try:
        nombre    = pedir("Nombre")
        raza      = pedir("Raza")
        genero    = pedir("Género (macho/hembra)", opciones=GENEROS)
        domestico = pedir("¿Es doméstico? (s/n)", opciones={"s", "n"})
        animales.append(Mamifero(nombre, raza, genero, domestico == "s"))
        print("  ✅  Mamífero agregado correctamente.")
    except ValueError as e:
        print(f"  ❌  Error: {e}")

def agregar_ave():
    separador("➕  Agregar Ave")
    try:
        nombre = pedir("Nombre")
        raza   = pedir("Raza")
        genero = pedir("Género (macho/hembra)", opciones=GENEROS)
        volar  = pedir("¿Puede volar? (s/n)", opciones={"s", "n"})
        animales.append(Ave(nombre, raza, genero, volar == "s"))
        print("  ✅  Ave agregada correctamente.")
    except ValueError as e:
        print(f"  ❌  Error: {e}")

def agregar_pez():
    separador("➕  Agregar Pez")
    try:
        nombre      = pedir("Nombre")
        raza        = pedir("Raza")
        genero      = pedir("Género (macho/hembra)", opciones=GENEROS)
        agua_salada = pedir("¿Agua salada? (s/n)", opciones={"s", "n"})
        animales.append(Pez(nombre, raza, genero, agua_salada == "s"))
        print("  ✅  Pez agregado correctamente.")
    except ValueError as e:
        print(f"  ❌  Error: {e}")

def agregar_anfibio():
    separador("➕  Agregar Anfibio")
    try:
        nombre  = pedir("Nombre")
        raza    = pedir("Raza")
        genero  = pedir("Género (macho/hembra)", opciones=GENEROS)
        habitat = pedir("Hábitat")
        animales.append(Anfibio(nombre, raza, genero, habitat))
        print("  ✅  Anfibio agregado correctamente.")
    except ValueError as e:
        print(f"  ❌  Error: {e}")

def menu_animales():
    while True:
        separador("🐾  Agregar Animal")
        print("  1. Agregar Reptil")
        print("  2. Agregar Mamífero")
        print("  3. Agregar Ave")
        print("  4. Agregar Pez")
        print("  5. Agregar Anfibio")
        print("  0. Volver al menú principal")
        opcion = input("\n  Selecciona una opción: ").strip()
        if   opcion == "1": agregar_reptil()
        elif opcion == "2": agregar_mamifero()
        elif opcion == "3": agregar_ave()
        elif opcion == "4": agregar_pez()
        elif opcion == "5": agregar_anfibio()
        elif opcion == "0": break
        else: print("  ⚠  Opción inválida.")
        continuar()


# ─────────────────────────────────────────────
#  MENÚ PRINCIPAL
# ─────────────────────────────────────────────

def menu_principal():
    while True:
        separador("🏠  ZOOLÓGICO — MENÚ PRINCIPAL")
        print("  1. Agregar empleado")
        print("  2. Listar empleados")
        print("  3. Agregar medio de transporte")
        print("  4. Listar medios de transporte")
        print("  5. Agregar animal")
        print("  6. Listar animales")
        print("  0. Salir")
        opcion = input("\n  Selecciona una opción: ").strip()

        if   opcion == "1": menu_empleados()
        elif opcion == "2": listar(empleados,   "Empleados");   continuar()
        elif opcion == "3": menu_transportes()
        elif opcion == "4": listar(transportes, "Medios de Transporte"); continuar()
        elif opcion == "5": menu_animales()
        elif opcion == "6": listar(animales,    "Animales");    continuar()
        elif opcion == "0": print("\n  👋  ¡Hasta luego!\n"); break
        else: print("  ⚠  Opción inválida."); continuar()


if __name__ == "__main__":
    menu_principal()
