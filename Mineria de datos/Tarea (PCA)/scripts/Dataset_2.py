import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


def Scree_Plot():
    df = pd.read_csv('data/Country-data.csv')
    
    features = ['child_mort', 'exports', 'health', 'imports',
                'income', 'inflation', 'life_expec', 'total_fer', 'gdpp']
    
    X = df[features].dropna()
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # PCA con todos los componentes para ver la varianza acumulada
    pca = PCA(n_components=len(features))
    pca.fit(X_scaled)
    
    varianza_explicada = pca.explained_variance_ratio_
    varianza_acumulada = np.cumsum(varianza_explicada)
    componentes = range(1, len(features) + 1)
    
    plt.figure(figsize=(10, 6))
    
    # Barras de varianza individual
    plt.bar(componentes, varianza_explicada * 100, alpha=0.6,
            color='steelblue', label='Varianza individual')
    
    # Línea de varianza acumulada
    plt.plot(componentes, varianza_acumulada * 100, 
             marker='o', color='red', linewidth=2, label='Varianza acumulada')
    
    plt.xlabel('Componente Principal')
    plt.ylabel('Varianza Explicada (%)')
    plt.title('Scree Plot - PCA Country Data')
    plt.xticks(componentes)
    plt.legend()
    plt.tight_layout()
    plt.show()


def Circulo_Correlacion():
    df = pd.read_csv('data/Country-data.csv')
    features = ['child_mort', 'exports', 'health', 'imports',
                'income', 'inflation', 'life_expec', 'total_fer', 'gdpp']

    X = df[features].dropna()
    idx = X.index
    countries = df.loc[idx, 'country'].values

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    pca = PCA(n_components=2)
    scores = pca.fit_transform(X_scaled)
    loadings = pca.components_.T  # forma (9, 2)

    # Escalar scores al rango de los loadings ([-1, 1])
    scale = np.max(np.abs(scores))
    scores_norm = scores / scale

    fig, ax = plt.subplots(figsize=(10, 10))

    # ── Países (puntos escalados) ──────────────────────────────────────
    ax.scatter(scores_norm[:, 0], scores_norm[:, 1],
               color='steelblue', alpha=0.4, s=25, zorder=2, label='Países')

    # Etiquetar solo los países más extremos (distancia al origen > umbral)
    distances = np.sqrt(scores_norm[:, 0]**2 + scores_norm[:, 1]**2)
    threshold = np.percentile(distances, 85)  # top 15% más alejados
    for i, country in enumerate(countries):
        if distances[i] >= threshold:
            ax.text(scores_norm[i, 0] + 0.02, scores_norm[i, 1] + 0.02,
                    country, fontsize=7, color='steelblue', alpha=0.85,
                    va='bottom')

    # ── Círculo unitario de referencia ────────────────────────────────
    circulo = plt.Circle((0, 0), 1, color='gray', fill=False,
                         linestyle='--', linewidth=1)
    ax.add_patch(circulo)

    # ── Flechas y etiquetas de variables ──────────────────────────────
    colors_feat = ['#E24B4A', '#3481C8', '#1D9E75', '#8B5CF6',
                   '#F59E0B', '#EC4899', '#14B8A6', '#D85A30', '#6366F1']
    for i, feature in enumerate(features):
        lx, ly = loadings[i, 0], loadings[i, 1]
        ax.annotate('', xy=(lx, ly), xytext=(0, 0),
                    arrowprops=dict(arrowstyle='->', color=colors_feat[i], lw=2.2))
        norm = np.sqrt(lx**2 + ly**2 + 1e-9)
        offset = 0.13
        ax.text(lx + lx / norm * offset,
                ly + ly / norm * offset,
                feature, fontsize=10, ha='center',
                color=colors_feat[i], fontweight='bold')

    # ── Líneas de referencia ──────────────────────────────────────────
    ax.axhline(0, color='black', linewidth=0.5, linestyle='--')
    ax.axvline(0, color='black', linewidth=0.5, linestyle='--')

    ax.set_xlim(-1.35, 1.35)
    ax.set_ylim(-1.35, 1.35)
    ax.set_xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}%)', fontsize=12)
    ax.set_ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.1f}%)', fontsize=12)
    ax.set_title('Círculo de Correlación - PCA Country Data\n'
                 '(países escalados al espacio unitario)', fontsize=14)
    ax.set_aspect('equal')
    ax.legend(fontsize=10, loc='lower right')
    plt.tight_layout()
    plt.show()


def Biplot():
    df = pd.read_csv('data/Country-data.csv')
    features = ['child_mort', 'exports', 'health', 'imports',
                'income', 'inflation', 'life_expec', 'total_fer', 'gdpp']

    X = df[features].dropna()
    idx = X.index
    countries = df.loc[idx, 'country'].values

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    pca = PCA(n_components=2)
    scores = pca.fit_transform(X_scaled)   # shape (n, 2) — posición real de países
    loadings = pca.components_.T           # shape (9, 2) — dirección de variables

    # ── Escala correcta: loadings → rango de scores ───────────────────
    # Los scores van hasta ~7, loadings hasta ~0.67 → factor ~7
    scale = np.max(np.abs(scores)) / np.max(np.abs(loadings)) * 0.75
    loadings_scaled = loadings * scale

    fig, ax = plt.subplots(figsize=(13, 10))
    fig.patch.set_facecolor('#F8F7F4')
    ax.set_facecolor('#F8F7F4')

    # ── Puntos: países en su posición real en el espacio PCA ──────────
    ax.scatter(scores[:, 0], scores[:, 1],
               color='steelblue', alpha=0.5, s=45, zorder=2)

    # Etiquetar países más extremos (top 15% por distancia al origen)
    distances = np.sqrt(scores[:, 0]**2 + scores[:, 1]**2)
    threshold = np.percentile(distances, 85)
    for i, country in enumerate(countries):
        if distances[i] >= threshold:
            ax.text(scores[i, 0] + 0.1, scores[i, 1] + 0.1,
                    country, fontsize=7.5, color='navy', alpha=0.9)

    # ── Flechas: loadings escalados al espacio de scores ─────────────
    colors_feat = ['#E24B4A', '#3481C8', '#1D9E75', '#8B5CF6',
                   '#F59E0B', '#EC4899', '#14B8A6', '#D85A30', '#6366F1']
    for i, feature in enumerate(features):
        lx, ly = loadings_scaled[i, 0], loadings_scaled[i, 1]
        ax.annotate('', xy=(lx, ly), xytext=(0, 0),
                    arrowprops=dict(arrowstyle='->', color=colors_feat[i],
                                   lw=2.2, mutation_scale=18))
        norm = np.sqrt(lx**2 + ly**2 + 1e-9)
        offset = 0.5
        ax.text(lx + lx / norm * offset,
                ly + ly / norm * offset,
                feature, fontsize=10, color=colors_feat[i],
                fontweight='bold', ha='center')

    # ── Líneas de referencia ──────────────────────────────────────────
    ax.axhline(0, color='#AAAAAA', linewidth=0.8, linestyle='--', zorder=1)
    ax.axvline(0, color='#AAAAAA', linewidth=0.8, linestyle='--', zorder=1)

    ax.set_xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}%)', fontsize=12)
    ax.set_ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.1f}%)', fontsize=12)
    ax.set_title('Biplot PCA — Country Data\n'
                 'Puntos = países (scores reales) · Flechas = variables (loadings escalados)',
                 fontsize=14, fontweight='bold')

    ax.spines[['top', 'right']].set_visible(False)
    plt.tight_layout()
    plt.show()


def Plano_Principal():
    df = pd.read_csv('data/Country-data.csv')
    features = ['child_mort', 'exports', 'health', 'imports',
                'income', 'inflation', 'life_expec', 'total_fer', 'gdpp']
    
    X = df[features].dropna()
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
    
    countries = df['country'].dropna().reset_index(drop=True)
    
    fig, ax = plt.subplots(figsize=(14, 10))
    
    # ── Puntos de los países ──────────────────────────
    ax.scatter(X_pca[:, 0], X_pca[:, 1],
               alpha=0.6, color='steelblue', s=50, zorder=2)
    
    # ── Etiquetas solo para outliers ──────────────────
    for i in range(len(X_pca)):
        if abs(X_pca[i, 0]) > 2 or abs(X_pca[i, 1]) > 2:
            ax.text(X_pca[i, 0] + 0.05, X_pca[i, 1] + 0.05,
                    countries[i], fontsize=8, color='navy')
    
    # ── Líneas de referencia ──────────────────────────
    ax.axhline(0, color='black', linewidth=0.8, linestyle='--', alpha=0.5)
    ax.axvline(0, color='black', linewidth=0.8, linestyle='--', alpha=0.5)
    
    ax.set_xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}%)', fontsize=13)
    ax.set_ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.1f}%)', fontsize=13)
    ax.set_title('Plano Principal PC1 vs PC2 - Country Data', fontsize=14)
    plt.tight_layout()
    plt.show()