Import Datasets from Kaggle Directly through API Call

# Installing the kaggle Library

!pip install kaggle # "! System command should be proceeded with this exclamatory mark"


Uploading your kaggle json file after creating a new token in settings of kaggle.

# Configuring the path of kaggle.json file

!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

Importing the Earthquake Dataset

# API to fetch the dataset from kaggle

!kaggle competitions download -c LANL-Earthquake-Prediction




# extracting the compressed dataset

from zipfile import ZipFile
dataset = '/content/LANL-Earthquake-Prediction.zip'

with ZipFile(dataset,'r') as zip:
  zip.extractall()
  print('The dataset is extracted')
  

The dataset is extracted....................