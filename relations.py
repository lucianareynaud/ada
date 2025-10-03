import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset('penguins')
penguins.head()

penguins['species'].value_count()
penguins_numeric = penguins.drop(columns=['species', 'island', 'sex'])
penguins.corr()
