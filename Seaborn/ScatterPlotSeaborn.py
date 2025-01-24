sns.scatterplot(data=iris, x = 'sepal_length', y = 'sepal_length', hue = 'species')

sns.scatterplot(data=iris, x = 'sepal_length', y = 'sepal_width', hue = 'species')

# Loading the titanic dataset

titanic = sns.load_dataset('titanic')

titanic.head()

