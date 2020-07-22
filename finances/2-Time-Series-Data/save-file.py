import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2015, 1, 1)
end = dt.datetime.now()
df = web.DataReader("TSLA", 'yahoo', start, end)
#df =web.DataReader("AAPL", "yahoo", start, end)

#df.to_csv('tsla.csv')
df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)

print(df.head())

df['Adj Close'].plot()
plt.show()

# Inspect the index 
print(df.index)

# Inspect the columns
print(df.columns)

# Select only the last 10 observations of `Close`
ts = df['Close'][-10:]

# Check the type of `ts` 
print(type(ts))


# Plot the closing prices for `df`
df['Close'].plot(grid=True)

# Show the plot
plt.show()