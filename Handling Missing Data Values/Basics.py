https://colab.research.google.com/drive/1uBaEUKl0ECxl-taRCkD9EM5A7p6frQJ4#scrollTo=hkrKtOD9mBQF

Methods to handle missing values

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


Replace the missing values with Median Value
dataset['salary'].fillna(dataset['salary'].median(), inplace=True)

# check if there is still missing values

dataset.isnull().sum()

# Filling missing places with Mean value
dataset['salary'].fillna(dataset['salary'].mean(), inplace=True)

Dropping Method

salary_dataset = pd.read_csv('/content/Placement_Dataset.csv')
salary_dataset.isnull().sum()

# Drop the missing values

salary_dataset = salary_dataset.dropna(how='any')
salary_dataset.isnull().sum()

salary_dataset.shape
(148, 15)