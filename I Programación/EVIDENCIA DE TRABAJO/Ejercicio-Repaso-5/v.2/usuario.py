import pandas as pd
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_promedios(edad, salario, peso):
    print("\n--- Promedios ---")
    print(f"Edad promedio:    {edad:.1f} años")
    print(f"Salario promedio: ${salario:.2f}")
    print(f"Peso promedio:    {peso:.1f} kg")
    print("-----------------")

def leer_csv():
    ruta = os.path.join(DATA_DIR, 'personas.csv')
    df = pd.read_csv(ruta)
    print(df.to_string(index=False))
    mostrar_promedios(
        df['edad'].mean(),
        df['salario'].mean(),
        df['peso'].mean()
        #suma de todos los valores ÷ cantidad de elementos — el mismo promedio que calcularías a mano, solo que pandas lo hace automáticamente sobre toda la columna.
    )

def leer_json():
    ruta = os.path.join(DATA_DIR, 'personas.json')
    with open(ruta, 'r', encoding='utf-8') as f:
        datos = json.load(f)
    print(json.dumps(datos, indent=4, ensure_ascii=False))
    df = pd.DataFrame(datos)
    mostrar_promedios(
        df['edad'].mean(),
        df['salario'].mean(),
        df['peso'].mean()
    )

def menu():
    print("\n¿Qué archivo desea leer?")
    print("1. CSV")
    print("2. JSON")
    print("3. Salir")
    return input("Seleccione una opción: ")

def volver_a_menu():
    input("\nPresione Enter para volver al menú...")

while True:
    clear()
    opcion = menu()
    if opcion == '1':
        clear()
        leer_csv()
        volver_a_menu()
    elif opcion == '2':
        clear()
        leer_json()
        volver_a_menu()
    elif opcion == '3':
        clear()
        print("Hasta luego.")
        break
    else:
        print("Opción no válida.")
        volver_a_menu()