# Reducción de Dimensionalidad — Análisis de Componentes Principales (PCA)

**Curso:** Minería de Datos I  
**Programa:** Maestría en Ciencia de Datos — LEAD University  
**Repositorio:** [YordinZ/LEAD-UNIVERSITY](https://github.com/YordinZ/LEAD-UNIVERSITY/tree/main/Mineria%20de%20datos/Tarea%20(PCA))  
**Ruta:** `Mineria de datos / Tarea (PCA)`

---

## Estructura del Proyecto

```
Tarea (PCA)/
├── data/
│   ├── USA_Cars_Dataset.csv        # Dataset de vehículos eléctricos
│   ├── Country-data.csv            # Indicadores de desarrollo por país
│   └── Telco_Customer_Churn.csv    # Comportamiento de clientes Telco
│
├── Dataset_1.py                    # Módulo PCA — EV Dataset
├── Dataset_2.py                    # Módulo PCA — Country Data
├── Dataset_3.py                    # Módulo PCA — Telco Churn
├── venv/                           # Entorno virtual (excluido del repositorio)
│
└── Reduccion_Dimensionalidad.ipynb # Notebook principal con análisis completo
```

---

## Descripción de los Datasets

### Dataset 1 — EV Cars Dataset (`USA_Cars_Dataset.csv`)
Dataset de vehículos eléctricos con especificaciones técnicas de múltiples marcas. Contiene variables como potencia `(kW)`, autonomía `(km)`, consumo `COMB (kWh/100 km)` y tiempo de carga `TIME (h)`. La autonomía `(km)` se utiliza como **proxy de valor comercial** dada su correlación con potencia (r = 0.895) y consumo (r = 0.907).

> **Nota:** El dataset original solicitado en el enunciado (`price`, `year`, `mileage`) no contaba con la columna `price`. Se adaptó el análisis utilizando variables técnicas del vehículo eléctrico como indicadores equivalentes de valor y antigüedad.

### Dataset 2 — Country Data (`Country-data.csv`)
Indicadores socioeconómicos de desarrollo por país, incluyendo `child_mort`, `exports`, `health`, `imports`, `income`, `inflation`, `life_expec`, `total_fer` y `gdpp`. El objetivo es segmentar países según su nivel de desarrollo para apoyo humanitario.

### Dataset 3 — Telco Customer Churn (`Telco_Customer_Churn.csv`)
Datos de comportamiento de clientes de una empresa de telecomunicaciones. Variables clave: `tenure`, `MonthlyCharges`, `TotalCharges`, junto con variables categóricas binarias (`Dependents`, `Partner`, `PaperlessBilling`, `SeniorCitizen`). El objetivo es observar si el PCA logra separar clientes con churn de los que no.

---

## Visualizaciones Generadas

Por cada dataset se generan cuatro visualizaciones obligatorias:

| Visualización | Descripción |
|---|---|
| **Scree Plot** | Varianza explicada individual y acumulada por componente. Justifica cuántos PCs capturan ≥ 80% de la información. |
| **Círculo de Correlación** | Variables originales como vectores en el espacio PCA. Analiza magnitud, dirección y correlaciones entre variables. |
| **Plano Principal (PC1 vs PC2)** | Proyección de observaciones en el espacio reducido, coloreadas por categoría (marca en Cars, churn en Telco). |
| **Biplot** | Superposición de observaciones y loadings para interpretar la posición de los datos en función de sus atributos. |

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

### Dataset 3 — Telco Churn
- `tenure` y `TotalCharges` presentan **alta colinealidad** (clientes con más tiempo acumulan más cargos totales), ambas cargan fuerte en PC1.
- `MonthlyCharges` carga principalmente en **PC2**, formando un eje casi ortogonal a `tenure`, lo que confirma que son dimensiones independientes del comportamiento del cliente.
- El PCA no logra separar limpiamente los clientes con churn de los que no, lo que sugiere que el abandono depende de variables categóricas no lineales (tipo de contrato, servicio) más que de las variables numéricas analizadas.

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
pip install pandas numpy matplotlib scikit-learn jupyter
```

### 4. Ejecutar el notebook

```bash
jupyter notebook Reduccion_Dimensionalidad.ipynb
```

> Asegúrate de tener los archivos CSV dentro de la carpeta `data/` antes de ejecutar cualquier celda.

---

## Uso de Módulos Individuales

Cada dataset tiene su propio módulo independiente. Puedes importar y ejecutar funciones de forma aislada:

```python
from Dataset_1 import Scree_Plot, Plano_Principal, Biplot
from Dataset_2 import Scree_Plot, Circulo_Correlacion
from Dataset_3 import Plano_Principal, Biplot
```

---

## Stack Tecnológico

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat&logo=jupyter&logoColor=white)