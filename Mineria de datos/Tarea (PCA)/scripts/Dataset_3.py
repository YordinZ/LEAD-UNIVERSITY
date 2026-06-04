import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


def Scree_Plot():
    df = pd.read_csv('data/Telco_Customer_Churn.csv')

    # Encoding de variables categóricas binarias
    binary_map = {'Yes': 1, 'No': 0}
    for col in ['Dependents', 'Partner', 'PaperlessBilling']:
        df[col] = df[col].map(binary_map)
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

    features = ['tenure', 'MonthlyCharges', 'TotalCharges', 'Dependents', 'SeniorCitizen', 'Partner', 'PaperlessBilling']
    X = df[features].dropna()

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    pca = PCA(n_components=len(features))
    pca.fit(X_scaled)

    varianza = pca.explained_variance_ratio_ * 100
    varianza_acumulada = np.cumsum(varianza)
    componentes = [f'PC{i+1}' for i in range(len(features))]

    fig, ax1 = plt.subplots(figsize=(9, 5))

    # Barras de varianza individual
    ax1.bar(componentes, varianza, color='steelblue', alpha=0.7, label='Varianza explicada (%)')
    ax1.set_xlabel('Componente Principal', fontsize=12)
    ax1.set_ylabel('Varianza explicada (%)', fontsize=12, color='steelblue')
    ax1.tick_params(axis='y', labelcolor='steelblue')
    ax1.set_ylim(0, max(varianza) * 1.25)

    # Valores sobre cada barra
    for i, v in enumerate(varianza):
        ax1.text(i, v + 0.5, f'{v:.1f}%', ha='center', fontsize=9, color='steelblue')

    # Línea de varianza acumulada (eje secundario)
    ax2 = ax1.twinx()
    ax2.plot(componentes, varianza_acumulada, color='darkred', marker='o',
             linewidth=2, markersize=6, label='Varianza acumulada (%)')
    ax2.set_ylabel('Varianza acumulada (%)', fontsize=12, color='darkred')
    ax2.tick_params(axis='y', labelcolor='darkred')
    ax2.set_ylim(0, 115)

    # Línea de referencia al 80%
    ax2.axhline(80, color='gray', linewidth=1, linestyle='--', alpha=0.7)
    ax2.text(len(features) - 1, 81.5, '80%', ha='right', fontsize=9, color='gray')

    # Valores sobre la línea acumulada
    for i, v in enumerate(varianza_acumulada):
        ax2.text(i, v + 2, f'{v:.1f}%', ha='center', fontsize=9, color='darkred')

    # Leyenda combinada
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='center right', fontsize=10)

    ax1.set_title('Scree Plot - PCA Telco Churn', fontsize=14)
    plt.tight_layout()
    plt.show()


def Circulo_Correlacion():
    df = pd.read_csv('data/Telco_Customer_Churn.csv')
    
    # Encoding de variables categóricas binarias
    binary_map = {'Yes': 1, 'No': 0}
    for col in ['Dependents', 'Partner', 'PaperlessBilling']:
        df[col] = df[col].map(binary_map)
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

    features = ['tenure', 'MonthlyCharges', 'TotalCharges', 'Dependents', 'SeniorCitizen', 'Partner', 'PaperlessBilling']
    X = df[features].dropna()

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    pca = PCA(n_components=2)
    pca.fit(X_scaled)
    loadings = pca.components_.T  # forma (7, 2)

    fig, ax = plt.subplots(figsize=(8, 8))

    # Círculo unitario de referencia
    circulo = plt.Circle((0, 0), 1, color='gray', fill=False, linestyle='--', linewidth=1)
    ax.add_patch(circulo)

    # Flechas y etiquetas por variable
    for i, feature in enumerate(features):
        ax.annotate('',
                    xy=(loadings[i, 0], loadings[i, 1]),
                    xytext=(0, 0),
                    arrowprops=dict(arrowstyle='->', color='steelblue', lw=2))
        ax.text(loadings[i, 0] * 1.15, loadings[i, 1] * 1.15,
                feature, fontsize=10, ha='center', color='darkred')

    # Líneas de referencia
    ax.axhline(0, color='black', linewidth=0.5, linestyle='--')
    ax.axvline(0, color='black', linewidth=0.5, linestyle='--')

    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.3, 1.3)
    ax.set_xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}%)', fontsize=12)
    ax.set_ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.1f}%)', fontsize=12)
    ax.set_title('Círculo de Correlación - Churn', fontsize=14)
    ax.set_aspect('equal')
    plt.tight_layout()
    plt.show()


def Biplot():
    df = pd.read_csv('data/Telco_Customer_Churn.csv')

    # Encoding de variables categóricas binarias
    binary_map = {'Yes': 1, 'No': 0}
    for col in ['Dependents', 'Partner', 'PaperlessBilling']:
        df[col] = df[col].map(binary_map)
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

    features = ['tenure', 'MonthlyCharges', 'TotalCharges', 'Dependents', 'SeniorCitizen', 'Partner', 'PaperlessBilling']
    X = df[features].dropna()

    # Conservar columna Churn alineada tras dropna
    churn = df.loc[X.index, 'Churn'].map({'Yes': 1, 'No': 0}).values

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    pca = PCA(n_components=2)
    scores = pca.fit_transform(X_scaled)
    loadings = pca.components_.T
    scale = np.sqrt(pca.explained_variance_)

    fig, ax = plt.subplots(figsize=(10, 8))

    # Scatter de observaciones coloreadas por Churn
    colors = np.where(churn == 1, '#E24B4A', '#3B8BD4')
    ax.scatter(scores[:, 0], scores[:, 1],
               c=colors, alpha=0.25, s=12, linewidths=0)

    # Leyenda manual Churn
    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0], [0], marker='o', color='w', markerfacecolor='#E24B4A', markersize=8, label='Churn: Yes'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor='#3B8BD4', markersize=8, label='Churn: No')
    ]
    ax.legend(handles=legend_elements, loc='upper left', fontsize=10)

    # Vectores de loadings escalados
    arrow_scale = scale[0] * 2.2
    for i, feature in enumerate(features):
        lx = loadings[i, 0] * arrow_scale
        ly = loadings[i, 1] * arrow_scale
        ax.annotate('',
                    xy=(lx, ly),
                    xytext=(0, 0),
                    arrowprops=dict(arrowstyle='->', color='darkred', lw=1.8))
        ax.text(lx * 1.12, ly * 1.12,
                feature, fontsize=9, ha='center', color='darkred', fontweight='bold')

    # Líneas de referencia
    ax.axhline(0, color='black', linewidth=0.5, linestyle='--')
    ax.axvline(0, color='black', linewidth=0.5, linestyle='--')

    ax.set_xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}%)', fontsize=12)
    ax.set_ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.1f}%)', fontsize=12)
    ax.set_title('Biplot PCA - Telco Churn', fontsize=14)
    plt.tight_layout()
    plt.show()


def Plano_Principal():
    df = pd.read_csv('data/Telco_Customer_Churn.csv')

    # Encoding
    binary_map = {'Yes': 1, 'No': 0}
    for col in ['Dependents', 'Partner', 'PaperlessBilling']:
        df[col] = df[col].map(binary_map)
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

    features = ['tenure', 'MonthlyCharges', 'TotalCharges', 'Dependents',
                'SeniorCitizen', 'Partner', 'PaperlessBilling']
    X = df[features].dropna()
    churn = df.loc[X.index, 'Churn'].map({'Yes': 1, 'No': 0}).values

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    pca = PCA(n_components=2)
    scores = pca.fit_transform(X_scaled)

    # --- Identificar las 2 variables con mayor contribución a PC1 y PC2 ---
    loadings = pca.components_.T
    contrib_pc1 = np.abs(loadings[:, 0])
    contrib_pc2 = np.abs(loadings[:, 1])

    top_pc1 = np.argsort(contrib_pc1)[-2:]  # 2 mejores en PC1
    top_pc2 = np.argsort(contrib_pc2)[-2:]  # 2 mejores en PC2
    top_idx = list(set(top_pc1.tolist() + top_pc2.tolist()))
    top_features = [features[i] for i in top_idx]

    # --- Figura con 3 paneles ---
    fig = plt.figure(figsize=(16, 6))
    fig.suptitle('Plano Principal PCA - Telco Churn', fontsize=15, fontweight='bold')

    colors_map = np.where(churn == 1, '#E24B4A', '#3B8BD4')

    # ── Panel 1: Plano principal PC1 vs PC2 ──────────────────────────────
    ax1 = fig.add_subplot(1, 3, 1)
    ax1.scatter(scores[:, 0], scores[:, 1],
                c=colors_map, alpha=0.2, s=10, linewidths=0)
    ax1.axhline(0, color='black', linewidth=0.5, linestyle='--')
    ax1.axvline(0, color='black', linewidth=0.5, linestyle='--')
    ax1.set_xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}%)', fontsize=11)
    ax1.set_ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.1f}%)', fontsize=11)
    ax1.set_title('Plano Principal\nPC1 vs PC2', fontsize=11)

    # Centroides de Churn
    for label, color, name in [(1, '#E24B4A', 'Churn'), (0, '#3B8BD4', 'No Churn')]:
        mask = churn == label
        cx, cy = scores[mask, 0].mean(), scores[mask, 1].mean()
        ax1.scatter(cx, cy, c=color, s=120, marker='X', edgecolors='white',
                    linewidths=1.2, zorder=5, label=name)
    ax1.legend(fontsize=9, loc='upper right')

    # ── Panel 2: Variables top PC1 coloreadas por Churn ──────────────────
    ax2 = fig.add_subplot(1, 3, 2)
    feat_pc1 = [features[i] for i in top_pc1]
    x2 = df.loc[X.index, feat_pc1[0]].values
    y2 = df.loc[X.index, feat_pc1[1]].values

    ax2.scatter(x2[churn == 0], y2[churn == 0],
                c='#3B8BD4', alpha=0.25, s=10, linewidths=0, label='No Churn')
    ax2.scatter(x2[churn == 1], y2[churn == 1],
                c='#E24B4A', alpha=0.35, s=10, linewidths=0, label='Churn')

    # Centroides
    for label, color in [(0, '#3B8BD4'), (1, '#E24B4A')]:
        mask = churn == label
        ax2.scatter(x2[mask].mean(), y2[mask].mean(),
                    c=color, s=120, marker='X', edgecolors='white',
                    linewidths=1.2, zorder=5)

    ax2.set_xlabel(feat_pc1[0], fontsize=11)
    ax2.set_ylabel(feat_pc1[1], fontsize=11)
    ax2.set_title(f'Top variables PC1\n{feat_pc1[0]} vs {feat_pc1[1]}', fontsize=11)
    ax2.legend(fontsize=9)

    # ── Panel 3: Variables top PC2 coloreadas por Churn ──────────────────
    ax3 = fig.add_subplot(1, 3, 3)
    feat_pc2 = [features[i] for i in top_pc2]
    x3 = df.loc[X.index, feat_pc2[0]].values
    y3 = df.loc[X.index, feat_pc2[1]].values

    ax3.scatter(x3[churn == 0], y3[churn == 0],
                c='#3B8BD4', alpha=0.25, s=10, linewidths=0, label='No Churn')
    ax3.scatter(x3[churn == 1], y3[churn == 1],
                c='#E24B4A', alpha=0.35, s=10, linewidths=0, label='Churn')

    for label, color in [(0, '#3B8BD4'), (1, '#E24B4A')]:
        mask = churn == label
        ax3.scatter(x3[mask].mean(), y3[mask].mean(),
                    c=color, s=120, marker='X', edgecolors='white',
                    linewidths=1.2, zorder=5)

    ax3.set_xlabel(feat_pc2[0], fontsize=11)
    ax3.set_ylabel(feat_pc2[1], fontsize=11)
    ax3.set_title(f'Top variables PC2\n{feat_pc2[0]} vs {feat_pc2[1]}', fontsize=11)
    ax3.legend(fontsize=9)

    plt.tight_layout()
    plt.show()

    # --- Reporte en consola ---
    print('Variables con mayor contribución a PC1:')
    for i in np.argsort(contrib_pc1)[::-1]:
        print(f'  {features[i]:<20} {contrib_pc1[i]:.4f}')
    print('\nVariables con mayor contribución a PC2:')
    for i in np.argsort(contrib_pc2)[::-1]:
        print(f'  {features[i]:<20} {contrib_pc2[i]:.4f}')