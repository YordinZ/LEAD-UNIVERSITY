"""
preprocessing.py
-----------------
Funciones reutilizables de carga y preparacion de datos para ambos datasets
(Mall Customers y Palmer Penguins). Se usan desde los notebooks de
dataset1_mall/ y dataset2_penguins/.
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler


def load_data(path: str) -> pd.DataFrame:
    """
    Carga un CSV en un DataFrame de pandas.
    """
    return pd.read_csv(path)


def explore_data(df: pd.DataFrame) -> None:
    """
    Imprime un resumen exploratorio rapido: shape, dtypes, nulos por columna,
    estadisticas descriptivas.
    """
    print(f"Dimensiones: {df.shape[0]} filas x {df.shape[1]} columnas\n")
    print("Tipos de datos:")
    print(df.dtypes, "\n")
    print("Valores nulos por columna:")
    print(df.isnull().sum(), "\n")
    print("Estadisticas descriptivas:")
    print(df.describe(include="all").T)


def handle_missing_values(df: pd.DataFrame, strategy: str = "drop") -> pd.DataFrame:
    """
    Maneja valores nulos segun la estrategia indicada.

    strategy:
        'drop'   -> elimina filas con al menos un nulo
        'mean'   -> imputa columnas numericas con la media
        'median' -> imputa columnas numericas con la mediana
    """
    df = df.copy()

    if strategy == "drop":
        return df.dropna()

    numeric_cols = df.select_dtypes(include="number").columns

    if strategy == "mean":
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
    elif strategy == "median":
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
    else:
        raise ValueError("strategy debe ser 'drop', 'mean' o 'median'")

    return df


def handle_outliers(df: pd.DataFrame, columns: list, method: str = "iqr") -> pd.DataFrame:
    """
    Detecta y trata valores atipicos en las columnas indicadas usando
    el rango intercuartilico (IQR). Los valores fuera de
    [Q1 - 1.5*IQR, Q3 + 1.5*IQR] se eliminan.
    """
    df = df.copy()

    if method != "iqr":
        raise ValueError("Por ahora solo esta implementado el metodo 'iqr'")

    for col in columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        limite_inferior = Q1 - 1.5 * IQR
        limite_superior = Q3 + 1.5 * IQR
        antes = len(df)
        df = df[(df[col] >= limite_inferior) & (df[col] <= limite_superior)]
        eliminados = antes - len(df)
        if eliminados > 0:
            print(f"'{col}': {eliminados} filas eliminadas por outliers (IQR)")

    return df.reset_index(drop=True)


def select_numeric_features(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Selecciona las columnas numericas que se usaran para el clustering.
    """
    faltantes = [c for c in columns if c not in df.columns]
    if faltantes:
        raise ValueError(f"Columnas no encontradas en el DataFrame: {faltantes}")
    return df[columns].copy()


def scale_features(df: pd.DataFrame, method: str = "standard"):
    """
    Normaliza o estandariza las variables numericas antes de aplicar
    K-Means / Clustering Jerarquico.

    method:
        'standard' -> StandardScaler (media 0, desv. 1)
        'minmax'   -> MinMaxScaler (rango 0-1)

    Retorna (array_escalado, scaler_entrenado)
    """
    if method == "standard":
        scaler = StandardScaler()
    elif method == "minmax":
        scaler = MinMaxScaler()
    else:
        raise ValueError("method debe ser 'standard' o 'minmax'")

    X_scaled = scaler.fit_transform(df)
    return X_scaled, scaler
