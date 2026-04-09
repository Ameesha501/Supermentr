# Install (run once)
# pip install nltk

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download required data
nltk.download('vader_lexicon')

# Initialize analyzer
sia = SentimentIntensityAnalyzer()

# Function to analyze sentiment
def analyze_sentiment(review):
    score = sia.polarity_scores(review)
    
    if score['compound'] >= 0.05:
        return "Positive 😊"
    elif score['compound'] <= -0.05:
        return "Negative 😞"
    else:
        return "Neutral 😐"

# Take number of reviews from user
n = int(input("Enter number of reviews: "))

reviews = []

# Taking user input
for i in range(n):
    review = input(f"Enter review {i+1}: ")
    reviews.append(review)

print("\n--- Sentiment Analysis Result ---\n")

# Analyze and print results
for i, review in enumerate(reviews, 1):
    result = analyze_sentiment(review)
    print(f"Review {i}: {review}")
    print(f"Sentiment: {result}")
    print("-" * 50)