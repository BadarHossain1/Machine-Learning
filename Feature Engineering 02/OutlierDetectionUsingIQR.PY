

import numpy as np

# Sample data
data = [10, 12, 15, 18, 20, 22, 25, 100]  # 100 is an outlier

# Calculate the first quartile (Q1) and third quartile (Q3)
q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)

# Calculate the interquartile range (IQR)
iqr = q3 - q1

# Define the lower and upper bounds for outliers
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

# Identify outliers
outliers = [x for x in data if x < lower_bound or x > upper_bound]

# Print results
print("Q1:", q1)
print("Q3:", q3)
print("IQR:", iqr)
print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)
print("Outliers:", outliers)
