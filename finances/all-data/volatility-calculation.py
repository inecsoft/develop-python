import datetime as dt
import os
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import numpy as np
import pandas_datareader as pdr

style.use('ggplot')

tickers = ['AAPL', 'MSFT', 'IBM', 'GOOG']

def get(tickers, startdate, enddate):
  def data(ticker):
    return (pdr.get_data_yahoo(ticker, start=startdate, end=enddate))
  datas = map (data, tickers)
  return(pd.concat(datas, keys=tickers, names=['Ticker', 'Date']))

if not os.path.exists('all_data.csv'):
    all_data = get(tickers, dt.datetime(2006, 10, 1), dt.datetime.now())
    all_data.to_csv('all_data.csv')
else:
    print('Already have all_data.csv')

#all_data.to_csv('all_data.csv')
#all_data = pd.read_csv('all_data.csv', parse_dates=True, index_col=0)
all_data = pd.read_csv('all_data.csv', parse_dates=True, index_col='Ticker')
print(all_data)

all_data = get(tickers, dt.datetime(2006, 10, 1), dt.datetime.now())
print(all_data)

# Isolate the `Adj Close` values and transform the DataFrame
daily_close_px = all_data[['Adj Close']].reset_index().pivot('Date', 'Ticker', 'Adj Close')

# Calculate the daily percentage change for `daily_close_px`
daily_pct_change = daily_close_px.pct_change()

#df.to_csv('tsla.csv')
#df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)

# Isolate the adjusted closing prices 
#adj_close_px = df['Adj Close']

# Assign `Adj Close` to `daily_close`
#daily_close = df[['Adj Close']]

# Daily returns
#daily_pct_change = daily_close.pct_change()

# Replace NA values with 0
#daily_pct_change.fillna(0, inplace=True)

# Daily returns
#daily_pct_change = daily_close / daily_close.shift(1) - 1

# Print `daily_pct_change`
#print(daily_pct_change)

# Define the minumum of periods to consider 
min_periods = 75 

# Calculate the volatility
vol = daily_pct_change.rolling(min_periods).std() * np.sqrt(min_periods) 

# Plot the volatility
vol.plot(figsize=(10, 8))

# Show the plot
plt.show()
