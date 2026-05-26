import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def Composicion_Categorica(df, hue=None):  
    vars_macro = ['Protein (g)', 'Carbohydrates (g)', 'Fat (g)']
    
    # Top 10 categorías con más registros
    top10 = df['Category'].value_counts().nlargest(10).index
    df_top = df[df['Category'].isin(top10)]
    
    # Promedio de macronutrientes por categoría
    df_grouped = df_top.groupby('Category')[vars_macro].mean()
    
    # Barras apiladas
    fig, ax = plt.subplots(figsize=(12, 6), dpi=100)
    df_grouped.plot(
        kind='bar',
        stacked=True,
        color=['#FF5733', '#33C1FF', '#FF8C33'],
        ax=ax
    )
    
    ax.set_ylabel('Promedio')
    ax.set_title('Composición de Macronutrientes por Categoría (Top 10)')
    ax.legend(title='Macronutrientes')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


def Relacion_Caloricas(df, hue=None):
    from statsmodels.nonparametric.smoothers_lowess import lowess
    
    fig, ax = plt.subplots(figsize=(8, 6), dpi=100)
    
    # Scatter
    ax.scatter(df['Fat (g)'], df['Calories (kcal)'], 
               alpha=0.4, color='#33C1FF', s=20)
    
    # LOWESS
    smoothed = lowess(df['Calories (kcal)'], df['Fat (g)'], frac=0.3)
    ax.plot(smoothed[:, 0], smoothed[:, 1], 
            color='#FF5733', linewidth=2, label='LOWESS')
    
    ax.set_xlabel('Fat (g)')
    ax.set_ylabel('Calories (kcal)')
    ax.set_title('Scatter: Fat vs Calories con regresión LOWESS')
    ax.legend()
    plt.tight_layout()
    plt.show()


def ANOVA_Sugar(df, hue=None):
    from scipy.stats import f_oneway

    grupo1 = df[df['Category'] == 'Fruit']['Sugars (g)']
    grupo2 = df[df['Category'] == 'Grain']['Sugars (g)']

    f_stat, p_value = f_oneway(grupo1, grupo2)

    print(f'F-statistic: {f_stat}')
    print(f'Valor p: {p_value:.4f}')
    print(f'Resultado: {"Diferencia significativa" if p_value < 0.05 else "Sin diferencia significativa"}')


def PostHoc_Sugar(df, hue=None):
    fig, ax = plt.subplots(figsize=(8, 6), dpi=100)
    
    df_filtrado = df[df['Category'].isin(['Fruit', 'Grain'])]
    
    sns.boxplot(
        data=df_filtrado,
        x='Category',
        y='Sugars (g)',
        palette=['#FF5733', '#33C1FF'],
        ax=ax
    )
    
    ax.set_title('Distribución de Azúcar: Fruit vs Grain')
    ax.set_xlabel('Categoría')
    ax.set_ylabel('Sugars (g)')
    plt.tight_layout()
    plt.show()


def Regresion_Lineal_Multiple(df, hue=None):
    import statsmodels.api as sm

    X = df[['Protein (g)', 'Carbohydrates (g)', 'Fat (g)', 'Sugars (g)']]
    X = sm.add_constant(X)
    y = df['Calories (kcal)']

    model = sm.OLS(y, X)
    result = model.fit()
    print(result.summary())