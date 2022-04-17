# task 1: The below code exports a summary of the variables to a txt file
import pandas as pd
import matplotlib.pyplot as plt
import numpy as py
import csv

path = '../pands-project/'
filename = path + 'iris.data'

iris_data = pd.read_csv(filename)
iris_data.columns = ['sepal_length','sepal_width','petal_length','petal_width','species']


summary=iris_data.describe()
summary = summary.transpose()
print(summary)

# export 'summary' output to a text file

# add text header to new file
lines = ['Summary of each variable', 'Dataset = iris.data']
# create new txt file
with open('irisVariablesSummary.txt', 'w') as f:
    for line in lines: 
        f.write(line)
        f.write('\n')

fields=['1','2','3']
with open('irisVariablesSummary.txt', 'a') as f:
    #for lines in df: #=> code not working
    #infile.readlines(df):
    #writer = csv.writer(f)
   # writer.writerow(fields)
    # loop through the text to add line by line --> code not working
    # ?how do you get it to add every row of the output??
    #for line in summary:
        # append the ouput of summary to the file, adding a space after each column
    #f.readlines(summary)
    f.writelines('\n'.join(summary))







