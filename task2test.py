# task 2: The below code saves a histogram of each variable to png files
import pandas as pd
import re
import csv
import matplotlib.pyplot as plt
import numpy as py

path = '../pands-project/'
filename = path + 'iris.data'

iris_data = pd.read_csv(filename)
iris_data.columns = ['sepal_length','sepal_width','petal_length','petal_width','species']

print(iris_data.head(10))




#plt.hist(df)
#plt.show()