4000 5000 6000 7000 7500 8000 10000000

Remove the outlier:
percentile_99 = df.income.quantile(0.99)
df = df[df.income <= percentile_99]

Outlier Removed after getting the 99% of the value and then updating the data frame df with values of income less than the 99% value.
