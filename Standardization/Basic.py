https://colab.research.google.com/drive/1tFxfxHKytKs9lNBHM2vumz8COu5UrbaW#scrollTo=zI9clOL39cr2


Data Standardization The process of standardizing the data to a common format and common range

import numpy as np
import pandas as pd
import sklearn.datasets
from sklearn.preprocessing import StandardScaler #This is used to standardize our data
from sklearn.model_selection import train_test_split

# Loading the dataset
dataset = sklearn.datasets.load_breast_cancer()
print(dataset)

# Loading the data to a pandas dataframe
df = pd.DataFrame(dataset.data, columns=dataset.feature_names)

df.head()
df.shape

X=df
Y = dataset.target
print(X)
print(Y)

Splitting the data into training data and test data

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=3) # 0.2 means 20 percent of data taken.
print(X.shape, X_train.shape, X_test.shape)
(569, 30) (455, 30) (114, 30)



Standardize the data

print(dataset.data.std()) # The data is not in the same range here. If in same range then output will be 1.
scaler = StandardScaler()

scaler.fit(X_train)

X_train_standardized = scaler.transform(X_train)
print(X_train_standardized.std()) # Nice!
1.0

X_test_standardized = scaler.transform(X_test)
print(X_test_standardized.std()) # Nice! Close to 1 .
0.8654541077212674

