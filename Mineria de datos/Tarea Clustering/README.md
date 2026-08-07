# Tarea Práctica: Aprendizaje No Supervisado — K-Means y Clustering Jerárquico

## Estructura

```
tarea_clustering/
├── scripts/                     # funciones reutilizables (importadas por ambos notebooks)
│   ├── preprocessing.py         # carga, limpieza, escalado
│   ├── clustering.py            # codo, K-Means, jerárquico, PCA
│   ├── visualization.py         # gráficos (codo, dendrograma, dispersión)
│   └── style.py                 # paleta y tipografía del proyecto
├── data/
│   ├── dataset1_mall/            # colocar aquí el CSV de Mall Customer Segmentation
│   └── dataset2_penguins/        # colocar aquí el CSV de Palmer Penguins
├── dataset1_mall/
│   └── analisis_dataset1_mall.ipynb
├── dataset2_penguins/
│   └── analisis_dataset2_penguins.ipynb
└── main.ipynb                    
```

## Pasos para arrancar

1. Descargar los datasets de Kaggle:
   - **Dataset 1 (negocio):** Mall Customer Segmentation
     https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python
   - **Dataset 2 (científico):** Palmer Penguins
     https://www.kaggle.com/datasets/borhanitrash/palmer-penguins-dataset

2. Guardar los CSV en `data/dataset1_mall/` y `data/dataset2_penguins/` respectivamente.

3. Instalar dependencias:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn scipy
   ```

4. Completar las funciones marcadas con `TODO` en `scripts/` (son el motor que
   usan ambos notebooks).

5. Correr `dataset1_mall/analisis_dataset1_mall.ipynb` y
   `dataset2_penguins/analisis_dataset2_penguins.ipynb` de arriba hacia abajo.

6. Volver a `main.ipynb` y llenar la sección de conclusiones generales
   comparando ambos datasets.
