# Task 3: The below code outputs a scatter plot of each pair of variables
# Author: Éilis Sutton

from matplotlib.ft2font import BOLD
import pandas as pd
import matplotlib.pyplot as plt
import numpy as py

path = '../pands-project/'
filename = path + 'iris_data.csv'

iris_data = pd.read_csv(filename)
iris_data.columns = ['sepal_length','sepal_width','petal_length','petal_width','species']

# generating a scatter plot matrix to look at the interaction between the variables
fig,ax = plt.subplots(6, figsize=(20,20))
    
ax[0].scatter(x = iris_data['sepal_length'], y = iris_data['sepal_width'], color = 'blue', edgecolors = "black")
ax[0].set_xlabel("Sepal Length", weight='bold')
ax[0].set_ylabel("Sepal Width", weight='bold')
ax[0].set_title('Iris dataset: Scatter plots of each pair of variables', 
                fontname='Times New Roman',
                fontsize=35, 
                fontweight='bold'
                )


ax[1].scatter(x = iris_data['sepal_width'], y = iris_data['petal_length'], color = 'blueviolet', edgecolors = "black")
ax[1].set_xlabel("Sepal Width", weight='bold')
ax[1].set_ylabel("Petal Length", weight='bold')

ax[2].scatter(x = iris_data['petal_length'], y = iris_data['petal_width'], color = 'darkgreen', edgecolors = "black")
ax[2].set_xlabel("Petal Length", weight='bold')
ax[2].set_ylabel("Petal Width", weight='bold')

ax[3].scatter(x = iris_data['sepal_length'], y = iris_data['sepal_width'], color = 'teal', edgecolors = "black")
ax[3].set_xlabel("Sepal Length", weight='bold')
ax[3].set_ylabel("Sepal Width", weight='bold')

plt.grid()
plt.show()

# the code below was used to visualise the scatterplots while customising
#plt.savefig("scatterplot.png")

