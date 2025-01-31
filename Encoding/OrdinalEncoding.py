# prompt: write code and show simple example of ordinal encoding

import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

# Sample data
data = {'color': ['red', 'green', 'blue', 'red', 'green'],
        'size': ['small', 'medium', 'large', 'small', 'medium']}
df = pd.DataFrame(data)

# Initialize OrdinalEncoder
encoder = OrdinalEncoder()

# Fit and transform the data
encoded_data = encoder.fit_transform(df)

# Create a new DataFrame with encoded data
encoded_df = pd.DataFrame(encoded_data, columns=df.columns)

print("Original DataFrame:")
print(df)
print("Encoded DataFrame:")
print(encoded_df)

df['color'] = encoded_df['color']
print(df)