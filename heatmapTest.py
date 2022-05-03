# this program runs a heatmap of the iris dataset
# Author: Éilis Sutton
# Ref: https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/

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

sns.heatmap(iris_data.corr(), linecolor = 'white', linewidths = 1, annot = True)

plt.savefig("iris_data_Heatmap.png")




