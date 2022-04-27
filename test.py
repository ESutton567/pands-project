import pandas as pd
import re
import csv
import matplotlib.pyplot as plt

path = '../pands-project/'
filename = path + 'iris_data.csv'
# assign column names
columns = ['sepal_length','sepal_width','petal_length','petal_width', 'species']

#read in file
iris_data = pd.read_csv(filename, sep= ',', header=None, names=columns)

# locate the target data within the file
setosa = iris_data.loc[iris_data['species']=='Iris-setosa']
virginica = iris_data.loc[iris_data['species']=='Iris-virginica']
versicolor = iris_data.loc[iris_data['species']=='Iris-versicolor']

print(iris_data)
