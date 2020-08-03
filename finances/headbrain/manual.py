import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression

#plt.rcParams['figure.figzise'] = ( 20.0, 10.0 )
data=pd.read_csv('./headbrain/headbrain.csv')
print(data.shape)
print(data.head())

# Colecting X and Y
X = data['Head Size(cm^3)'].values
Y = data['Brain Weight(grams)'].values

# Mean X and Y
mean_x = np.mean(X)
mean_y = np.mean(Y)

# total number of values
m = len(X)

# Using the formula to calcualte b1 and b2
numer = 0
denom = 0

for i in range(m):
    numer += (X[i] - mean_x) * (Y[i] - mean_y)
    denom += (X[i] - mean_x) ** 2
b1 = numer / denom
b0 = mean_y - (b1 * mean_x)

# print coefficients
print('coefficient b0: {0} \ncoefficient b1: {1}'.format(b0, b1))

# Plotting values and Regression line
max_x = np.max(X) + 100
min_x = np.min(X) - 100

# Calculating Line values x and y
x = np.linspace(min_x, max_x, 1000)
y = b0 + b1 * x

# Ploting line 
plt.plot(x,y, color='#58b970', label='Regression line')
# Ploting Scatter Points
plt.scatter(X, Y, c='#ef5423', label='Scatter Plot')

plt.xlabel('Head Size in cm3')
plt.ylabel('Brain Weight in grams')
plt.legend()
plt.show()

ss_t = 0
ss_r = 0

# Calculate r square value
for i in range(m):
    y_pred = b0 + b1 * x[i]
    ss_t += (Y[i] - mean_y) ** 2
    ss_r += (Y[i] - y_pred) ** 2
r2 = 1 - (ss_r/ss_t)
print('r-square value: {0}'.format(r2))

# Cannot use Rank 1 matrix in scikt learn
X = X.reshape((m, 1))
# Creating Model
reg = LinearRegression()
# Fitting training data
reg = reg.fit(X,Y)
# Y Prediction
Y_pred = reg.predict(X)

# Calculation R2 Score
r2_score = reg.score(X,Y)


# The coefficients
print('Coefficients: ', reg.coef_)
# The mean squared error
print('Mean squared error: {}'.format(mean_squared_error(X, Y_pred)))
# The coefficient of determination: 1 is perfect prediction
print('R2_score: {0}'.format(r2_score))

# Plot outputs
plt.scatter(X, Y,  color='red', label="brain weight values")
plt.plot(X, Y_pred, color='blue', linewidth=1, label="linear regression")

plt.xlabel('Head Size in cm3')
plt.ylabel('Brain Weight in grams')
plt.legend()
plt.show()
