# Task 3: The below code outputs a scatter plot of each pair of variables
# Author: Éilis Sutton

import pandas as pd
import matplotlib.pyplot as plt
import numpy as py

path = '../pands-project/'
filename = path + 'iris_data.csv'

iris_data = pd.read_csv(filename)
iris_data.columns = ['sepal_length','sepal_width','petal_length','petal_width','species']

#versicolor = iris_data[iris_data.columns 'species' == 'Versicolor']

# generating a scatter plot matrix to look at the interaction between the variables
fig,ax = plt.subplots()

points = ax.scatter

iris_data.plot(kind ="scatter", 
                x ='sepal_length',
                y = 'sepal_width')                

iris_data.plot(kind ="scatter", 
                x ='sepal_width',
                y = 'petal_length')

iris_data.plot(kind ="scatter", 
                x ='petal_length',
                y = 'petal_width')

iris_data.plot(kind ="scatter", 
                x ='petal_width',
                y = 'species')

iris_data.plot(kind ="scatter", 
                x ='species',
                y = 'sepal_length')


plt.grid()
plt.show()

