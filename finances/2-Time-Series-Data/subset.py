import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

#df.to_csv('tsla.csv')
df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)


print(df.head())
# Inspect the first rows of November-December 2015
print("Inspect the first rows of November-December 2015")
print(df.loc[pd.Timestamp('2015-11-01'):pd.Timestamp('2015-12-31')].head())

# Inspect the first rows of 2015
print("Inspect the first rows of 2015")
print(df.loc['2015'].head())

# Inspect November 2015
print("Inspect November 2015")
print(df.iloc[22:43])

# Inspect the 'Open' and 'Close' values at 2015-11-01 and 2015-12-01
print("Inspect the 'Open' and 'Close' values at 2015-11-01 and 2015-12-01")
print(df.iloc[[22,43], [0, 3]])