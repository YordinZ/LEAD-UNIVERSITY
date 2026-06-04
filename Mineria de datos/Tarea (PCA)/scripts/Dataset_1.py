import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


def Scree_Plot(pca):
    varianza_explicada_acumulada = np.cumsum(pca.explained_variance_ratio_)

    plt.figure(figsize=(10, 6))
    plt.plot(
        range(1, len(varianza_explicada_acumulada) + 1),
        varianza_explicada_acumulada,
        marker='o',
        linestyle='--'
    )

    plt.title('Scree Plot')
    plt.xlabel('Número de Componentes Principales')
    plt.ylabel('Varianza Explicada Acumulada')
    plt.xticks(range(1, len(varianza_explicada_acumulada) + 1))
    plt.grid()
    plt.show()


def Cırculo_Correlacion():
    df = pd.read_csv('data/USA_Cars_Dataset.csv')

    features = ['YEAR', '(kW)', 'COMB (kWh/100 km)', '(km)', 'TIME (h)', 'RATING']
    labels  = ['year', 'power_kw', 'consumption', 'range_km', 'charge_time', 'rating']
    X = df[features].dropna()

    # PCA
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    pca = PCA(n_components=2)
    pca.fit(X_scaled)
    loadings = pca.components_.T  # shape (n_features, 2)

    # ── Figura con 2 subplots ──────────────────────────────────────────
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))
    fig.patch.set_facecolor("#F8F7F4")

    # ── 1. Círculo de correlación ──────────────────────────────────────
    ax1.set_facecolor("#F8F7F4")
    circle = plt.Circle((0, 0), 1, color="#D3D1C7", fill=False, linewidth=1.2)
    ax1.add_patch(circle)
    ax1.axhline(0, color="#D3D1C7", linewidth=0.8, linestyle="--")
    ax1.axvline(0, color="#D3D1C7", linewidth=0.8, linestyle="--")

    colors_feat = ["#3481C8", "#D85A30", "#1D9E75", "#8B5CF6", "#F59E0B", "#EC4899"]

    for i, lbl in enumerate(labels):
        x, y = loadings[i, 0], loadings[i, 1]
        ax1.annotate("", xy=(x, y), xytext=(0, 0),
                    arrowprops=dict(arrowstyle="->", color=colors_feat[i], lw=2))
        offset_x = 0.07 if x >= 0 else -0.07
        offset_y = 0.07 if y >= 0 else -0.07
        ax1.text(x + offset_x, y + offset_y, lbl,
                fontsize=10, color=colors_feat[i], fontweight="bold", ha="center")

    ax1.set_xlim(-1.3, 1.3)
    ax1.set_ylim(-1.3, 1.3)
    ax1.set_aspect("equal")
    ax1.set_xlabel(f"PC1 ({pca.explained_variance_ratio_[0]*100:.1f}%)", fontsize=11, color="#5F5E5A")
    ax1.set_ylabel(f"PC2 ({pca.explained_variance_ratio_[1]*100:.1f}%)", fontsize=11, color="#5F5E5A")
    ax1.set_title("Círculo de correlación\nVariables en espacio PCA", fontsize=12, fontweight="bold", color="#2C2C2A")
    ax1.spines[["top", "right"]].set_visible(False)
    ax1.spines[["left", "bottom"]].set_edgecolor("#D3D1C7")

    # ── 2. Scatter YEAR vs (km) — proxy de valor ──────────────────────
    # Usar solo filas sin nulos en las columnas necesarias
    df_clean = df[['YEAR', '(km)', '(kW)']].dropna()

    ax2.set_facecolor("#F8F7F4")
    scatter = ax2.scatter(
        df_clean['YEAR'], df_clean['(km)'],
        c=df_clean['(kW)'], cmap='RdYlGn',
        s=60, alpha=0.8, edgecolors='white', linewidth=0.5
    )
    cbar = plt.colorbar(scatter, ax=ax2)
    cbar.set_label('Potencia (kW)', fontsize=10, color="#5F5E5A")

    # Línea de tendencia
    z = np.polyfit(df_clean['YEAR'], df_clean['(km)'], 1)
    p = np.poly1d(z)
    x_line = np.linspace(df_clean['YEAR'].min(), df_clean['YEAR'].max(), 100)
    ax2.plot(x_line, p(x_line), color="#D85A30", linewidth=2, linestyle="--", label="Tendencia")

    ax2.set_xlabel("Año", fontsize=11, color="#5F5E5A")
    ax2.set_ylabel("Autonomía (km) — proxy de valor", fontsize=11, color="#5F5E5A")
    ax2.set_title("Año vs Autonomía\nColoreado por potencia (kW)", fontsize=12, fontweight="bold", color="#2C2C2A")
    ax2.legend(fontsize=10, framealpha=0)
    ax2.spines[["top", "right"]].set_visible(False)
    ax2.spines[["left", "bottom"]].set_edgecolor("#D3D1C7")
    ax2.set_xticks(sorted(df_clean['YEAR'].unique()))

    plt.suptitle("Relación de variables — EV Dataset", fontsize=14, fontweight="bold", color="#2C2C2A", y=1.01)
    plt.tight_layout()
    plt.show()

    # ── Correlaciones numéricas ────────────────────────────────────────
    print("=== Correlaciones con (km) — autonomía / proxy de valor ===")
    print(df[features].corr()['(km)'].sort_values(ascending=False).to_string())
    print()
    print("=== Correlaciones con (kW) — potencia ===")
    print(df[features].corr()['(kW)'].sort_values(ascending=False).to_string())


def Biplot():
    # ── Datos ──────────────────────────────────────────────────────────
    df = pd.read_csv('data/USA_Cars_Dataset.csv')
 
    # Solo variables no redundantes (se eliminaron CITY y COMB por correlación >0.95)
    features = ['(kW)', 'HWY (kWh/100 km)', '(km)', 'TIME (h)']
    labels_feat = ['Potencia\n(kW)', 'Consumo\nCarretera', 'Autonomía\n(km)', 'T. Carga\n(h)']
 
    X = df[features].dropna()
    idx = X.index
 
    # ── PCA ────────────────────────────────────────────────────────────
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    pca = PCA(n_components=2)
    scores = pca.fit_transform(X_scaled)
    loadings = pca.components_.T
 
    scale = np.max(np.abs(scores)) / np.max(np.abs(loadings)) * 0.75
 
    # ── Colores por marca ──────────────────────────────────────────────
    brands = df.loc[idx, 'Brand'].values
    brand_list = sorted(df['Brand'].unique())
    palette = {
        'BMW':       '#3481C8',
        'CHEVROLET': '#D85A30',
        'FORD':      '#1D9E75',
        'KIA':       '#8B5CF6',
        'MITSUBISHI':'#F59E0B',
        'NISSAN':    '#EC4899',
        'SMART':     '#14B8A6',
        'TESLA':     '#E24B4A',
    }
    colors_pts = [palette[b] for b in brands]
 
    # ── Colores de flechas ─────────────────────────────────────────────
    arrow_colors = ['#3481C8', '#1D9E75', '#8B5CF6', '#F59E0B']
 
    # ── Figura ─────────────────────────────────────────────────────────
    fig, ax = plt.subplots(figsize=(11, 8))
    fig.patch.set_facecolor('#F8F7F4')
    ax.set_facecolor('#F8F7F4')
    ax.set_ylim(-2.8, 3.5)  # ampliar hacia arriba
 
    # — Scatter por marca —
    for brand in brand_list:
        mask = brands == brand
        ax.scatter(
            scores[mask, 0], scores[mask, 1],
            c=palette[brand], s=70, alpha=0.88,
            edgecolors='white', linewidth=0.6,
            label=brand, zorder=3
        )
 
    # — Flechas de loadings —
    for i, (label, c) in enumerate(zip(labels_feat, arrow_colors)):
        x = loadings[i, 0] * scale
        y = loadings[i, 1] * scale
        ax.annotate(
            '', xy=(x, y), xytext=(0, 0),
            arrowprops=dict(arrowstyle='->', color=c, lw=2.2, mutation_scale=18)
        )
        norm = np.sqrt(x**2 + y**2 + 1e-9)
        offset = 0.4
        ax.text(
            x * (1 + offset / norm),
            y * (1 + offset / norm),
            label, fontsize=9, color=c, fontweight='bold',
            ha='center', va='center'
        )
 
    # — Líneas de referencia —
    ax.axhline(0, color='#D3D1C7', linewidth=0.8, linestyle='--', zorder=1)
    ax.axvline(0, color='#D3D1C7', linewidth=0.8, linestyle='--', zorder=1)
 
    # — Leyenda de marcas —
    ax.legend(
        title='Marca', fontsize=8, title_fontsize=9,
        framealpha=0.5, facecolor='#F8F7F4',
        edgecolor='#D3D1C7', loc='lower left'
    )
 
    # — Etiquetas y título —
    pc1_var = pca.explained_variance_ratio_[0] * 100
    pc2_var = pca.explained_variance_ratio_[1] * 100
    ax.set_xlabel(f'PC1 — {pc1_var:.1f}% varianza explicada', fontsize=11, color='#5F5E5A')
    ax.set_ylabel(f'PC2 — {pc2_var:.1f}% varianza explicada', fontsize=11, color='#5F5E5A')
    ax.set_title(
        'Biplot PCA — Vehículos Eléctricos (USA)\n'
        'Variables independientes: Potencia · Consumo Carretera · Autonomía · T. Carga',
        fontsize=13, fontweight='bold', color='#2C2C2A', pad=14
    )
 
    ax.spines[['top', 'right']].set_visible(False)
    ax.spines[['left', 'bottom']].set_edgecolor('#D3D1C7')
 
    plt.tight_layout()
    plt.show()
 

def Plano_Principal():
    # ── Datos ──────────────────────────────────────────────────────────
    df = pd.read_csv('data/USA_Cars_Dataset.csv')
 
    # Solo variables no redundantes (se eliminaron CITY y COMB por correlación >0.95)
    features = ['(kW)', 'HWY (kWh/100 km)', '(km)', 'TIME (h)']
 
    X = df[features].dropna()
    idx = X.index
 
    # ── PCA ────────────────────────────────────────────────────────────
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    pca = PCA(n_components=2)
    scores = pca.fit_transform(X_scaled)
 
    # ── Colores por marca ──────────────────────────────────────────────
    brands = df.loc[idx, 'Brand'].values
    brand_list = sorted(df['Brand'].unique())
    palette = {
        'BMW':        '#3481C8',
        'CHEVROLET':  '#D85A30',
        'FORD':       '#1D9E75',
        'KIA':        '#8B5CF6',
        'MITSUBISHI': '#F59E0B',
        'NISSAN':     '#EC4899',
        'SMART':      '#14B8A6',
        'TESLA':      '#EF4444',
    }
 
    # ── Figura ─────────────────────────────────────────────────────────
    fig, ax = plt.subplots(figsize=(11, 8))
    fig.patch.set_facecolor('#F8F7F4')
    ax.set_facecolor('#F8F7F4')
 
    # — Scatter por marca —
    for brand in brand_list:
        mask = brands == brand
        ax.scatter(
            scores[mask, 0], scores[mask, 1],
            c=palette[brand], s=80, alpha=0.88,
            edgecolors='white', linewidth=0.6,
            label=brand, zorder=3
        )
 
    # — Anotar solo los 10 puntos más alejados del origen —
    models = df.loc[idx, 'Model'].values
    years  = df.loc[idx, 'YEAR'].values
    distances = np.sqrt(scores[:, 0]**2 + scores[:, 1]**2)
    top_idx = np.argsort(distances)[-10:]
 
    for i in top_idx:
        ax.annotate(
            f"{models[i]} {years[i]}",
            xy=(scores[i, 0], scores[i, 1]),
            xytext=(5, 5), textcoords='offset points',
            fontsize=7, color='#5F5E5A', alpha=0.9
        )
 
    # — Líneas de referencia —
    ax.axhline(0, color='#D3D1C7', linewidth=0.9, linestyle='--', zorder=1)
    ax.axvline(0, color='#D3D1C7', linewidth=0.9, linestyle='--', zorder=1)
 
    # — Leyenda —
    ax.legend(
        title='Marca', fontsize=8, title_fontsize=9,
        framealpha=0.5, facecolor='#F8F7F4',
        edgecolor='#D3D1C7', loc='upper left'
    )
 
    # — Etiquetas y título —
    pc1_var = pca.explained_variance_ratio_[0] * 100
    pc2_var = pca.explained_variance_ratio_[1] * 100
 
    ax.set_xlabel(f'PC1 — {pc1_var:.1f}% varianza explicada', fontsize=11, color='#5F5E5A')
    ax.set_ylabel(f'PC2 — {pc2_var:.1f}% varianza explicada', fontsize=11, color='#5F5E5A')
    ax.set_title(
        'Plano Principal — PC1 vs PC2\n'
        'Proyección de vehículos eléctricos en espacio reducido',
        fontsize=13, fontweight='bold', color='#2C2C2A', pad=14
    )
 
    ax.spines[['top', 'right']].set_visible(False)
    ax.spines[['left', 'bottom']].set_edgecolor('#D3D1C7')
 
    plt.tight_layout()
    plt.show()