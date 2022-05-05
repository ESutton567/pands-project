# pands-project

## Background


This ReadMe file is an accompaniment to a project I completed as part of my Higher Diploma in in Computing in Data Analytics

The overall aim of this task is to research the well-known [Fisher's Iris data set](https://en.wikipedia.org/wiki/Iris_flower_data_set).

The information in this ReadMe file covers the work necessary to meet the individual objectives set within this task and includes: 
* A summary of the data set
* Addition of the data set to this repository
* A program called analysis.py that explores different types of data analysis of the data set

STEPS
* Research the data set online and provide a summary
* Add the data set to this repository
* Write a program called analysis.py that:
  * Task 1: Outputs a summary of each variable to a single text file
  * Task 2: Saves a histogram of each variable to png files
  * Task 3: Outputs a scatter plot of each pair of variables
  * Additional tasks: Performs any other appropriate analysis


## Fisher's Iris data set

This data set is a well-known benchmark mulivariate data set used for testing out and validating programs <sup>1,2</sup>. It was developed by Ronald Fisher, a statistician and biologist<sup>3</sup>, whose stauch support of eugenics will forever overshadow any contributions he made to his field<sup>4,5</sup>. Fisher developed the data set in 1936 as an example of a linear discriminant analysis<sup>6</sup>.

Nowadays the data set is commonly used as a test case in machine learning techniques<sup>7</sup>. The data set itself contains 50 instances each of 3 classes (types) of iris plant<sup>8</sup> for a total of 150 instances, and can be found [here](https://archive.ics.uci.edu/ml/datasets/iris). 

The information in the data set is laid out as follows<sup>10</sup>:

| Sepal length (cm)  | Sepal Width (cm)    | Petal Length (cm)  | Petal Width (cm)  | Species (cm)  |
|:---------------|:---------------|:--------------|:--------------|----------:|
| 50 data points | 50 data points | 50 data points| 50 data points| setosa    |
| 50 data points | 50 data points | 50 data points| 50 data points| versicolor|
| 50 data points | 50 data points | 50 data points| 50 data points| virginica |

To begin the analysis of this data set we will look at some descriptive summaries, followed by employing the use of the [**Pandas**](https://pandas.pydata.org/) software to manipulate the data, allowing visualisation of the data through [**Matplotlib**](https://matplotlib.org/). The latter half of the analsis will be an exploration into the data visualisation capabilities of [**Seaborn**](https://seaborn.pydata.org/), a 'Python data visualisation library based on Matplotlib'.

### Set-up

Before we begin writing code for the analyses that we would like to explore we need to set-up our environment: 

1. Suggested tools to download/sign-up to to run this program:
* [Visual Studio Code (VSC)](https://code.visualstudio.com/) 
* [Python 3.8 or higher](https://www.python.org/)
* [GitHub website](https://github.com/)

2. Create the program: 
* In this project the file is named [analysis.py](https://github.com/ESutton567/pands-project/blob/main/analysis.py)

3. Import the required modules:
~~~
import pandas as pd
import re
import csv
import matplotlib.pyplot as plt
import seaborn as sns
~~~

4. Download the Iris data set [here](https://archive.ics.uci.edu/ml/datasets/iris) to the same folder you will save your analsyis program, read it into the program, and assign the column names:

~~~
path = '../pands-project/'
filename = path + 'iris_data.csv'
# assign column names
columns = ['sepal_length','sepal_width','petal_length','petal_width', 'species']
~~~

5. Read in the file and locate the target variable within the dataset, i.e. in this case we want to compare between Species of Iris plants (Setosa, Virginia and Versicolor)

~~~
#read in file
iris_data = pd.read_csv(filename, sep= ',', header=None, names=columns)

# locate the target data within the dataset
setosa = iris_data.loc[iris_data['species']=='Iris-setosa']
virginica = iris_data.loc[iris_data['species']=='Iris-virginica']
versicolor = iris_data.loc[iris_data['species']=='Iris-versicolor']
~~~

6. Proceed with the code for the analyses 

### Task 1: Output a summary of each variable to a single text file

* Using the ```open``` command a text file is created and opened. The initial header is written to the file ('w') and subsequent outputs are appended ('a'). 
 * The ```describe``` command outputs a statistics summary for each variable (sepal length, sepal width, petal length and petal width) in the data set
 * The ```dtype``` command outputs the type of of the object, i.e. float, object, etc.
 * the ```info``` command output a concise summary of the data set


~~~
# create a text file to ouptut a summary of the variables
print('Summary statistics for each variable (cm) in the Iris Dataset:\n', file=open('irisVariablesSummary.txt', 'w'))
# append a stats summary of the variables
summary_all = iris_data.describe()
print(summary_all, file=open('irisVariablesSummary.txt', 'a'))

print('\nA list of the type for each variable in the Iris Dataset:\n', file=open('irisVariablesSummary.txt', 'a'))
# append a type summary of the variables
print(iris_data.dtypes, file=open('irisVariablesSummary.txt', 'a'))

print('\nA concise summary of the Iris Dataset: \n', file=open('irisVariablesSummary.txt', 'a'))
print(iris_data.info, file=open('irisVariablesSummary.txt', 'a'))
~~~

# Task 2: Save a histogram of each variable to png files

* 
















References
1. Yen GG, Meesad P. Constructing a fuzzy rule-based system using the ILFN network and Genetic Algorithm. Int J Neural Syst. 2001 Oct;11(5):427-43. doi: 10.1142/S0129065701000618. PMID: 11709810.
2. Woods RP, Hansen LK, Strother S. How many separable sources? Model selection in independent components analysis. PLoS One. 2015 Mar 26;10(3):e0118877. doi: 10.1371/journal.pone.0118877. PMID: 25811988; PMCID: PMC4374758.
3. https://en.wikipedia.org/wiki/Ronald_Fisher
4. Blacker, C.P. (1931). "The sterilization proposals: A history of their development". Eugen Rev. 22 (4): 240. PMC 2984995. PMID 21259955. "Amemorandum was accordingly circulated to the Council signed by Dr. R.A. Fisher, Professor Huxley, Dr. J.A. Ryle, Mr. E.J. Lidbetter, and myself, asking for authorization to form a sub-committee, the aim of which would be to secure the legalization of eugenics sterilization. The memorandum was unanimously approved by the Council, and in this way the nucleus of the existing Committee for Legalizing Eugenic Sterilization was formed."
5. "Report of Committee for Legalizing Eugenic Sterilization". Postgraduate Medical Journal. 6 (61): 13. 1930. doi:10.1136/pgmj.6.61.13. PMC 2531824.
6. FISHER, R.A. (1936), THE USE OF MULTIPLE MEASUREMENTS IN TAXONOMIC PROBLEMS. Annals of Eugenics, 7: 179-188. https://doi.org/10.1111/j.1469-1809.1936.tb02137.x
7. "UCI Machine Learning Repository: Iris Data Set". archive.ics.uci.edu. Retrieved 2017-12-01.
8. https://archive.ics.uci.edu/ml/datasets/iris
9. https://gist.github.com/curran/a08a1080b88344b0c8a7


