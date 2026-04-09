import pandas as pd

# Create dataset
data = {
    "Study_Hours": [1,2,3,4,5,6,7,8,9,10],
    "Marks": [40,45,50,55,60,65,70,80,88,95]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Display dataset
print("Dataset:")
print(df)

# Identify feature and label
feature = df[["Study_Hours"]]
label = df["Marks"]

print("\nFeature (Input):")
print(feature)

print("\nLabel (Output):")
print(label)

# Relationship explanation
print("\nRelationship: As study hours increase, marks also increase.")