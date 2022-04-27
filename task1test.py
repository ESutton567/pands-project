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
#?Removed species column here - check if it works for the plot outputs
iris_data.columns = ['sepal_length','sepal_width','petal_length','petal_width', 'species']

# Check if any values are missing
iris_data.isnull().sum()

# Create a text file to ouptut a summary of the variables
print('Summary statistics for each variable (cm) in the Iris Dataset:\n', file=open('irisVariablesSummary.txt', 'w'))
# append a stats summary of the variables
summary_all = iris_data.describe()
print(summary_all, file=open('irisVariablesSummary.txt', 'a'))

print('\nA list of the type for each variable in the Iris Dataset:\n', file=open('irisVariablesSummary.txt', 'a'))
# append a type summary of the variables
print(iris_data.dtypes, file=open('irisVariablesSummary.txt', 'a'))

print('\nA concise summary of the Iris Dataset: \n', file=open('irisVariablesSummary.txt', 'a'))
print(iris_data.info, file=open('irisVariablesSummary.txt', 'a'))



