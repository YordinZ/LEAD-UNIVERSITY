import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


VAR_SOCIAL = ['social_energy', 'talkativeness', 'deep_reflection', 'personality_type']


def Distribuciones_Cruzadas(df, hue=None):
    fig= sns.pairplot(
        df[VAR_SOCIAL],
        diag_kind='kde',
        hue=hue)
    plt.show()


def Analisis_Outliers(df, hue=None):
    fig, ax= plt.subplots(figsize=(5, 5), dpi=100)
    
    sns.boxplot(
        x='personality_type',
        y='risk_taking',
        data=df,
        ax=ax)
    plt.title('Boxplot de Risk Taking por Tipo de Personalidad') #plt.subplots retorna tupla (fig, ax), no solo fig.
    plt.show()


def Estructura_Correlacional(df, hue=None):
    corr= df[VAR_SOCIAL].select_dtypes(include='number').corr()

    sns.heatmap(
        corr,
        annot=True,
        cmap='coolwarm',
        fmt='.2f',)
    
    plt.title('Mapa de Calor de Correlaciones')
    plt.show()


def Prueba_t_student(df, variable, hue=None):
    from scipy.stats import f_oneway

    # Filtrar los datos por tipo de personalidad
    grupo1 = df[df['personality_type'] == 'Introvert'][variable]
    grupo2 = df[df['personality_type'] == 'Extrovert'][variable]

    # Realizar la prueba t de Student
    t_stat, p_value = f_oneway(grupo1, grupo2)

    print(f'Variable: {variable}')
    print(f'Estadístico t: {t_stat}')
    print(f'Valor p: {p_value:.4f}')
    print(f'Resultado: {"Diferencia significativa" if p_value < 0.05 else "Sin diferencia significativa"}')


def Analisis_MANOVA(df):
    from statsmodels.multivariate.manova import MANOVA

    formula = 'empathy + listening_skill + friendliness ~ personality_type'
    manova = MANOVA.from_formula(formula, data=df)
    print(manova.mv_test())

def Regresion_Logistica(df, hue=None):
    import statsmodels.api as sm

    df['high_leadership'] = (df['leadership'] > 7.5).astype(int)

    x= df[['public_speaking_comfort', 'stress_handling', 'organization']]
    x= sm.add_constant(x)

    y= df['high_leadership']
    model= sm.Logit(y, x)

    result= model.fit()
    print(result.summary())