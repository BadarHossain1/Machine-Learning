# prompt: outlier detection and removal using percentile with simple dataset of height simple

import pandas as pd

# Sample height data (replace with your actual data)
data = {'height': [150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 220]}  # Added an outlier (220)
df = pd.DataFrame(data)

# Calculate the 5th and 95th percentiles
lower_bound = df['height'].quantile(0.05)
upper_bound = df['height'].quantile(0.95)

# Filter out the outliers
df_filtered = df[(df['height'] >= lower_bound) & (df['height'] <= upper_bound)]

print("Original DataFrame:\n", df)
print("\nDataFrame after outlier removal:\n", df_filtered)


Original DataFrame:
     height
0      150
1      155
2      160
3      165
4      170
5      175
6      180
7      185
8      190
9      195
10     220

DataFrame after outlier removal:
    height
1     155
2     160
3     165
4     170
5     175
6     180
7     185
8     190
9     195
