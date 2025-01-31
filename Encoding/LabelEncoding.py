https://colab.research.google.com/drive/1wBxJY6ggMlMZmKXStp40EeZxAzcV3LOv#scrollTo=wbyK4dLy8R21

Label Encoding

Converting the labels into numeric form

# Importing the dependencies

import pandas as pd
from sklearn.preprocessing import LabelEncoder

Label Encoding of Breast Cancer Dataset
cancer_data = pd.read_csv('/content/cancerData.csv')

cancer_data.head()
cancer_data['diagnosis'].value_counts()

# load the label encoder function
label_encode = LabelEncoder()

labels = label_encode.fit_transform(cancer_data.diagnosis)

# appending the labels to the dataframe

cancer_data['target'] = labels


0-> Benign 1-> Malingnant

cancer_data['target'].value_counts()

