import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import mplfinance as mpf
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web
import numpy as np
style.use('ggplot')

#df.to_csv('tsla.csv')
df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)

df_ohlc   = df['Adj Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()

df_ohlc.reset_index(inplace=True)
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

ax1 = plt.subplot2grid((11,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((8,1), (6,0), rowspan=1, colspan=1, sharex=ax1)
ax1.xaxis_date()

candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup="g")
#mpf.plot(df,type='candle', mav=(3,6,9),volume=True)
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)

plt.show()
