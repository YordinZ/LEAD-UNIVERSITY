# Reducción de Dimensionalidad — ACM

Tarea de análisis de datos enfocado en técnicas de reducción de dimensionalidad: **Análisis de Correspondencia Múltiple (ACM)**, aplicadas sobre conjuntos de datos categóricos y numéricos.

---

## Requisitos previos

- Python 3.10 o superior instalado
- `pip` actualizado
- Git (opcional, para clonar el repositorio)

---

## Configuración del entorno virtual

Antes de ejecutar el notebook, es necesario crear un entorno virtual e instalar las dependencias listadas en `requirements.txt`. Esto evita conflictos con otras instalaciones de Python en el sistema.

### Windows (CMD)

```cmd
:: 1. Crear el entorno virtual
python -m venv venv

:: 2. Activar el entorno virtual
venv\Scripts\activate.bat

:: 3. Instalar las dependencias
pip install -r requirements.txt
```

### Linux / macOS

```bash
# 1. Crear el entorno virtual
python3 -m venv venv

# 2. Activar el entorno virtual
source venv/bin/activate

# 3. Instalar las dependencias
pip install -r requirements.txt
```

---

## Verificar la instalación

Con el entorno activado, confirme que las librerías quedaron instaladas correctamente:

```bash
pip list
```

Debe aparecer `pandas`, `scikit-learn`, `prince`, `altair`, `matplotlib`, entre otras.

---

## Ejecutar el proyecto

1. Active el entorno virtual (ver pasos anteriores).
2. Inicie Jupyter Notebook o Jupyter Lab:

   ```bash
   jupyter notebook
   ```

3. Abra el archivo `Reduccion_Dimensionalidad_ACM.ipynb` y ejecute las celdas en orden.

---

## Desactivar el entorno virtual

Cuando termine de trabajar, puede salir del entorno virtual con:

```bash
deactivate
```

---

## Estructura de dependencias principales

| Paquete | Uso en el proyecto |
|---|---|
| `pandas` | Manipulación y limpieza de datos |
| `numpy` | Operaciones numéricas |
| `scikit-learn` | Algoritmos de PCA y utilidades de preprocesamiento |
| `prince` | Implementación de Análisis de Correspondencia Múltiple (ACM) |
| `matplotlib` / `seaborn` | Visualizaciones estáticas (Scree Plot, Biplot, Círculo de Correlación) |
| `altair` | Visualizaciones interactivas |
| `jsonschema` | Validación de esquemas usados por Altair |

La lista completa de versiones se encuentra en [`requirements.txt`](./requirements.txt).

---

## Notas

- Se recomienda no instalar las dependencias de forma global; usar siempre el entorno virtual evita conflictos de versiones entre proyectos.
- Si agrega nuevas librerías al proyecto, actualice el archivo `requirements.txt` ejecutando:

  ```bash
  pip freeze > requirements.txt
  ```