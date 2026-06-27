# Reducción de Dimensionalidad — Métodos No Supervisados

**Lead University · Minería de Datos I**

Comparación de tres métodos de reducción de dimensionalidad (ACP, t-SNE y UMAP) aplicados a datasets de distinta naturaleza, evaluando la calidad de separación de clusters mediante el Silhouette Score en proyecciones 2D y 3D.

---

## Datasets

| # | Archivo | Descripción | Variable objetivo |
|---|---------|-------------|-------------------|
| 1 | `ropa.csv` | Fashion-MNIST — 784 variables de píxeles por prenda | 10 categorías de ropa |
| 2 | `winequality.csv` | Variables fisicoquímicas de vino | Calidad (escala 3–8) |
| 3 | `Players1.csv` | Estadísticas de jugadores de baloncesto | Posición / arquetipo |

---

## Estructura del proyecto

```
.
├── data/
│   ├── ropa.csv
│   ├── winequality.csv
│   └── Players1.csv
├── scripts/
│   ├── Dataset_1.py          # Funciones ACP, t-SNE, UMAP — Ropa
│   ├── Dataset_2.py          # Funciones ACP, t-SNE, UMAP — Winequality
│   └── Dataset_3.py          # Funciones ACP, t-SNE, UMAP — Players1
├── Reduccion_dimensionalidad_Ropa.ipynb
├── Reduccion_dimensionalidad_Winequality.ipynb
├── Reduccion_dimensionalidad_Players1.ipynb
└── README.md
```

---

## Métodos aplicados

- **ACP (Análisis de Componentes Principales)** — reducción lineal, maximiza la varianza global
- **t-SNE** — reducción no lineal, preserva estructura local y forma clusters compactos
- **UMAP** — reducción no lineal, preserva estructura local y global simultáneamente

Cada notebook aplica los tres métodos en **2D y 3D** y compara los resultados con el **Silhouette Score**.

---

## Resultados principales

### Dataset 1 — Ropa (Fashion-MNIST)

| Método | 2D | 3D |
|--------|----|----|
| UMAP | **0.1932** | **0.1865** |
| t-SNE | 0.1454 | 0.1211 |
| ACP | −0.0313 | 0.0097 |

UMAP fue el mejor método en ambas dimensiones. ACP capturó solo el 37.2% de la varianza con 2 componentes, produciendo un score negativo que indica solapamiento mayor al aleatorio.

### Dataset 2 — Winequality

Las clases de calidad son continuas y adyacentes (5, 6 y 7 concentran la mayoría de muestras), lo que dificulta la separación en cualquier método. UMAP reveló la gradación de calidad de forma más clara, con calidades extremas (3–4 y 8) alejadas del núcleo central.

### Dataset 3 — Players1

Sin etiquetas predefinidas, los clusters emergentes corresponden a arquetipos de jugadores. ACP ofrece mayor interpretabilidad de variables; UMAP produce la mejor separación de perfiles; t-SNE es útil para detectar outliers.

---

## Requisitos

```
pandas
numpy
scikit-learn
umap-learn
matplotlib
plotly
```

Instalar con:

```bash
pip install -r requirements.txt
```

---

## Ejecución

Abrir cada notebook en Jupyter y ejecutar las celdas en orden. Los módulos en `scripts/` se recargan con `importlib.reload` para reflejar cambios sin reiniciar el kernel.

```bash
jupyter notebook Reduccion_dimensionalidad_Ropa.ipynb
```

---

**Yordin Herrera · LEAD University · 2025**