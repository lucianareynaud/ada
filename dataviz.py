import pandas as pd 
import seaborn as sns

iris = sns.load_dataset('iris')

iris.head()

iris['species'].value_counts()

col = 'sepal_length'

sns.histplot(data=iris, x='sepal_length').set_title(f{'Distribuição da variável {col}'})