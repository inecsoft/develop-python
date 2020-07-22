import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

#df.to_csv('tsla.csv')
df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)

# Sample 20 rows
sample = df.sample(20)

# Print `sample`
print(sample)

# Resample to monthly level 
monthly_tsla = df.resample('M').mean()

# Print `monthly_tsla`
print(monthly_tsla)