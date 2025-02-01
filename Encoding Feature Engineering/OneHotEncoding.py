https://colab.research.google.com/drive/1SzQesAO_6_9IeJ1C8Ni00tPuzeeJc0v-#scrollTo=or6JsS7GHhJ1


Lets say we are trying to predict prices of houses in different towns. How should we handle text data in numeric model(Ex: town name). We use numeric value instead of names to categorize like 1 for sylhet, 2 for Dhaka. But the problem with this approach is that after we assign this values and give it to our model... it will assume that there is an order like dhaka comes after sylhet as numbers have ordinal relationship like 1 is less than 2 etc. The model will start making this assumptions and it quite doesn't make sense.

Categorical Variables:

Nominal --> Town Names, Male or Female, green red or blue

In some cases we use Ordinal --> Satisfied neutral or dissatisfied, graduate<masters<phd , low<medium<high etc.

We use one hot encoding. We assign binary values.

import pandas as pd
df = pd.read_csv("carprices.csv")
print(df)

dummies = pd.get_dummies(df['Car Model'])
merged = pd.concat([df,dummies],axis='columns')

# Rule of the thumb --> Drop one of the dummies column to not create dummy variable trap.

final = merged.drop(['Car Model','Mercedez Benz C class'], axis='columns')
final

from sklearn.linear_model import LinearRegression
model = LinearRegression()

X = final.drop('Sell Price($)', axis='columns')
X

Y = final['Sell Price($)']
Y

model.fit(X,Y)

model.predict([[50000,5,False,True]])

model.score(X,Y) # Check how much accurate it is. Here its 94% accurate. 
0.9417050937281082

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

dfle = df
dfle['Car Model'] = le.fit_transform(dfle['Car Model'])
dfle

X = dfle[['Car Model','Mileage','Age(yrs)']].values
X

Y = dfle['Sell Price($)']
Y

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
ct = ColumnTransformer([('Car Model', OneHotEncoder(), [0])], remainder = 'passthrough')  

X = ct.fit_transform(X)
X

X = X[:,1:] # Drop the 0th column
X

model.fit(X,Y)
model.predict([[0,1,50000,5]])
array([33808.25311106])

