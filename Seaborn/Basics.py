import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


Note: Seaborn has some built-in datasets

# total bill vs tip dataset

tips = sns.load_dataset('tips')

tips.head()

# setting a theme for the plots

sns.set_theme()

# visualize the data

sns.relplot(data = tips, x='total_bill', y='tip', hue='smoker', style='time', size='size')

# load the iris dataset

iris = sns.load_dataset('iris')

iris.head()

from google.colab import sheets
sheet = sheets.InteractiveSheet(df=iris)

