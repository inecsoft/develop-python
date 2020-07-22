
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
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
print("Daily Porcent Change","\n" , daily_pct_change)

# Calculate the cumulative daily returns
cum_daily_return = (1 + daily_pct_change).cumprod()

# Print `cum_daily_return`
print("Cumulative Daily Return","\n", cum_daily_return)

# Plot the cumulative daily returns
cum_daily_return.plot(figsize=(12,8))

# Show the plot
plt.show()

# Resample the cumulative daily return to cumulative monthly return 
cum_monthly_return = cum_daily_return.resample("M").mean()

# Print the `cum_monthly_return`
print("Cumulative monthly Return","\n",cum_monthly_return)