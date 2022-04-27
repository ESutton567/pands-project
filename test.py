import pandas as pd
import re
import csv
import matplotlib.pyplot as plt

path = '../pands-project/'
filename = path + 'iris_data.csv'

#read in file
iris_data = pd.read_csv(filename)

# assign column names
#?Removed species column here - check if it works for the plot outputs
iris_data.columns = ['sepal_length','sepal_width','petal_length','petal_width', 'species']

print(iris_data.head())
