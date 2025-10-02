import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

candy = pd.read_csv('candy_production.csv')

candy.head(12)
candy.tail(12)
candy.info()

candy['observation_date'] = pd.to_datetime(candy['observation_date'])
candy.info()

candy.plot(x='observation_date', y='industrial_production' )