"""
style.py
--------
Configuracion visual compartida para todo el proyecto: paleta de colores,
tipografia y helpers para que los graficos de matplotlib/seaborn mantengan
el mismo estilo (naranja #B85300 + Palatino Linotype) en ambos datasets.
"""

import matplotlib.pyplot as plt

# ----------------------------------------------------------------------
# Paleta del proyecto
# ----------------------------------------------------------------------
COLOR_PRIMARY = "#B85300"      # Naranja principal
COLOR_DARK = "#3B2412"         # Texto/oscuro para contraste
COLOR_PALETTE = [              # Paleta para clusters (K variable, hasta 6)
    "#B85300", "#4C6A92", "#7A9E7E", "#A63A50", "#C9A227", "#5C4B8A"
]
FONT_FAMILY = "Palatino Linotype"


def set_plot_style():
    """
    Configura rcParams de matplotlib para que todos los graficos del
    notebook usen la fuente y colores del proyecto.
    """
    plt.rcParams["font.family"] = FONT_FAMILY
    plt.rcParams["axes.titlesize"] = 14
    plt.rcParams["axes.titleweight"] = "bold"
    plt.rcParams["axes.labelcolor"] = COLOR_DARK
    plt.rcParams["axes.edgecolor"] = COLOR_DARK
    plt.rcParams["xtick.color"] = COLOR_DARK
    plt.rcParams["ytick.color"] = COLOR_DARK
    plt.rcParams["figure.facecolor"] = "white"
    plt.rcParams["axes.facecolor"] = "white"
    plt.rcParams["grid.color"] = "#E0D2C0"
    plt.rcParams["grid.alpha"] = 0.6
    plt.rcParams["axes.grid"] = True
    plt.rcParams["figure.figsize"] = (8, 5)


def cluster_palette(n_clusters: int):
    """
    Devuelve una lista de n_clusters colores tomados de COLOR_PALETTE.
    Si se piden mas colores de los definidos, se ciclan.
    """
    if n_clusters <= len(COLOR_PALETTE):
        return COLOR_PALETTE[:n_clusters]
    reps = (n_clusters // len(COLOR_PALETTE)) + 1
    return (COLOR_PALETTE * reps)[:n_clusters]
