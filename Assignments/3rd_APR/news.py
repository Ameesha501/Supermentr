# Fake News Detector (Using CSV)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# load dataset
df = pd.read_csv("D:/Supermentr/Tasks/3rd_APR/fake_news_dataset.csv")

# split data
X = df["text"]
y = df["label"]

# train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# convert text to numbers
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# train model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# test accuracy
predictions = model.predict(X_test_vec)
print("Accuracy:", accuracy_score(y_test, predictions))

# user input
user_input = input("Enter news: ")
user_vec = vectorizer.transform([user_input])

# prediction
result = model.predict(user_vec)

if result[0] == 1:
    print("REAL news ✅")
else:
    print("FAKE news ❌")