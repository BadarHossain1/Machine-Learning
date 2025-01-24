sns.barplot(data=titanic, x='sex', y='survived', hue='class')

# house price dataset

from sklearn.datasets import fetch_california_housing
house_boston = fetch_california_housing()

house = pd.DataFrame(house_boston.data, columns=house_boston.feature_names)
house['PRICE'] = house_boston.target

house.head()

