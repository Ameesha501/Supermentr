''' 24th Feb

Assignment Name : Dataset Detective
Description : Load a dataset, display top rows, find highest value column, count missing values, share 5 insights.
''' 
import pandas as pd

# Load dataset (example: CSV file)
data = pd.read_csv("/content/iris.csv")

# Display top rows
print("Top 5 Rows of Dataset:")
print(data.head())

# Find column with highest value
highest_column = data.max(numeric_only=True)
print("\nHighest Value in Each Numeric Column:")
print(highest_column)

# Count missing values
missing_values = data.isnull().sum()
print("\nMissing Values in Each Column:")
print(missing_values)


