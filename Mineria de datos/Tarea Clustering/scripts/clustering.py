"""
clustering.py
--------------
Funciones para determinar el K optimo y ejecutar los dos algoritmos
pedidos en la tarea: K-Means y Clustering Jerarquico Aglomerativo.
"""

from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.decomposition import PCA
from scipy.cluster.hierarchy import linkage


def elbow_method(X, k_range: range = range(1, 11)) -> list:
    """
    Calcula la Inercia (WCSS) de K-Means para cada valor de K en k_range.
    Se usa para graficar el Metodo del Codo de Jambu y elegir el K optimo.
    """
    inertias = []
    for k in k_range:
        kmeans = KMeans(n_clusters=k, init="k-means++", n_init=10, random_state=42)
        kmeans.fit(X)
        inertias.append(kmeans.inertia_)
    return inertias


def kmeans_clustering(X, n_clusters: int, random_state: int = 42):
    """
    Ejecuta K-Means con el K optimo identificado en el metodo del codo.

    Retorna (labels, modelo_entrenado)
    """
    model = KMeans(n_clusters=n_clusters, init="k-means++", n_init=10,
                    random_state=random_state)
    labels = model.fit_predict(X)
    return labels, model


def hierarchical_clustering(X, n_clusters: int, linkage: str = "ward"):
    """
    Ejecuta Clustering Jerarquico Aglomerativo.

    linkage: 'ward', 'complete' o 'average'

    Retorna labels (array)
    """
    model = AgglomerativeClustering(n_clusters=n_clusters, linkage=linkage)
    labels = model.fit_predict(X)
    return labels


def linkage_matrix(X, method: str = "ward"):
    """
    Genera la matriz de enlace necesaria para graficar el dendrograma.
    """
    return linkage(X, method=method)


def apply_pca(X, n_components: int = 2):
    """
    Reduce la dimensionalidad con PCA para poder visualizar los clusters
    en 2D cuando el dataset tiene mas de 2 variables.

    Retorna (X_pca, varianza_explicada)
    """
    pca = PCA(n_components=n_components, random_state=42)
    X_pca = pca.fit_transform(X)
    return X_pca, pca.explained_variance_ratio_
