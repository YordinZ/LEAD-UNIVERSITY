import pandas as pd
import prince
import matplotlib.pyplot as plt


import altair as alt
alt.data_transformers.enable("vegafusion")

class ACM:
    def __init__(self, df, n_components=10, sample_size=3000):
        self.df = df
        self.n_components = n_components
        self.sample_size = sample_size
        self.acm_fit = prince.MCA(n_components=n_components, random_state=42)
        self.acm_fit = self.acm_fit.fit(self.df)

    def scree_plot(self):
        eig = self.acm_fit.eigenvalues_summary.copy()
        inercia = (
            eig['% of variance']
            .astype(str).str.rstrip('%').str.strip().astype(float)
        )
        inercia_acumulada = inercia.cumsum()
        n = len(inercia)

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(range(1, n + 1), inercia, alpha=0.6, color='steelblue',
               label='Inercia explicada (%)')
        ax.plot(range(1, n + 1), inercia_acumulada, marker='o',
                color='red', label='Inercia acumulada (%)')

        for i, (v, acum) in enumerate(zip(inercia, inercia_acumulada)):
            ax.text(i + 1, v + 0.3, f'{v:.1f}%',
                    ha='center', va='bottom', fontsize=9)
            ax.text(i + 1, acum + 0.3, f'{acum:.1f}%',
                    ha='center', va='bottom', fontsize=9, color='red')

        ax.set_xlabel("Componente")
        ax.set_ylabel("Porcentaje de inercia (%)")
        ax.set_title("Scree Plot - ACM")
        ax.set_xticks(range(1, n + 1))
        ax.legend()
        ax.grid(True, linestyle='--', alpha=0.5)
        plt.tight_layout()
        plt.show()

    def biplot(self, x_component=0, y_component=1):

        col_coords = self.acm_fit.column_coordinates(self.df).reset_index()
        col_coords.columns = ['label'] + list(col_coords.columns[1:])
        col_coords = col_coords[['label',
                                col_coords.columns[x_component + 1],
                                col_coords.columns[y_component + 1]]]
        col_coords.columns = ['label', 'x', 'y']
        col_coords['variable'] = 'column'

        if self.sample_size is not None and len(self.df) > self.sample_size:
            df_plot = self.df.sample(n=self.sample_size, random_state=42)
        else:
            df_plot = self.df
        row_coords = self.acm_fit.row_coordinates(df_plot).reset_index(drop=True)
        row_coords = row_coords.iloc[:, [x_component, y_component]]
        row_coords.columns = ['x', 'y']
        row_coords['label'] = ''
        row_coords['variable'] = 'row'

        df_combined = pd.concat([row_coords, col_coords], ignore_index=True)

        eig = self.acm_fit.eigenvalues_summary
        inercia = (
            eig['% of variance']
            .astype(str).str.rstrip('%').str.strip().astype(float)
        )

        base = alt.Chart(df_combined).encode(
            x=alt.X('x:Q', title=f"component {x_component} — {inercia.iloc[x_component]:.2f}%"),
            y=alt.Y('y:Q', title=f"component {y_component} — {inercia.iloc[y_component]:.2f}%"),
            color=alt.Color('variable:N', scale=alt.Scale(
                domain=['row', 'column'],
                range=['#FFA500', "#1163AF"]
            ))
        )

        points = base.mark_point(opacity=0.4, size=30)

        # Etiquetas SOLO para las categorías, siempre visibles
        labels = alt.Chart(col_coords).mark_text(
            dx=6, dy=-6, fontSize=10, color='black'
        ).encode(
            x=alt.X('x:Q'),
            y=alt.Y('y:Q'),
            text='label:N'
        )

        return (points + labels).interactive().properties(
            width=600,
            height=600,
            title=f"Biplot ACM - Componentes {x_component + 1} y {y_component + 1}"
        )