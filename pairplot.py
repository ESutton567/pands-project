# This program plots pairwaise relationships in the iris dataset
# Author: Éilis Sutton
# Ref: https://web.ics.purdue.edu/~yrosokha/code/Seaborn_Example_1.html

import pandas as pd
import csv
import re
import matplotlib.pyplot as plt
# create the plot using seaborn
import seaborn as sns

path = '../pands-project/'
filename = path + 'iris_data.csv'
# assign column names
columns = ['sepal_length','sepal_width','petal_length','petal_width', 'species']

iris_data = pd.read_csv(filename, sep= ',', header=None, names=columns)

# change the style 
sns.set(style='ticks', color_codes=True)
g = sns.pairplot(iris_data, hue='species')

plt.savefig("iris_data_Pairplot.png")




