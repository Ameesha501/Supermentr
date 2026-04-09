# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import pickle

# Create sample dataset (since no file given)
data = {
    "Income": [50000, 60000, 30000, 80000, 40000],
    "CreditScore": [700, 750, 650, 800, 600],
    "Age": [25, 35, 45, 30, 50],
    "LoanAmount": [200000, 250000, 100000, 300000, 150000],
    "EmploymentYears": [2, 5, 10, 3, 8],
    "Approved": [1, 1, 0, 1, 0]   # Target
}

df = pd.DataFrame(data)

# Split input and output
X = df.drop("Approved", axis=1)
y = df["Approved"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Decision Tree
dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)
dt_acc = dt.score(X_test, y_test)

# Random Forest
rf = RandomForestClassifier()
rf.fit(X_train, y_train)
rf_acc = rf.score(X_test, y_test)

# Compare accuracy
print("Decision Tree Accuracy:", dt_acc)
print("Random Forest Accuracy:", rf_acc)

# Feature importance (Random Forest)
print("\nFeature Importance:")
for name, value in zip(X.columns, rf.feature_importances_):
    print(name, ":", value)

# Save model
pickle.dump(rf, open("loan_model.pkl", "wb"))
print("\nModel saved!")