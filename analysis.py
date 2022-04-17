# This program performs some basic data analysis on the Fisher's Iris data set
# Author: Éilis Sutton

import pandas as pd

path = '../pands-project/'
filename = path + 'iris.data'

df = pd.read_csv(filename)

header_list=['Sepal Length','Sepal Width','Petal Length','Petal Width','Species']
df = pd.read_csv(filename, names=header_list)

print(df.head(5))


# The below code outputs a summary of each variable to a single text file

# open iris dataset in read only mode
#f = open("iris.data", "r")
# create new txt file
#f.open("irisVariablesSummary.txt", "x")
# write to the new txt file
#f.write("irisVariablesSummary.txt")

#print(f.read())


# The below code saves a histogram of each variable to png files

# The below code outputs a scatter plot of each pair of variables

# The below code ......

# The below code prints out the average of each variable for 