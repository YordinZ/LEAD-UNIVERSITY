import prince
import matplotlib.pyplot as plt
import altair as alt

alt.data_transformers.enable("vegafusion")

class ACM:
    def __init__(self, df, n_components=2, sample_n=2000): #modelo entrenado
        # Hacer el sample aquí, una sola vez
        self.df_full = df
        self.df = df.sample(n=min(sample_n, len(df)), random_state=42).reset_index(drop=True)
        self.n_components = n_components
        self.acm = prince.MCA(n_components=self.n_components, random_state=42)
        self.acm_fit = self.acm.fit(self.df)  # entrenar con el sample

    def scree_plot(self):
        eig = self.acm_fit.eigenvalues_summary.copy()

        inercia = eig['% of variance'].astype(str).str.rstrip('%').str.strip().astype(float)
        inercia_acumulada = inercia.cumsum()
        n = len(inercia)

        fig, ax = plt.subplots(figsize=(10, 6))
        bars = ax.bar(range(1, n + 1), inercia, alpha=0.6, label='Inercia explicada (%)')
        ax.plot(range(1, n + 1), inercia_acumulada, marker='o', color='red', label='Inercia acumulada (%)')

        # Valores encima de cada barra
        for i, (v, acum) in enumerate(zip(inercia, inercia_acumulada)):
            ax.text(i + 1, v + 0.3, f'{v:.1f}%', ha='center', va='bottom', fontsize=9)
            ax.text(i + 1, acum + 0.3, f'{acum:.1f}%', ha='center', va='bottom', fontsize=9, color='red')

        ax.set_xlabel("Componente")
        ax.set_ylabel("Porcentaje de inercia (%)")
        ax.set_title("Scree Plot - ACM (Inercia explicada y acumulada)")
        ax.set_xticks(range(1, n + 1))
        ax.legend()
        ax.grid(True)
        plt.tight_layout()
        plt.show()

    def biplot(self, x_component=0, y_component=1):
        chart = self.acm_fit.plot(
            self.df,  # usar el mismo df con el que se entrenó
            x_component=x_component,
            y_component=y_component,
            show_row_markers=True, #individuos
            show_column_markers=True, #categorias
            show_column_labels=True, #categorias
        )
        return chart.properties(
        width=600,
        height=600,
        title=f"Biplot ACM - Componentes {x_component+1} y {y_component+1}"
        )