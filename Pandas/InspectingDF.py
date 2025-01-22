# Finding the number of rows and columns

boston_df.shape

# Print First 5 rows

boston_df.head()

# Print the last 5 rows of the data frame
boston_df.tail()

# Information about Data Frame

boston_df.info()

# Function to find the number of missing value

boston_df.isnull().sum()

# Pizza data frame
pizza_df.head()

# Counting the values based on the labels (How many people ordered 4 pizzas)

pizza_df.value_counts('quantity')
count
quantity	
1	47693
2	903
3	21
4	3


boston_df.groupby('HouseAge').mean()
	MedInc	AveRooms	AveBedrooms	Population	AveOccupied	Latitude	Longitude
HouseAge							
1.0	4.003400	9.088091	1.552106	328.500000	3.244088	36.205000	-119.457500
2.0	5.167766	7.649087	1.273514	2083.051724	2.747802	35.494483	-119.121379
3.0	5.460258	6.851805	1.192486	3001.774194	2.734708	35.284516	-118.936452

