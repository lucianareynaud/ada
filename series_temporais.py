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

#decomposição da sazonalidade com a lib stats models
#fazer conversão do observation time para que seja um índice

from statsmodels.tsa.seasonal import seasonal_decompose

candy_filtered.set_index('observation_date', inplace=True)
analysis = candy_filtered[['industrial_production']].copy()

decompose_result = seasonal_decompose(analysis, model='multiplicative') #modelo multiplicative separa os componentes do gráfico temporal
trend = decompose_result.trend
seasonal = decompose_result.seasonal
residual = decompose_result.residual

decompose_result.plot()





