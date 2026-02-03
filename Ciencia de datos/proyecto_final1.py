import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    ConfusionMatrixDisplay,
)


# =========================
# CARGA Y LIMPIEZA DE DATOS
# =========================

def cargar_datos(ruta_archivo):
    """Carga los datos desde un archivo CSV."""
    return pd.read_csv(ruta_archivo)


def limpiar_datos(df):
    """
    Limpia los datos eliminando columnas sin título explícito
    y filas completamente vacías.
    """
    columnas_sin_titulo = [
        col for col in df.columns
        if pd.isna(col)
        or not str(col).strip()
        or str(col).lower().startswith('unnamed')
    ]

    if columnas_sin_titulo:
        df = df.drop(columns=columnas_sin_titulo)

    df = df.replace(r'^\s*$', np.nan, regex=True)
    df = df.dropna(how='all')

    return df


# ======================================
# TRANSFORMACIÓN DE VARIABLES CATEGÓRICAS
# ======================================

def cambio_alfabetico_a_numerico(df):
    """
    Convierte columnas categóricas a valores numéricos ordenados.
    """
    df = df.copy()

    housing_mapa = {'rent': 0, 'free': 1, 'own': 2}
    savings_mapa = {
        'missing': 0,
        'little': 1,
        'moderate': 2,
        'quite rich': 3,
        'rich': 4,
    }
    checking_mapa = {
        'missing': 0,
        'little': 1,
        'moderate': 2,
        'rich': 3,
    }
    risk_mapa = {'bad': 0, 'good': 1}
    purpose_mapa = {
        'radio/TV': 0,
        'education': 1,
        'furniture/equipment': 2,
        'car': 3,
        'business': 4,
        'domestic appliances': 5,
        'repairs': 6,
        'vacation/others': 7,
    }

    reemplazos = {
        'Housing': housing_mapa,
        'Saving accounts': savings_mapa,
        'Checking account': checking_mapa,
        'Risk': risk_mapa,
        'Purpose': purpose_mapa,
    }

    for columna, mapa in reemplazos.items():
        if columna in df.columns:
            df[columna] = (
                df[columna]
                .astype('object')
                .fillna('missing')
                .replace(mapa)
            )

    return df


# =========================
# PREPARACIÓN DEL MODELO
# =========================

def preparar_datos_modelo(df):
    """Divide los datos en entrenamiento y prueba."""
    variables_entrada = [
        'Age',
        'Housing',
        'Saving accounts',
        'Checking account',
        'Credit amount',
        'Duration',
        'Purpose',
    ]
    objetivo = 'Risk'

    faltantes = [
        col for col in variables_entrada + [objetivo]
        if col not in df.columns
    ]
    if faltantes:
        raise ValueError(
            f'Faltan columnas requeridas en el DataFrame: {faltantes}'
        )

    X = df[variables_entrada].copy()
    y = df[objetivo].copy()

    return train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )


def entrenar_modelo_riesgo(X_train, y_train):
    """Entrena un modelo de regresión logística."""
    modelo = LogisticRegression(max_iter=1000)
    modelo.fit(X_train, y_train)
    return modelo


def evaluar_modelo(modelo, X_test, y_test):
    """Evalúa el modelo con métricas de clasificación."""
    predicciones = modelo.predict(X_test)

    exactitud = accuracy_score(y_test, predicciones)
    reporte = classification_report(
        y_test,
        predicciones,
        target_names=['bad', 'good'],
    )

    print('Exactitud del modelo:')
    print(f'{exactitud:.3f}\n')

    print('Reporte de clasificación:')
    print(reporte)

    return predicciones


# =========================
# FUNCIÓN PRINCIPAL
# =========================

def main():
    """Ejecuta todo el flujo del proyecto."""

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    ruta_csv = os.path.join(BASE_DIR, 'german_credit_data.csv')

    # Carga y preparación de datos
    df = cargar_datos(ruta_csv)
    df_limpio = limpiar_datos(df)
    df_numerico = cambio_alfabetico_a_numerico(df_limpio)

    # Modelo
    X_train, X_test, y_train, y_test = preparar_datos_modelo(df_numerico)
    modelo = entrenar_modelo_riesgo(X_train, y_train)
    predicciones = evaluar_modelo(modelo, X_test, y_test)

    # =========================
    # GRÁFICOS
    # =========================

    # Matriz de confusión
    ConfusionMatrixDisplay.from_predictions(y_test, predicciones)
    plt.title('Matriz de Confusión')
    plt.show()

    # Comparación real vs predicción
    valores_reales = np.bincount(y_test, minlength=2)
    valores_predichos = np.bincount(predicciones, minlength=2)

    etiquetas = ['Bad', 'Good']
    x = np.arange(len(etiquetas))

    plt.bar(x - 0.2, valores_reales, width=0.4, label='Real')
    plt.bar(x + 0.2, valores_predichos, width=0.4, label='Predicho')
    plt.xticks(x, etiquetas)
    plt.ylabel('Cantidad')
    plt.title('Valores reales vs predicciones')
    plt.legend()
    plt.show()

    # Histograma de probabilidades
    probabilidades = modelo.predict_proba(X_test)[:, 1]

    plt.hist(probabilidades, bins=20)
    plt.title('Distribución de probabilidades (Risk = good)')
    plt.xlabel('Probabilidad')
    plt.ylabel('Frecuencia')
    plt.show()


if __name__ == '__main__':
    main()
