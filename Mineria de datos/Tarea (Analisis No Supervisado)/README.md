# 📊 Análisis No Supervisado — Minería de Datos
**LEAD University** · Curso: Minería de Datos

---

## 📋 Requisitos previos

- [Python 3.9+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)

---

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/YordinZ/LEAD-UNIVERSITY.git
cd "LEAD-UNIVERSITY/Mineria de datos/Tarea (Analisis No Supervisado)"
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

Si no existe un `requirements.txt`, instala manualmente:

```bash
pip install pandas matplotlib jupyter
```

---

## 📦 Librerías utilizadas

| Librería | Alias | Descripción |
|---|---|---|
| `pandas` | `pd` | Manipulación y análisis de datos |
| `matplotlib.pyplot` | `plt` | Visualización de gráficos |
| `importlib` | — | Importación dinámica de módulos |
| `scripts.Dataset_1` | `gi` | Dataset personalizado #1 |
| `scripts.Dataset_2` | `gii` | Dataset personalizado #2 |

---

## ▶️ Uso

Con el entorno virtual activo, lanza Jupyter:

```bash
jupyter notebook
```

Abre el notebook principal. La primera celda configura el entorno automáticamente:

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

```bash
deactivate
```

---

## 📁 Estructura del proyecto

```
Tarea (Analisis No Supervisado)/
│
├── scripts/
│   ├── Dataset_1.py
│   └── Dataset_2.py
│
├── notebook.ipynb
├── requirements.txt
└── README.md
```

---

## 🛠️ Solución de problemas

**Error al importar `scripts.Dataset_1`:**
Asegúrate de ejecutar Jupyter desde la carpeta raíz de la tarea, no desde dentro de `scripts/`.

**El comando `python` no se reconoce:**
Usa `python3` en su lugar (común en macOS/Linux).

**El entorno virtual no se activa en Windows (PowerShell):**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## 🔗 Repositorio

[github.com/YordinZ/LEAD-UNIVERSITY](https://github.com/YordinZ/LEAD-UNIVERSITY)