Again! When there are outliers, we dont use average to handle missing values, we use median or mode. 

Percentile --> lets see some data

4000 5000 6000 7000 7500 8000 10000000

From above we can say that the 50th Percentile is 7000, there are three values less than 7000 and three values more.

What is the 25th percentile?
Ans: 25% of 7 is 1.75 which is approximately 2 data points.

So, draw a line after two points, that will be the value. Here the answer is 5500.

Code:

df.column_Name.quantile(0.25) --> 5500
df.column_Name.quantile(0.25, interpolation="lower") --> 5000
df.column_Name.quantile(0.25, interpolation="higer") --> 6000
