import pandas as pd 

import matplotlib 
from matplotlib import pyplot as plt
%matplotlib inline
matplotlib.rcParams['figure.figsize'] = (10, 6)



import pandas as pd

# Create a dictionary with gender and height data
data = {'gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
        'height': [180, 165, 175, 170, 181]}

# Create a pandas DataFrame from the dictionary
df = pd.DataFrame(data)

# Display the DataFrame


plt.hist(df['height'], bins=20, rwidth=0.8)
plt.xlabel('Height (cm)')
plt.ylabel('Count of people with that height')
plt.title('Distribution of Height')
plt.show()


from scipy.stats import norm
import numpy as np

plt.hist(df['height'], bins=20, rwidth=0.8, density=True)
plt.xlabel('Height (cm)')
plt.ylabel('Count')
plt.title('Distribution of Height')

rng = np.arange(df['height'].min(), df['height'].max())
plt.plot(rng, norm.pdf(rng, df['height'].mean(), df['height'].std()))
plt.show()


Standard Deviation outlier removal
upper_limit = df['height'].mean() + 3*df['height'].std()
upper_limit

lower_limit = df['height'].mean() - 3*df['height'].std()
lower_limit


df_no_outlier = df[(df['height'] < upper_limit) & (df['height'] > lower_limit)]
df_no_outlier # Less data and no outliers so not working. 

import pandas as pd
import numpy as np

# Sample data (replace with your actual data)
data = {'value': [1, 2, 3, 4, 5, 100]}  # Example with an outlier (100)
df = pd.DataFrame(data)

# Calculate z-scores
df['zscore'] = np.abs((df['value'] - df['value'].mean()) / df['value'].std())

# Define a threshold for outlier detection (e.g., z-score > 3)
threshold = 3

# Remove outliers
df_no_outliers = df[df['zscore'] <= threshold]

# Display the results
print("Original DataFrame:")
print(df)
print("\nDataFrame without outliers:")
df_no_outliers
