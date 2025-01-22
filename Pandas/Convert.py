Importing data from a csv file

# csv file to pandas df

pizza_df = pd.read_csv('/content/order_details.csv')

type(pizza_df)
pandas.core.frame.DataFrame

pizza_df.head()

pizza_df.shape

Loading the data from a excel file to a pandas data frame

pd.read_excel('file path')

Exporting a Data Frame to a csv file
boston_df.to_csv('boston_df.csv')

Exporting the pandas data frame to a excel file
boston_df.to_excel('boston_df.xlsx')

# Creating a Data Frame with random values.

random_df = pd.DataFrame(np.random.rand(20,10))
random_df.head()

random_df.shape