# Count or number of values

boston_df.count()

# Mean Value - Column Wise

boston_df.mean()

# Standard Deviation - Column Wise

boston_df.std()

# Give all statistical measures
boston_df.describe()

boston_df.min()

boston_df.max()

# adding a column to the data frame

boston_df['Price'] = boston_dataset.target

# Removing a particular row

boston_df.drop(index=1, axis=0)

# Drop a column

boston_df.drop(columns='Price', axis=1) # axis=1 for dropping column and axis = 0 for row.

# Locating a row using the index value

boston_df.iloc[3]

# Locate a particular column

boston_df.iloc[:,0] # First Column
boston_df.iloc[:,3] # Fourth Column
boston_df.iloc[:,-1] # Last Column


