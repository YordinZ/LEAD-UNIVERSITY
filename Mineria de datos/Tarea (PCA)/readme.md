---

## Descripción de los Datasets

### Dataset 1 — EV Cars Dataset (`USA_Cars_Dataset.csv`)
Dataset de vehículos eléctricos con especificaciones técnicas de múltiples marcas. Contiene variables como potencia `(kW)`, autonomía `(km)`, consumo `COMB (kWh/100 km)` y tiempo de carga `TIME (h)`. La autonomía `(km)` se utiliza como **proxy de valor comercial** dada su correlación con potencia (r = 0.895) y consumo (r = 0.907).

> **Nota:** El dataset original solicitado en el enunciado (`price`, `year`, `mileage`) no contaba con la columna `price`. Se adaptó el análisis utilizando variables técnicas del vehículo eléctrico como indicadores equivalentes de valor y antigüedad.

### Dataset 2 — Country Data (`Country-data.csv`)
Indicadores socioeconómicos de desarrollo por país, incluyendo `child_mort`, `exports`, `health`, `imports`, `income`, `inflation`, `life_expec`, `total_fer` y `gdpp`. El objetivo es segmentar países según su nivel de desarrollo para apoyo humanitario.

### Dataset 3 — Telco Customer Churn (`Telco_Customer_Churn.csv`)
Datos de comportamiento de clientes de una empresa de telecomunicaciones. Variables clave: `tenure`, `MonthlyCharges`, `TotalCharges`, junto con variables categóricas binarias (`Dependents`, `Partner`, `PaperlessBilling`, `SeniorCitizen`) y categóricas multinivel (`Contract`, `PaymentMethod`, `InternetService`, etc.). El objetivo es observar si el PCA logra separar a los clientes con churn de los que no, y comparar esta representación con la obtenida mediante ACM sobre las variables categóricas.

> **Nota:** La columna `TotalCharges` llega como texto. Antes de cualquier análisis (PCA y especialmente ACM) se convierte a numérico y se eliminan los registros vacíos resultantes, evitando que se trate erróneamente como variable categórica de miles de niveles.

---

## Visualizaciones Generadas

Por cada dataset (Datasets 1-3) se generan cuatro visualizaciones obligatorias:

| Visualización | Descripción |
|---|---|
| **Scree Plot** | Varianza explicada individual y acumulada por componente. Justifica cuántos PCs capturan ≥ 80% de la información. |
| **Círculo de Correlación** | Variables originales como vectores en el espacio PCA. Analiza magnitud, dirección y correlaciones entre variables. |
| **Plano Principal (PC1 vs PC2)** | Proyección de observaciones en el espacio reducido, coloreadas por categoría (marca en Cars, churn en Telco). |
| **Biplot** | Superposición de observaciones y loadings para interpretar la posición de los datos en función de sus atributos. |

---

## Análisis Comparativo — ACM vs PCA (Telco Churn)

El dataset Telco contiene numerosas variables categóricas (tipo de contrato, método de pago, servicios contratados) que el PCA estándar no puede tratar directamente. El módulo `ACM_PCA.py` implementa la clase `ACMAnalyzer`, que ajusta ambas técnicas sobre el mismo dataset y permite compararlas:

- **Scree Plot Comparativo** — inercia explicada por dimensión en PCA (sobre variables numéricas + dummies) vs ACM (sobre todas las variables categorizadas).
- **Biplots Comparativos** — individuos y variables/modalidades proyectados en el plano 1-2 para cada método.
- **Comparación de Inercia** — porcentaje de inercia total capturado por Dim 1 y Dim 2 en cada técnica.
- **Contribuciones y cos²** — variables/modalidades que más explican el plano principal, y calidad de representación de los individuos.

```python
from scripts.ACM_PCA import ACMAnalyzer

fx = ACMAnalyzer(df3, id_cols=["customerID"])
fx.fit(n_plot=2)

fx.plot_scree()
fx.plot_biplots()
fx.plot_comparison()
fx.show_contrib_cos2(n=12)
```

---

## Hallazgos Clave por Dataset

### Dataset 1 — EV Cars
- **PC1** captura el eje de *capacidad tecnológica*: autonomía, potencia y consumo cargan en la misma dirección.
- **PC2** separa el tiempo de carga del resto, reflejando diferencias en arquitectura de batería.
- Tesla se ubica consistentemente en el extremo positivo de PC1 (mayor autonomía y potencia). SMART y MITSUBISHI en el extremo opuesto.
- La tendencia temporal muestra que los modelos más recientes tienen mayor autonomía, confirmando la evolución tecnológica del sector.

### Dataset 2 — Country Data
- **PC1** representa el eje de *desarrollo humano*: `gdpp`, `income` y `life_expec` se oponen diametralmente a `child_mort` y `total_fer`.
- **PC2** diferencia países con alta inflación y exportaciones del resto.
- Países como Haití, Sierra Leona y Chad se ubican en el extremo de alta mortalidad infantil en el biplot.
- Con 2 componentes se captura más del 60% de la varianza; se necesitan 4-5 para alcanzar el 80%.
- El plano principal revela tres grupos naturales: países en vías de desarrollo, economías emergentes y naciones de alto ingreso, emergidos directamente de los datos.

### Dataset 3 — Telco Churn (PCA)
- `tenure` y `TotalCharges` presentan **alta colinealidad** (clientes con más tiempo acumulan más cargos totales), ambas cargan fuerte en PC1.
- `MonthlyCharges` carga principalmente en **PC2**, formando un eje casi ortogonal a `tenure`, lo que confirma que son dimensiones independientes del comportamiento del cliente.
- Se requieren aproximadamente 3 componentes para superar el 80% de varianza; PC1 y PC2 capturan cerca del 60%.
- Los clientes que abandonan tienden a agruparse en la zona de alto `MonthlyCharges` y bajo `tenure`. El PCA no separa perfectamente los grupos, pero los centroides de Churn y No-Churn difieren notablemente sobre PC1.

### Dataset 3 — ACM vs PCA
- En **PCA**, las variables con mayor contribución son las continuas de alta varianza (`tenure`, `TotalCharges`, `MonthlyCharges`).
- En **ACM**, las modalidades de tipo de contrato (*Month-to-month*) y método de pago (*Electronic check*) lideran las contribuciones, revelando patrones cualitativos asociados al churn.
- El ACM distribuye la inercia entre más dimensiones que el PCA, ya que cada categoría binaria aporta una columna indicadora independiente, requiriendo más componentes para alcanzar el mismo umbral de inercia acumulada.
- Ambos métodos resultan complementarios: PCA resume mejor las magnitudes financieras, mientras que ACM captura la segmentación por tipo de servicio y comportamiento contractual.

---

## Instalación y Configuración

### 1. Clonar el repositorio y navegar a la carpeta

```bash
git clone https://github.com/YordinZ/LEAD-UNIVERSITY.git
cd "LEAD-UNIVERSITY/Mineria de datos/Tarea (PCA)"
```

### 2. Crear y activar el entorno virtual

```bash
# Crear el entorno
python -m venv venv

# Activar — Windows (CMD)
venv\Scripts\activate

# Activar — macOS / Linux
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install pandas numpy matplotlib scikit-learn prince ipython jupyter
```

### 4. Ejecutar el notebook

```bash
jupyter notebook Reduccion_Dimensionalidad.ipynb
```

> Asegúrate de tener los archivos CSV dentro de la carpeta `data/` antes de ejecutar cualquier celda. En la sección de Telco Churn, ejecuta primero la celda de preparación de `TotalCharges` antes de instanciar `ACMAnalyzer`.

---

## Uso de Módulos Individuales

Cada dataset tiene su propio módulo independiente dentro de `scripts/`. Puedes importar y ejecutar funciones de forma aislada:

```python
from scripts.Dataset_1 import Scree_Plot, Plano_Principal, Biplot, Cırculo_Correlacion
from scripts.Dataset_2 import Scree_Plot, Circulo_Correlacion, Plano_Principal
from scripts.Dataset_3 import Scree_Plot, Circulo_Correlacion, Biplot, Plano_Principal
from scripts.ACM_PCA import ACMAnalyzer
```

---

## Stack Tecnológico

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat&logo=jupyter&logoColor=white)
![Prince](https://img.shields.io/badge/Prince-ACM%2FMCA-b85300?style=flat)