import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset=pd.read_csv('Salary_data.csv')
x=dataset.iloc[:,:-1]
y=dataset.iloc[:,1]

#taking the first 19 elements from the dataset
x_train=x[0:19]
x_test=x[19:30]
y_train=y[0:19]
y_test=y[19:30]
from sklearn.linear_model import LinearRegression
regressor=LinearRegression();
regressor.fit(x_train,y_train)
y_pred=regressor.predict(x_train)

#predicting on the x_test
y_pred2=regressor.predict(x_test)


