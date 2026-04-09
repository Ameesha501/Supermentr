import pandas as pd
from sklearn.linear_model import LinearRegression

# Create dataset
data = {
    "Study_Hours": [1,2,3,4,5,6,7,8,9,10],
    "Marks": [40,45,50,55,60,65,70,80,88,95]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Feature (Input) and Label (Output)
X = df[["Study_Hours"]]
y = df["Marks"]

# Train a simple ML model
model = LinearRegression()
model.fit(X, y)

# Take user input
hours = float(input("Enter study hours: "))

# Predict marks
predicted_marks = model.predict([[hours]])

print("Predicted Marks:", predicted_marks[0])