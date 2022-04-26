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
fig,ax = plt.subplots(6, figsize=(18,15))

ax[0].scatter(x = iris_data['sepal_length'], y = iris_data['sepal_width'], color = 'blue')
ax[0].set_xlabel("Sepal Length")
ax[0].set_ylabel("Sepal Width")

ax[1].scatter(x = iris_data['sepal_width'], y = iris_data['petal_length'])
ax[1].set_xlabel("Sepal Width")
ax[1].set_ylabel("Petal Length")

ax[2].scatter(x = iris_data['petal_length'], y = iris_data['petal_width'])
ax[2].set_xlabel("Petal Length")
ax[2].set_ylabel("Petal Width")

ax[3].scatter(x = iris_data['sepal_length'], y = iris_data['sepal_width'])
ax[3].set_xlabel("Sepal Length")
ax[3].set_ylabel("Sepal Width")

ax[4].scatter(x = iris_data['petal_width'], y = iris_data['species'])
ax[4].set_xlabel("Petal Width")
ax[4].set_ylabel("Species")

ax[5].scatter(x = iris_data['species'], y = iris_data['sepal_length'])
ax[5].set_xlabel("Species")
ax[5].set_ylabel("Sepal Length")

plt.grid()
plt.show()


