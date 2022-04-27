# Task 2: The below code saves a histogram of each variable to png files
import pandas as pd
import matplotlib.pyplot as plt
import numpy as py

path = '../pands-project/'
filename = path + 'iris_data.csv'

iris_data = pd.read_csv(filename)
iris_data.columns = ['sepal_length','sepal_width','petal_length','petal_width','species']

# histogram
iris_data.hist(color='indigo', edgecolor='black', grid=False)
plt.text(-3.5, 105,'Iris dataset: Histograms of each variable', 
                fontname='Times New Roman',
                fontsize=20, 
                fontweight='bold'
                )

# test the output using code below
# plt.show()
# save fig to a png file
plt.savefig("iris_data.png")




