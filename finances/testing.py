import bs4 as bs
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import os
import pandas as pd
import pandas_datareader.data as web
import pickle
import requests

"""
Ordinary Least-Squares Regression

"""

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import numpy as np

style.use('ggplot')

# Import the `api` model of `statsmodels` under alias `sm`
import statsmodels.api as sm

# Import the `datetools` module from `pandas`
#from pandas.core import datetools

tickers = ['AAPL', 'MSFT', 'IBM', 'GOOG']

def get(tickers, startdate, enddate):
  def data(ticker):
    return (web.get_data_yahoo(ticker, start=startdate, end=enddate))
    
  datas = map (data, tickers)
  
  return(pd.concat(datas, keys=tickers, names=['Ticker', 'Date']))

all_data = get(tickers, dt.datetime(2006, 10, 1), dt.datetime.now())

#save data to csv file
#all_data.to_csv('all_data.csv')

#all_data = pd.read_csv('sp4_joined_closes.csv')
#all_data = pd.read_csv('all_data.csv')

print(all_data)

# Isolate the `Adj Close` values and transform the DataFrame
#daily_close_px = all_data[[ 'AAPL', 'MSFT', 'IBM', 'GOOG' ]]
#daily_close_px = all_data[['Adj Close', 'Date', 'Ticker']].reset_index().pivot('Date', 'Ticker', 'Adj Close')
#print(daily_close_px)


# Isolate the adjusted closing price
all_adj_close = all_data[['Adj Close']]


# Calculate the returns 
all_returns = np.log(all_adj_close / all_adj_close.shift(1))

# Isolate the AAPL returns 
aapl_returns = all_returns.iloc[all_returns.index.get_level_values('Ticker') == 'AAPL']
aapl_returns.index = aapl_returns.index.droplevel('Ticker')
print(aapl_returns.index)


# Isolate the MSFT returns
msft_returns = all_returns.iloc[all_returns.index.get_level_values('Ticker') == 'MSFT']
msft_returns.index = msft_returns.index.droplevel('Ticker')

# Build up a new DataFrame with AAPL and MSFT returns
return_data = pd.concat([aapl_returns, msft_returns], axis=1)[1:]
return_data.columns = ['AAPL', 'MSFT']

# Add a constant 
X = sm.add_constant(return_data['AAPL'])

# Construct the model
model = sm.OLS(return_data['MSFT'],X).fit()

# Print the summary
print(model.summary())