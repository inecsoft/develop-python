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
tsla = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)

# Assign `Adj Close` to `daily_close`
daily_close = tsla[['Adj Close']]

# Daily returns
daily_pct_change = daily_close.pct_change()

# Replace NA values with 0
daily_pct_change.fillna(0, inplace=True)

# Plot the distribution of `daily_pct_c`
daily_pct_change.hist(bins=50)

# Show the plot
plt.show()

# Pull up summary statistics
print(daily_pct_change.describe())