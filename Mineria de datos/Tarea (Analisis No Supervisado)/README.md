# 📊 Proyecto de Análisis de Datos

Proyecto de análisis de datos con Python que utiliza `pandas`, `matplotlib` y scripts personalizados de datasets.

---

## 📋 Requisitos previos

- [Python 3.9+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)

---

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio
```

### 2. Crear el entorno virtual

**En Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**En macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

> ✅ Sabrás que el entorno está activo cuando veas `(venv)` al inicio de tu terminal.

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

---

## 📦 Dependencias principales

| Librería | Descripción |
|---|---|
| `pandas` | Manipulación y análisis de datos |
| `matplotlib` | Visualización de gráficos |
| `importlib` | Importación dinámica de módulos |

Los scripts personalizados `Dataset_1` y `Dataset_2` se encuentran en la carpeta `scripts/`.

---

## ▶️ Uso

Una vez activo el entorno virtual y con las dependencias instaladas, abre el notebook:

```bash
jupyter notebook
```

En la primera celda del notebook se configura el entorno:

```python
%matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt
import importlib
import scripts.Dataset_1 as gi
import scripts.Dataset_2 as gii

import warnings
warnings.filterwarnings('ignore')
```

---

## 🔄 Desactivar el entorno virtual

Cuando termines de trabajar, desactiva el entorno con:

```bash
deactivate
```

---

## 📁 Estructura del proyecto

```
tu-repositorio/
│
├── scripts/
│   ├── Dataset_1.py
│   └── Dataset_2.py
│
├── notebooks/
│   └── analisis.ipynb
│
├── requirements.txt
└── README.md
```

---

## 🛠️ Solución de problemas

**El comando `python` no se reconoce:**
Intenta usar `python3` en su lugar (común en macOS/Linux).

**Error al importar `scripts.Dataset_1`:**
Asegúrate de ejecutar el notebook desde la raíz del proyecto, no desde dentro de la carpeta `scripts/`.

**El entorno virtual no se activa en Windows:**
Ejecuta primero este comando en PowerShell:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```