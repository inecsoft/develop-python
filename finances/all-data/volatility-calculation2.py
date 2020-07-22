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

#all_data = get(tickers, dt.datetime(2006, 10, 1), dt.datetime.now())

def get_data_from_yahoo():

    if not os.path.exists('stock'):
        os.makedirs('stock')

    start = dt.datetime(2010, 1, 1)
    end = dt.datetime.now()

    for ticker in tickers:
        # just in case your connection breaks, we'd like to save our progress!
        print(ticker)

        if not os.path.exists('stock/{}.csv'.format(ticker)):
            df = web.DataReader(ticker, 'yahoo', start, end)
            df.to_csv('stock/{}.csv'.format(ticker))
        else:
            print('Already have {}'.format(ticker))


#get_data_from_yahoo()

def compile_data():
    
    main_df = pd.DataFrame()

    for count, ticker in enumerate(tickers):
        df = pd.read_csv('stock/{}.csv'.format(ticker))
        df.set_index('Date', inplace=True)

        df.rename(columns={'Adj Close': ticker}, inplace=True)
        df.drop(['Open', 'High', 'Low', 'Close', 'Volume'], 1, inplace=True)

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df, how='outer')

        if count % 10 == 0:
            print(count)
    print(main_df.head())
    main_df.to_csv('sp4_joined_closes.csv')

compile_data()

#all_data = pd.read_csv('sp4_joined_closes.csv')
all_data = pd.read_csv('all_data.csv')

print(all_data)

# Isolate the `Adj Close` values and transform the DataFrame
#daily_close_px = all_data[[ 'AAPL', 'MSFT', 'IBM', 'GOOG' ]]
daily_close_px = all_data[['Adj Close', 'Date', 'Ticker']].reset_index().pivot('Date', 'Ticker', 'Adj Close')
print(daily_close_px)

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
