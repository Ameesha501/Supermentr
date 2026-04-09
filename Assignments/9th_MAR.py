'''
9th *March*

House Price Predictor

In this assignment, a simple House Price Prediction system is developed using the Linear Regression algorithm. The model learns from past housing data such as area, number of bedrooms, and age of the house. After training, the program allows the user to enter details of a new house. Based on the learned relationship between these features and price, the model predicts an estimated house price. This assignment helps in understanding how machine learning can be applied in real-life scenarios like real estate price estimation.
'''

import pandas as pd
from sklearn.linear_model import LinearRegression

house_data = {
    "Area": [1000, 1500, 1800, 2400, 3000],
    "Bedrooms": [2, 3, 3, 4, 4],
    "Age": [10, 5, 7, 3, 1],
    "Price": [50, 65, 72, 90, 110]
}

data = pd.DataFrame(house_data)

X = data[["Area", "Bedrooms", "Age"]]   # Inputs
y = data["Price"]                       # Output (Price)

model = LinearRegression()
model.fit(X, y)

print("\nEnter details of the house to predict price")
area = float(input("Enter area in square feet: "))
bedrooms = int(input("Enter number of bedrooms: "))
age = int(input("Enter age of the house (years): "))

# Predict the house price
new_house = [[area, bedrooms, age]]
predicted_price = model.predict(new_house)

# Display the predicted price
print("\nEstimated House Price:", round(predicted_price[0], 2), "Lakhs")