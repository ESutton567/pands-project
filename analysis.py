# This program performs some basic data analysis on the Fisher's Iris data set
# Author: Éilis Sutton

# Task 1
# The below code outputs a summary of each variable to a single text file
import pandas as pd
import re
import csv
import matplotlib.pyplot as plt

path = '../pands-project/'
filename = path + 'iris_data.csv'

#read in file
iris_data = pd.read_csv(filename)

# assign column names
iris_data.columns = ['sepal_length','sepal_width','petal_length','petal_width','species']

# Create a text file to ouptut a summary of the variables
# Update this to make it more readable
summary = iris_data.describe()
print('Summary of each variable\nDataset = iris.data.csv', file=open('irisVariablesSummary.txt', 'w'))
# append a stats summary of the variables
print(summary, file=open('irisVariablesSummary.txt', 'a'))

# task 2: The below code saves a histogram of each variable to png files

iris_data.plot.bar()
plt.show()





# The below code outputs a scatter plot of each pair of variables

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

ax[4].scatter(x = iris_data['petal_width'], y = iris_data['species'], color = 'slateblue', edgecolors = "black")
ax[4].set_xlabel("Petal Width", weight='bold')
ax[4].set_ylabel("Species", weight='bold')

ax[5].scatter(x = iris_data['species'], y = iris_data['sepal_length'], color = 'orchid', edgecolors = "black")
ax[5].set_xlabel("Species", weight='bold')
ax[5].set_ylabel("Sepal Length", weight='bold')


plt.grid()
plt.show()

# the code below was used to visualise the scatterplots while customising
#plt.savefig("scatterplot.png")






























