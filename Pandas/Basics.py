Pandas Library: Useful for data processing and analysis

Pandas Data Frame: Pandas Data Frame is two dimensional data structure with labeled axis (rows and columns)

# Importing pandas Library
import pandas as pd
import numpy as np

Create a pandas Data Frame
from sklearn.datasets import fetch_california_housing
boston_dataset = fetch_california_housing()

type(boston_dataset)
sklearn.utils._bunch.Bunch

print(boston_dataset)

# pandas Data Frame
# loading data to the data frame called boston_df
boston_df = pd.DataFrame(boston_dataset.data, columns=boston_dataset.feature_names)

# print first five rows

boston_df.head()

boston_df.shape