import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

candy = pd.read_csv('candy_production.csv')

candy.head(12)
candy.tail(12)
candy.info()

candy['observation_date'] = pd.to_datetime(candy['observation_date'])
candy.info()

candy.plot(x='observation_date', y='industrial_production')

candy_filtered = candy[candy['observation_date'] >= '2010-01-01']

candy_filtered

ax = candy_filtered.plot(x='observation_date', y='industrial_production', fig_size=(12, 6))

xcoords = ['2011-01-01', '2012-01-01', '2013-01-01', '2014-01-01', '2015-01-01', '2016-01-01', '2017-01-01']
for xc in xcoords:
    plt.axvline(x=xc, color='black', linestyle='--')
