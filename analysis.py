# This program performs some basic data analysis on the Fisher's Iris data set
# Author: Éilis Sutton

# Task 1
# The below code outputs a summary of each variable to a single text file
import pandas as pd
import re
import csv
import matplotlib.pyplot as plt
import seaborn as sns

path = '../pands-project/'
filename = path + 'iris_data.csv'
# assign column names
columns = ['sepal_length','sepal_width','petal_length','petal_width', 'species']

#read in file
iris_data = pd.read_csv(filename, sep= ',', header=None, names=columns)

# locate the target data within the dataset
setosa = iris_data.loc[iris_data['species']=='Iris-setosa']
virginica = iris_data.loc[iris_data['species']=='Iris-virginica']
versicolor = iris_data.loc[iris_data['species']=='Iris-versicolor']

# check if any values are missing
iris_data.isnull().sum()

# create a text file to ouptut a summary of the variables
print('Summary statistics for each variable (cm) in the Iris Dataset:\n', file=open('irisVariablesSummary.txt', 'w'))
# append a stats summary of the variables
summary_all = iris_data.describe()
print(summary_all, file=open('irisVariablesSummary.txt', 'a'))

print('\nA list of the type for each variable in the Iris Dataset:\n', file=open('irisVariablesSummary.txt', 'a'))
# append a type summary of the variables
print(iris_data.dtypes, file=open('irisVariablesSummary.txt', 'a'))

print('\nA concise summary of the Iris Dataset: \n', file=open('irisVariablesSummary.txt', 'a'))
print(iris_data.info, file=open('irisVariablesSummary.txt', 'a'))

# Task 2: The below code saves a histogram of each variable to png files

# create histograms
iris_data.hist(color='indigo', edgecolor='black', grid=False)
plt.text(-3.5, 105,'Iris dataset: Histograms of each variable', 
                fontname='Times New Roman',
                fontsize=20, 
                fontweight='bold'
                )

# save fig to a png file
plt.savefig("iris_data.png")

# Task 3: The below code outputs a scatter plot of each pair of variables

fig,ax = plt.subplots(3, figsize=(10,10))
    
ax[0].scatter(x = iris_data['sepal_length'], y = iris_data['sepal_width'], color = 'blue', edgecolors = "black")
ax[0].set_xlabel("Sepal Length", weight='bold')
ax[0].set_ylabel("Sepal Width", weight='bold')
ax[0].set_title('Iris dataset: Scatter plots of each pair of variables', 
                fontname='Times New Roman',
                fontsize=20, 
                fontweight='bold'
                )


ax[0].scatter(x = iris_data['sepal_width'], y = iris_data['petal_length'], color = 'blueviolet', edgecolors = "black")
ax[0].set_xlabel("Sepal Width", weight='bold')
ax[0].set_ylabel("Petal Length", weight='bold')

ax[1].scatter(x = iris_data['petal_length'], y = iris_data['petal_width'], color = 'darkgreen', edgecolors = "black")
ax[1].set_xlabel("Petal Length", weight='bold')
ax[1].set_ylabel("Petal Width", weight='bold')

ax[2].scatter(x = iris_data['sepal_length'], y = iris_data['sepal_width'], color = 'teal', edgecolors = "black")
ax[2].set_xlabel("Sepal Length", weight='bold')
ax[2].set_ylabel("Sepal Width", weight='bold')

#plt.grid()
plt.tight_layout()
plt.show()

# the code below was used to visualise the scatterplots while customising
#plt.savefig("scatterplot.png")

# Additional plot 1: This program runs a heatmap of the iris dataset using Seaborn

# run a heatmap of the dataset showing correlations between all numerical values
# customise line colour and width and annotate each cell with the numeric value
sns.heatmap(iris_data.corr(), linecolor = 'white', linewidths = 1, annot = True)

plt.savefig("iris_data_Heatmap.png")




























