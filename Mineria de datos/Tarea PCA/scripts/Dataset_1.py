import matplotlib.pyplot as plt
import numpy as np

def Scree_Plot(pca):
    varianza_explicada_acumulada = np.cumsum(pca.explained_variance_ratio_)

    plt.figure(figsize=(10, 6))
    plt.plot(
        range(1, len(varianza_explicada_acumulada) + 1),
        varianza_explicada_acumulada,
        marker='o',
        linestyle='--'
    )

    plt.title('Scree Plot')
    plt.xlabel('Número de Componentes Principales')
    plt.ylabel('Varianza Explicada Acumulada')
    plt.xticks(range(1, len(varianza_explicada_acumulada) + 1))
    plt.grid()
    plt.show()
