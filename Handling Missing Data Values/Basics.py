Methods to hanlde missing values

1: Imputation. 2: Dropping

Importing the libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading the dataset to our pandas data frame

dataset = pd.read_csv('/content/Placement_Dataset.csv')
dataset.head()
https://drive.google.com/file/d/1YMSWDJ0lM8Rm81J-u4B_VyiQjGi1kDTA/view

dataset.shape
dataset.isnull().sum() # Gives numbers of missing values in a column


Central Tendencies

Mean --> Average of all values
Median --> Arrange the values in ascending order and take the middle value from the order or take mean or average of two middle values when there are even amount of numbers.
Mode --> The number which is repeated for most amount of times.

# Analyze the distribution of Data in the salary

fig, ax = plt.subplots(figsize=(8,8))
sns.distplot(dataset['salary'])
plt.show()

The graph shows that its skew. The thing is that after 6 lakhs there are values but mostly the values are concentrated in the 0.2-0.4 lakh. So, we cant use mean as it will effect the entire dataset. For example: 10 people got jobs, out of them 8 people have a salary of 3 lakh taka where as 2 have 10 lakh taka salary. These two are outliers. We wont get an accurate dataset using mean. So, we use median and mode in this scenarios.


