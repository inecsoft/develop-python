import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
# Import `numpy` as `np`
import numpy as np

style.use('ggplot')

#df.to_csv('tsla.csv')
df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)


# Assign `Adj Close` to `daily_close`
daily_close = df[['Adj Close']]

# Daily returns
#daily_pct_change = daily_close.pct_change()

# Replace NA values with 0
#daily_pct_change.fillna(0, inplace=True)

# Daily returns
daily_pct_change = daily_close / daily_close.shift(1) - 1

# Print `daily_pct_change`
print(daily_pct_change)
