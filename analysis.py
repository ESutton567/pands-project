# This program performs some basic data analysis on the Fisher's Iris data set
# Author: Éilis Sutton

#task 1
import pandas as pd
import re
import csv
import matplotlib.pyplot as plt

path = '../pands-project/'
filename = path + 'iris.data'

df = pd.read_csv(filename, index_col=0)

# assign column names
header=['Sepal Length','Sepal Width','Petal Length','Petal Width','Species']
df = pd.read_csv(filename, names=header)

# print out a stats summary of the variables
#print(df.describe())

# add text header to new file
lines = ['Summary of each variable', 'Dataset = iris.data']
# create new txt file
with open('irisVariablesSummary.txt', 'w') as f:
    for line in lines: 
        f.write(line)
        f.write('\n')

summary = df.describe()
print(summary)

with open('irisVariablesSummary.txt', 'a') as f:
    #for lines in df: #=> code not working
    #infile.readlines(df):
    #writer = csv.writer(f)
    #writer.writerows('\n'.join(df))
    f.writelines('\n'.join(summary))


# write to the new txt file
#write("irisVariablesSummary.txt")
# The below code outputs a summary of each variable to a single text file

# open iris dataset in read only mode
#f = open("iris.data", "r")


# task 2: The below code saves a histogram of each variable to png files





# The below code outputs a scatter plot of each pair of variables

# The below code ......


