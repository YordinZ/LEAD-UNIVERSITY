"""
visualization.py
------------------
Funciones de graficado para el analisis visual pedido en el enunciado:
curva del codo, dendrograma y dispersion de clusters (con PCA si aplica).
Todas respetan el estilo del proyecto (ver style.py).
"""

import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram

from . import style


def plot_elbow(inertias: list, k_range: range, title: str = "Metodo del Codo de Jambu"):
    """
    Grafica la Inercia (WCSS) contra K para identificar visualmente el codo.
    """
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(list(k_range), inertias, marker="o", color=style.COLOR_PRIMARY,
             linewidth=2, markersize=7, markerfacecolor=style.COLOR_DARK)
    ax.set_title(title, color=style.COLOR_PRIMARY)
    ax.set_xlabel("Numero de Clusters (K)")
    ax.set_ylabel("Inercia (WCSS)")
    ax.set_xticks(list(k_range))
    plt.tight_layout()
    plt.show()


def plot_dendrogram(Z, title: str = "Dendrograma - Clustering Jerarquico"):
    """
    Grafica el dendrograma a partir de la matriz de enlace Z
    (ver clustering.linkage_matrix).
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    dendrogram(
        Z, ax=ax,
        color_threshold=0.7 * max(Z[:, 2]),
        above_threshold_color=style.COLOR_DARK,
    )
    ax.set_title(title, color=style.COLOR_PRIMARY)
    ax.set_xlabel("Observaciones")
    ax.set_ylabel("Distancia")
    plt.tight_layout()
    plt.show()


def plot_clusters_2d(X_2d, labels, title: str, xlabel: str = "Componente 1",
                      ylabel: str = "Componente 2", ax=None):
    """
    Grafico de dispersion coloreado por cluster. Sirve tanto para variables
    originales (si ya son 2D) como para componentes PCA.
    """
    standalone = ax is None
    if standalone:
        fig, ax = plt.subplots(figsize=(7, 6))

    n_clusters = len(set(labels))
    palette = style.cluster_palette(n_clusters)

    for cluster_id in sorted(set(labels)):
        mask = labels == cluster_id
        ax.scatter(
            X_2d[mask, 0], X_2d[mask, 1],
            s=45, alpha=0.8, edgecolor="white", linewidth=0.5,
            color=palette[cluster_id % len(palette)],
            label=f"Cluster {cluster_id}",
        )

    ax.set_title(title, color=style.COLOR_PRIMARY)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend(frameon=False, fontsize=9)

    if standalone:
        plt.tight_layout()
        plt.show()


def plot_comparison(X_2d, labels_kmeans, labels_hierarchical, dataset_name: str):
    """
    Grafico lado a lado (1 fila, 2 columnas) comparando las asignaciones
    de K-Means vs Clustering Jerarquico sobre los mismos datos.
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    plot_clusters_2d(
        X_2d, labels_kmeans,
        title=f"K-Means - {dataset_name}",
        ax=axes[0],
    )
    plot_clusters_2d(
        X_2d, labels_hierarchical,
        title=f"Jerarquico - {dataset_name}",
        ax=axes[1],
    )

    plt.tight_layout()
    plt.show()
