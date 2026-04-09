import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

df = pd.read_csv("reviews.csv")

X_train, X_test, y_train, y_test = train_test_split(
    df["review"], df["label"], test_size=0.2, random_state=42
)

vec = TfidfVectorizer(stop_words='english', ngram_range=(1,2))
X_train = vec.fit_transform(X_train)
X_test = vec.transform(X_test)

model = MultinomialNB()
model.fit(X_train, y_train)

pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, pred))

while True:
    text = input("Enter review: ")
    if text.lower() == "exit":
        break
    print("Sentiment:", model.predict(vec.transform([text]))[0])