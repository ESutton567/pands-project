# This program downloads Fisher's Iris Dataset from a specified URL
# Author: Éilis Sutton

from urllib.request import urlretrieve
urlretrieve("https://www.kaggle.com/datasets/arshid/iris-flower-dataset?select=IRIS.csv", "iris.csv")

