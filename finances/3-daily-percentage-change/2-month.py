from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
# Import `numpy` as `np`
import numpy as np

style.use('ggplot')

#df.to_csv('tsla.csv')
df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)

# Resample `tsla` to business months, take last observation as value 
monthly = df.resample('BM').apply(lambda x: x[-1])
print(monthly)

# Calculate the monthly percentage change
monthly.pct_change()

# Resample `tsla` to quarters, take the mean as value per quarter
quarter = df.resample("4M").mean()

# Calculate the quarterly percentage change
quarter.pct_change()

