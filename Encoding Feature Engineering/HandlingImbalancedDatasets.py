https://colab.research.google.com/drive/1jwfxIJWKQRLoO1ZGZp6Nn8sRHA_eMPiq#scrollTo=ZHoIX9nk2Blb

Imbalanced Dataset

A dataset with an unequal class distribution

# Importing the dependencies

import numpy as np
import pandas as pd

# Loading the dataset to pandas Dataframe
credit_card_data = pd.read_csv('/content/credit_data.csv')

credit_card_data.head()

# Distribution of two classes

credit_card_data['Class'].value_counts()

count
Class	
0	284315
1	492


This is highly Imbalanced Datasheet

0 --> Legal and Legit 1 --> Fraudulent.

# Seperating the legit and fraudulent transactions.

legit = credit_card_data[credit_card_data.Class == 0]
fraud = credit_card_data[credit_card_data.Class == 1]

print(legit.shape)
print(fraud.shape)
(284315, 31)
(492, 31)

Undersampling

Build a sample dataset containing similar distribution of legit and fraudulent transactions.

Number of fraudulent transactions = 492

legit_sample = legit.sample(n=492) # Take 492 random values out of 284315 values to make a balance.

print(legit_sample.shape)
(492, 31)

Concatenate the two Data Frames

new_dataset = pd.concat([legit_sample, fraud], axis=0) # axis = 0 means on top of another. Legit on top and fraud on bottom which means concat row wise

new_dataset.head()
new_dataset.tail()

new_dataset['Class'].value_counts()

count
Class	
0	492
1	492
Now we have evenly distributed dataset.

