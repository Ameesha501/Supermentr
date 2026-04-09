# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Sample dataset
data = {
    "year": [2015, 2018, 2012, 2020, 2016, 2019],
    "km_driven": [50000, 30000, 70000, 20000, 60000, 25000],
    "fuel_type": [0, 1, 0, 1, 0, 1],  # 0=Petrol, 1=Diesel
    "price": [500000, 800000, 300000, 900000, 450000, 850000]
}

df = pd.DataFrame(data)

# Features and target
X = df[["year", "km_driven", "fuel_type"]]
y = df["price"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# -----------------------
# User Input
# -----------------------
year = int(input("Enter car year: "))
km = int(input("Enter km driven: "))
fuel = input("Enter fuel type (petrol/diesel): ").lower()

# Convert fuel type
if fuel == "petrol":
    fuel = 0
else:
    fuel = 1

# Predict
new_car = [[year, km, fuel]]
price = model.predict(new_car)

print("Predicted Car Price:", int(price[0]))