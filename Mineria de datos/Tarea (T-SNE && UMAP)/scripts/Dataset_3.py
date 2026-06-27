import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.metrics import silhouette_score
from umap import UMAP


COLUMNAS_EXCLUIR = ['surname', 'team', 'position']
COLORES = plt.cm.tab10.colors


def preparar_datos(df, target_col='position'):
    columnas_drop = [c for c in COLUMNAS_EXCLUIR if c in df.columns]
    X = df.drop(columns=columnas_drop)
    X_scaled = StandardScaler().fit_transform(X)
    y = df[target_col].values
    return X_scaled, y


def _graficar_2d(ax, datos, target_col, titulo):
    categorias = sorted(datos[target_col].unique())
    for i, categoria in enumerate(categorias):
        subset = datos[datos[target_col] == categoria]
        ax.scatter(
            subset['V1'], subset['V2'],
            color=COLORES[i % 10], label=str(categoria),
            s=25, edgecolor='white', linewidth=0.3, alpha=0.85
        )
    ax.set_title(f'Método: {titulo}', fontsize=12, fontweight='bold', fontfamily='serif')
    ax.set_xlabel('V1', fontfamily='serif')
    ax.set_ylabel('V2', fontfamily='serif')
    ax.grid(True, alpha=0.25)
    ax.legend(title='Posición', bbox_to_anchor=(1.02, 1), loc='upper left',
              fontsize=7, title_fontsize=8)


def _graficar_3d(ax, datos, target_col, titulo):
    categorias = sorted(datos[target_col].unique())
    for i, categoria in enumerate(categorias):
        subset = datos[datos[target_col] == categoria]
        ax.scatter(
            subset['V1'], subset['V2'], subset['V3'],
            color=COLORES[i % 10], label=str(categoria),
            s=20, edgecolor='white', linewidth=0.2, alpha=0.80
        )
    ax.set_title(f'Método: {titulo}', fontsize=12, fontweight='bold', fontfamily='serif')
    ax.set_xlabel('V1', fontfamily='serif', fontsize=8)
    ax.set_ylabel('V2', fontfamily='serif', fontsize=8)
    ax.set_zlabel('V3', fontfamily='serif', fontsize=8)
    ax.grid(True, alpha=0.25)
    ax.legend(title='Posición', bbox_to_anchor=(1.05, 1), loc='upper left',
              fontsize=6, title_fontsize=7)


def acp(df, target_col='position', n_components=3, random_state=42, graficar=True):
    X_scaled, y = preparar_datos(df, target_col)

    modelo = PCA(n_components=n_components, random_state=random_state)
    componentes = modelo.fit_transform(X_scaled)

    score = silhouette_score(componentes, y)
    print(f"Varianza explicada por componente: {modelo.explained_variance_ratio_}")
    print(f"Varianza explicada acumulada: {modelo.explained_variance_ratio_.sum():.4f}")
    print(f"Silhouette score (ACP): {score:.4f}")

    cols = [f'V{i+1}' for i in range(n_components)]
    resultado = pd.DataFrame(componentes, columns=cols, index=df.index)
    resultado[target_col] = y

    if graficar:
        fig = plt.figure(figsize=(7, 6))
        ax = fig.add_subplot(111, projection='3d')
        _graficar_3d(ax, resultado, target_col, 'ACP')
        plt.tight_layout()
        plt.show()

    return resultado, modelo


def tsne(df, target_col='position', n_components=3, perplexity=30, random_state=42, graficar=True):
    X_scaled, y = preparar_datos(df, target_col)

    modelo = TSNE(n_components=n_components, perplexity=perplexity, init='pca', random_state=random_state)
    componentes = modelo.fit_transform(X_scaled)

    score = silhouette_score(componentes, y)
    print(f"Silhouette score (t-SNE): {score:.4f}")

    cols = [f'V{i+1}' for i in range(n_components)]
    resultado = pd.DataFrame(componentes, columns=cols, index=df.index)
    resultado[target_col] = y

    if graficar:
        fig = plt.figure(figsize=(7, 6))
        ax = fig.add_subplot(111, projection='3d')
        _graficar_3d(ax, resultado, target_col, 't-SNE')
        plt.tight_layout()
        plt.show()

    return resultado


def umap(df, target_col='position', n_components=3, lista_vecinos=None, random_state=42, graficar=True):
    if lista_vecinos is None:
        lista_vecinos = [5, 10, 15, 20, 30, 50]

    X_scaled, y = preparar_datos(df, target_col)

    mejor_score = -1
    mejor_n_vecinos = None
    mejor_resultado = None
    scores_por_vecino = {}

    for n_vecinos in lista_vecinos:
        modelo = UMAP(n_components=n_components, n_neighbors=n_vecinos, random_state=random_state)
        componentes = modelo.fit_transform(X_scaled)

        score = silhouette_score(componentes, y)
        scores_por_vecino[n_vecinos] = score

        cols = [f'V{i+1}' for i in range(n_components)]
        resultado = pd.DataFrame(componentes, columns=cols, index=df.index)
        resultado[target_col] = y

        if score > mejor_score:
            mejor_score = score
            mejor_n_vecinos = n_vecinos
            mejor_resultado = resultado

    print(f"Silhouette score por cantidad de vecinos: {scores_por_vecino}")
    print(f"Mejor cantidad de vecinos: {mejor_n_vecinos} (silhouette score: {mejor_score:.4f})")

    if graficar:
        fig = plt.figure(figsize=(7, 6))
        ax = fig.add_subplot(111, projection='3d')
        _graficar_3d(ax, mejor_resultado, target_col, 'UMAP')
        plt.tight_layout()
        plt.show()

    return mejor_resultado, mejor_n_vecinos


def graficar_comparacion_2d(resultado_acp, resultado_tsne, resultado_umap, target_col='position'):
    fig = plt.figure(figsize=(13, 10))
    gs = gridspec.GridSpec(2, 4, figure=fig)

    ax1 = fig.add_subplot(gs[0, 0:2])
    ax2 = fig.add_subplot(gs[0, 2:4])
    ax3 = fig.add_subplot(gs[1, 1:3])

    _graficar_2d(ax1, resultado_acp, target_col, 'ACP')
    _graficar_2d(ax2, resultado_tsne, target_col, 't-SNE')
    _graficar_2d(ax3, resultado_umap, target_col, 'UMAP')

    plt.suptitle('Comparación 2D: ACP vs t-SNE vs UMAP', fontsize=14,
                 fontweight='bold', fontfamily='serif', y=1.01)
    plt.tight_layout()
    plt.show()


def graficar_comparacion_3d(resultado_acp, resultado_tsne, resultado_umap, target_col='position'):
    fig = plt.figure(figsize=(18, 6))

    ax1 = fig.add_subplot(131, projection='3d')
    ax2 = fig.add_subplot(132, projection='3d')
    ax3 = fig.add_subplot(133, projection='3d')

    _graficar_3d(ax1, resultado_acp, target_col, 'ACP')
    _graficar_3d(ax2, resultado_tsne, target_col, 't-SNE')
    _graficar_3d(ax3, resultado_umap, target_col, 'UMAP')

    plt.suptitle('Comparación 3D: ACP vs t-SNE vs UMAP', fontsize=14,
                 fontweight='bold', fontfamily='serif', y=1.01)
    plt.tight_layout()
    plt.show()