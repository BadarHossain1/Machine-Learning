Correlation:

Positive Correlation
Negative Correlation

Heat Map
correlation = house.corr()
# constructing a heat map

plt.figure(figsize=(10,10))
sns.heatmap(correlation, cbar=True, square=True, fmt='.1f', annot=True, annot_kws={'size':8}, cmap='Blues')

