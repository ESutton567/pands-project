# This program performs some basic data analysis on the Fisher's Iris data set
# Author: Éilis Sutton

import pandas as pd
import re
import csv

path = '../pands-project/'
filename = path + 'iris.data'

df = pd.read_csv(filename)

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

def summary(stats):
    return df.describe()

#summary = df.describe()
#print(df.describe())

#meanValues = df.groupby('Sepal Length').mean()
#print(meanValues)

stats = summary(stats) #??
with open('irisVariablesSummary.txt', 'a') as f:
    #for i in range(len(df)): #=> code not working
        f.write('\n'.join(summary(stats)))



# write to the new txt file
#write("irisVariablesSummary.txt")
# The below code outputs a summary of each variable to a single text file

# open iris dataset in read only mode
#f = open("iris.data", "r")






#print(f.read())


# The below code saves a histogram of each variable to png files

# The below code outputs a scatter plot of each pair of variables

# The below code ......

# The below code prints out the average of each variable for 