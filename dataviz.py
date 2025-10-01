import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')

iris.head()

iris['species'].value_counts()

col = 'sepal_length'

sns.histplot(data=iris, x='sepal_length', kde=True).set_title(f{'Distribuição da variável {col}'})

for col in iris.drop(columns='species'):
    sns.histplot(data=iris, x=col, kde=True).set_title(f'Distribioção de variável {col}')
    plt.show()

# Contexto: em análises de dados, precisamos escolher o gráfico certo
# dependendo do tipo de variável (categórica ou numérica) e do objetivo da análise.

# Gráfico de barras (barplot): mostra a média de uma variável numérica em cada categoria.
# É útil para comparar o valor médio entre grupos (por exemplo, tempo médio de entrega
# em diferentes regiões). O gráfico ainda mostra linhas de variação, que ajudam a avaliar
# se a diferença entre os grupos pode ser relevante.

# Histograma (histplot): mostra a distribuição de valores de uma variável numérica.
# Quando usamos a opção "hue", conseguimos comparar como essa distribuição varia
# entre grupos diferentes (por exemplo, notas de alunos que praticam esportes e os que não praticam).

# Boxplot: mostra a mediana, a dispersão e os valores extremos (outliers) de uma variável
# numérica em cada grupo. É útil para entender a variação e não apenas a média.

# Princípio geral: 
# - Use barplot quando o interesse está em comparar médias entre categorias.
# - Use histplot quando o objetivo é analisar a distribuição de valores e comparar grupos.
# - Use boxplot quando queremos observar variação, mediana e possíveis outliers.
# - Evite scatterplot ou lineplot para variáveis puramente categóricas, pois eles são mais
# adequados para relações entre duas variáveis numéricas ou séries temporais.
