import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
#reading the data
"""	here the directory of my code and the headbrain.csv 
	file is same make sure both the files are stored in 
	the same folder or directory""" 

path=os.getcwd()
print(path)
data=pd.read_csv('./headbrain/headbrain.csv')
print(data.head())

#assign head size values to x
x=data.iloc[:,2:3].values
#assign head size values to y
y=data.iloc[:,3:4].values


#splitting the data into training and test
from sklearn.model_selection import train_test_split
#from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.7,random_state=0)

#fitting simple linear regression to the training set
from sklearn.linear_model import LinearRegression

# Create linear regression object
regressor=LinearRegression()

# Train the model using the training sets
regressor.fit(x_train,y_train)

#predict the test result
y_pred=regressor.predict(x_test)

#to see the relationship between the training data values
plt.scatter(x_train,y_train,c='red')
plt.xlabel('headsize')
plt.ylabel('brain weight')
plt.show()

#to see the relationship between the predicted brain weight values using scattered graph
plt.plot(x_test,y_pred, label="linear regression")   
plt.scatter(x_test,y_test,c='red', label="brain weight values")
plt.xlabel('headsize')
plt.ylabel('brain weight')
plt.legend()
plt.show()


# The coefficients
print('Coefficients: \n', regressor.coef_)
# The mean squared error
print('Mean squared error: %.2f'
      % mean_squared_error(y_test, y_pred))
# The coefficient of determination: 1 is perfect prediction
print('Coefficient of determination: %.2f'
      % r2_score(y_test, y_pred))


# Plot outputs
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
ax1.scatter(x_train,y_train,c='red', label="training sets")
ax1.set_xlabel('headsize')
ax1.set_ylabel('brain weight')

ax2.plot(x_test,y_pred, color='blue', linewidth=2, label="linear regression")
ax2.set_xlabel('headsize')
ax2.set_ylabel('brain weight')
ax2.scatter(x_test,y_test,c='red', label="brain weight values")
ax2.legend()

plt.show()