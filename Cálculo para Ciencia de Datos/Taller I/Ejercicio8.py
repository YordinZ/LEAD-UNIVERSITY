import matplotlib.pyplot as plt
import sympy as sp
import numpy as np
from numpy.polynomial import Polynomial


dataset = {
    "Enero": 260,
    "Febrero": 250,
    "Marzo": 255,
    "Abril": 230,
    "Mayo": 200,
    "Junio": 195,
    "Julio": 220,
    "Agosto": 210,
    "Septiembre": 175,
    "Octubre": 180,
    "Noviembre": 215,
    "Diciembre": 270
}


def modelo_cubico(dataset):
    x = np.array(list(range(1, 13)))
    y = np.array(list(dataset.values()))
    polinomio_cubico = Polynomial.fit(x, y, deg=3)
    return polinomio_cubico


def verificar_simbolico(modelo):
    x = sp.symbols('x')
    coefs = modelo.convert().coef
    polinomio_sym = sum(c * x**i for i, c in enumerate(coefs))
    polinomio_sym = sp.expand(polinomio_sym)
    return polinomio_sym


def mayor_crecimiento(modelo):
    x = sp.symbols('x')
    polinomio_sym = verificar_simbolico(modelo)
    derivada = sp.diff(polinomio_sym, x)
    puntos_criticos = sp.solve(derivada, x)

    crecimiento = []
    for punto in puntos_criticos:
        valor_derivada_segunda = sp.diff(derivada, x).subs(x, punto)
        if valor_derivada_segunda > 0:
            crecimiento.append((punto, "crecimiento"))
        elif valor_derivada_segunda < 0:
            crecimiento.append((punto, "decrecimiento"))
        else:
            crecimiento.append((punto, "punto de inflexión"))

    return crecimiento


def regla_producto_gasto():
    t = sp.symbols('t')
    G = (300 + 20*t) * sp.exp(0.05*t)
    dG = sp.simplify(sp.diff(G, t))
    print("G'(t) =")
    sp.pprint(dG)


def derivadas_flujo(modelo):
    t = sp.symbols('t')
    coefs = modelo.convert().coef
    T = sp.expand(sum(c * t**i for i, c in enumerate(coefs)))

    dT  = sp.diff(T, t)
    ddT = sp.diff(dT, t)

    inflexion = sp.solve(ddT, t)
    inflexion_real = [float(p) for p in inflexion if p.is_real]

    print("T'(t) =");  sp.pprint(dT)
    print("\nT''(t) ="); sp.pprint(ddT)
    print(f"\nPunto de inflexión (mes): {inflexion_real}")
    return dT, ddT


def graficar_flujo(modelo, dataset):
    t_vals = np.linspace(1, 12, 200)
    T_vals = modelo(t_vals)

    # Derivada simbólica convertida a función numpy
    t_sym = sp.symbols('t')
    coefs = modelo.convert().coef
    T_sym = sp.expand(sum(c * t_sym**i for i, c in enumerate(coefs)))
    dT_sym = sp.diff(T_sym, t_sym)
    dT_func = sp.lambdify(t_sym, dT_sym, 'numpy')
    dT_vals = dT_func(t_vals)

    # API orientada a objetos + layout='constrained'
    fig, ax = plt.subplots(figsize=(10, 6), layout='constrained')

    ax.plot(t_vals, T_vals,  color='#004B87', linewidth=2, label="T(t) — Modelo cúbico")
    ax.plot(t_vals, dT_vals, color='#E8A020', linewidth=2, linestyle='--', label="T'(t) — Tasa de cambio")
    ax.scatter(range(1, 13), list(dataset.values()), color='#004B87', zorder=5, label='Datos ICT')

    ax.set_title('Flujo turístico mensual — Costa Rica', fontsize=14)
    ax.set_xlabel('Mes (t)')
    ax.set_ylabel('Llegadas (miles)')
    ax.set_xticks(range(1, 13))
    ax.set_xticklabels(list(dataset.keys()), rotation=45)
    ax.legend(loc='best')
    ax.grid(True)
    plt.show()


def scree_plot(dataset):
    meses = list(dataset.keys())
    ventas = list(dataset.values())

    varianza_total = sum(v**2 for v in ventas)
    varianza_explicada = [(v**2 / varianza_total) * 100 for v in ventas]
    varianza_acumulada = np.cumsum(varianza_explicada)

    fig, ax = plt.subplots(figsize=(10, 6), layout='constrained')
    ax.bar(meses, varianza_explicada, color='#E8A020', alpha=0.7, label='Varianza explicada (%)')
    ax.plot(meses, varianza_acumulada, color='#004B87', marker='o', label='Varianza acumulada (%)')
    ax.set_title('Scree Plot — Flujo turístico mensual')
    ax.set_xlabel('Meses')
    ax.set_ylabel('Varianza explicada (%)')
    ax.set_xticklabels(meses, rotation=45)
    ax.legend(loc='best')
    ax.grid(True)
    plt.show()


modelo = modelo_cubico(dataset)
print("Modelo cúbico ajustado:")
print(modelo)

polinomio_sym = verificar_simbolico(modelo)
print("\nPolinomio simbólico (sympy):")
sp.pprint(polinomio_sym)

crecimiento = mayor_crecimiento(modelo)
print("\nPuntos de crecimiento y decrecimiento:")
print(crecimiento)

print("\nRegla del producto — G'(t):")
regla_producto_gasto()

print("\nDerivadas del flujo turístico:")
dT, ddT = derivadas_flujo(modelo)

graficar_flujo(modelo, dataset)
scree_plot(dataset)