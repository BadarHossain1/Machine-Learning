https://colab.research.google.com/drive/1-mBxZG5129bxlDcLCBx3DCEecX0smWkB#scrollTo=DhWKy8edOkC0

Normalization in data transformation

It is used to scale and standardize the features of a dataset
Primary goal is to bring all the features to a similar scale, typically between 0 and 1
Min-Max normalization Technique
Z-score normalization Technique


Min-Max technique:
x' = (x - min)/max-min where x is the value.

Lets say we have square foot column with values like 1200, 1500 etc. Limit this values using the above formula to bring it in the range of [0-1].

Z-Score Technique
x' = (x-min)/standard deviation

Standard deviation is (value1 - mean)^2 + ......./Total No. of Values.


from sklearn.preprocessing import MinMaxScaler

scaling = MinMaxScaler()
scaling.fit_transform(df[['square_feet']])

Standardization(Z-score Normalization)

from sklearn.preprocessing import StandardScaler
scaling.fit_transform(df[['square feet']])