import pandas as pd
import numpy as np

houses_sp = pd.read_csv('houses_sp.csv')

houses_sp.head(10)

houses_sp['city'].value_counts()
houses_sp.info()

#coluna constante no dataset inteiro é inutil, atrapalha e gasta processamento

houses_sp = houses_sp.drop(columns=['city'])

#lidando com dados erroneos

houses_sp['rooms']

houses_sp.info()

#é possivel preencher os nulos com estatística descritiva, por exemplo, calculando a media de todos os campos nao-nulos e 
#preencher com a media do conjunto dos dados. Mas não é recomendado
#porque a média é muito sensivel a outliers
#a mediana é melhor, dá um numero inteiro

houses_sp['rooms'].median()

#função fillna preenche dados nulos
#fazer preenchimento com zeros é perigoso pois pode não ser representativo
#por exemplo, no nosso caso não temos nenhuma casa sem quartos

houses_sp['rooms'] = houses_sp['rooms'].fillna(houses_sp['rooms'].median())

#também podemos ter dados digitados erroneod