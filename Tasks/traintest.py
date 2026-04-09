# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Create dataset
data = {
    "income": [50000, 60000, 30000, 80000, 40000],
    "credit_score": [700, 750, 650, 800, 600],
    "loan_amount": [200000, 250000, 100000, 300000, 150000],
    "employment_years": [2, 5, 1, 6, 3],
    "loan_approved": [1, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

# Split input and output
X = df[["income", "credit_score", "loan_amount", "employment_years"]]
y = df["loan_approved"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Check accuracy
accuracy = model.score(X_test, y_test)
print("Accuracy:", accuracy)

# Predict new customer
new_customer = [[55000, 720, 180000, 3]]
prediction = model.predict(new_customer)

print("Loan Approved (1=Yes, 0=No):", prediction[0])