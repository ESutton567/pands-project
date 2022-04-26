# This program performs some basic data analysis on the Fisher's Iris data set
# Author: Éilis Sutton

# Task 1
# The below code outputs a summary of each variable to a single text file
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

# open iris dataset in read only mode
#f = open("iris.data", "r")

# task 2: The below code saves a histogram of each variable to png files

df.plot.bar()
plt.show()





# The below code outputs a scatter plot of each pair of variables

fig,ax = plt.subplots(6, figsize=(20,20))
    
ax[0].scatter(x = iris_data['sepal_length'], y = iris_data['sepal_width'], color = 'blue', edgecolors = "black")
ax[0].set_xlabel("Sepal Length", weight='bold')
ax[0].set_ylabel("Sepal Width", weight='bold')
ax[0].set_title('Iris dataset: Scatter plots of each pair of variables', 
                fontname='Times New Roman',
                fontsize=35, 
                fontweight='bold'
                )


ax[1].scatter(x = iris_data['sepal_width'], y = iris_data['petal_length'], color = 'blueviolet', edgecolors = "black")
ax[1].set_xlabel("Sepal Width", weight='bold')
ax[1].set_ylabel("Petal Length", weight='bold')

ax[2].scatter(x = iris_data['petal_length'], y = iris_data['petal_width'], color = 'darkgreen', edgecolors = "black")
ax[2].set_xlabel("Petal Length", weight='bold')
ax[2].set_ylabel("Petal Width", weight='bold')

ax[3].scatter(x = iris_data['sepal_length'], y = iris_data['sepal_width'], color = 'teal', edgecolors = "black")
ax[3].set_xlabel("Sepal Length", weight='bold')
ax[3].set_ylabel("Sepal Width", weight='bold')

ax[4].scatter(x = iris_data['petal_width'], y = iris_data['species'], color = 'slateblue', edgecolors = "black")
ax[4].set_xlabel("Petal Width", weight='bold')
ax[4].set_ylabel("Species", weight='bold')

ax[5].scatter(x = iris_data['species'], y = iris_data['sepal_length'], color = 'orchid', edgecolors = "black")
ax[5].set_xlabel("Species", weight='bold')
ax[5].set_ylabel("Sepal Length", weight='bold')


plt.grid()
plt.show()

# the code below was used to visualise the scatterplots while customising
#plt.savefig("scatterplot.png")






























