Feature Scaling

Feature scaling is a method used to normalize the range of features of data/independent variables . In data processing, it is also known as data normalization/standardization and is generally performed during the data processing step. It is also to use feature scaling if you use regularisation in your model.

What Is Feature Scaling (Standardization)?

Imagine you're learning to compare different fruits by their weight and sweetness. If one fruit’s weight is measured in grams (like 150g) and another’s sweetness is measured on a scale from 1 to 10, the numbers are on very different scales. Feature scaling is like adjusting these numbers so they are on a similar scale. This helps when you're trying to analyze or compare them fairly.

Standardization (a Type of Feature Scaling)

Standardization is one method of feature scaling. It transforms your data so that:

The mean (average) of the data becomes 0.
The standard deviation (how spread out the data is) becomes 1.
This transformation is done by the formula: Standardized Value = (original value - Mean)/Standard Deviation

Why Do We Use Standardization?

Equal Contribution: In many machine learning models, features with larger values can dominate the results. Standardization ensures that each feature contributes equally.
Improved Performance: Some algorithms (like gradient descent in neural networks or k-nearest neighbors) work better and converge faster when the features are on a similar scale.
Handling Different Units: When features have different units (e.g., weight in kg vs. height in cm), standardization helps put them on the same footing.
Real-World Scenario Example

Imagine you are building a model to predict house prices. You have two features:

Size of the house (in square feet)
Age of the house (in years)
These features are on different scales. A house size could be 1,500 to 3,000 square feet, while the age might be between 1 and 50 years. Without scaling, the size might overly influence the model. Standardizing both features helps the model treat them equally.

Simple Python Code Example Using StandardScaler

Below is a simple example using Python and the popular scikit-learn library to standardize features

# Step 1: Import necessary libraries
import numpy as np
from sklearn.preprocessing import StandardScaler

# Step 2: Create some sample data
# Let's assume we have data for house size and age:
# Each row represents one house: [size in square feet, age in years]
data = np.array([
    [1500, 10],
    [2000, 20],
    [2500, 30],
    [3000, 40]
])

print("Original Data:")
print(data)

# Step 3: Initialize the StandardScaler
scaler = StandardScaler()

# Step 4: Fit the scaler to our data and transform the data
scaled_data = scaler.fit_transform(data)

print("\nStandardized Data:")
print(scaled_data)

# Optional: Check the mean and standard deviation of the scaled data
print("\nMean of each feature after scaling (should be ~0):")
print(scaled_data.mean(axis=0))

print("\nStandard deviation of each feature after scaling (should be ~1):")
print(scaled_data.std(axis=0))


Explanation of the Code:

Importing Libraries:
We import NumPy for handling arrays and StandardScaler from scikit-learn for standardization.

Creating Sample Data:
The data array has rows of houses with two features each: size and age.

Initializing StandardScaler:
We create an instance of StandardScaler which will handle the standardization.

Fitting and Transforming:
The fit_transform method calculates the mean and standard deviation for each feature and scales the data accordingly.

Checking Results:
We print the standardized data. The means should be close to 0 and standard deviations close to 1 for each feature.

Conclusion:

Feature scaling, especially standardization, is a crucial step in preparing your data for many machine learning models. It ensures that all features contribute equally to the analysis, improves model performance, and makes the training process more efficient.
