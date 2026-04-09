''' 26th Feb

Assignment Name : Data Doctor
Description : Clean a dataset by handling missing values, removing duplicates, standardizing text, and explain why cleaning matters.
'''
import pandas as pd

# Load dataset
data = pd.read_csv("/content/iris.csv")

# Display first few rows
print("Original Data:")
print(data.head())

# Handle missing values (fill with mean for numeric columns)
data = data.fillna(data.mean(numeric_only=True))

# Remove duplicate rows
data = data.drop_duplicates()

# Standardize text (convert text columns to lowercase)
for column in data.select_dtypes(include='object').columns:
    data[column] = data[column].str.lower()

# Display cleaned dataset
print("\nCleaned Data:")
print(data.head())


'''
Explanation

The dataset is loaded using the pandas library.

Missing values in numeric columns are replaced with the column mean.

Duplicate rows are removed to avoid repeated data.

Text data is converted to lowercase to maintain consistency.

Why Data Cleaning Matters

Improves data accuracy and reliability.

Prevents errors in analysis or machine learning models.

Ensures consistent and standardized data format.

Removes redundant or incorrect information.

Helps in producing better insights and predictions.
'''
