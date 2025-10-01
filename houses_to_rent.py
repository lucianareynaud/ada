import pandas as pd
import numpy as np

houses = pd.read_csv('houses_to_rent.csv')

houses.head()
houses.describe()

houses['bathroom'].value_counts()

#critérios de detecção de outliers
#IQR-Inter Quantile Range -> distância inter quartil
#distância entre primeiro quartil (25%) e terceiro quartil (75%)

q1 = houses['bathroom'].quantile(0.25)
q3 = houses['bathroom'].quantile(0.75)

IQR = q3 - q1

print(f'IQR: {IQR}')

houses_outliers = houses[(houses['bathroom'] < Q1 -m (IQR * 1.5))| (houses['bathroom'] > Q3 + IQR * 1.5)]