
from sklearn.feature_extraction.text import TfidfVectorizer

# -------- USER INPUT --------
documents = []

print("Enter 5 documents:\n")

for i in range(5):
    doc = input(f"Enter document {i+1}: ")
    documents.append(doc)

# Create TF-IDF model
vectorizer = TfidfVectorizer(stop_words='english')

# Transform documents into TF-IDF matrix
tfidf_matrix = vectorizer.fit_transform(documents)

# Get feature names (words)
feature_names = vectorizer.get_feature_names_out()

# Convert matrix to array
tfidf_array = tfidf_matrix.toarray()

# Display top keywords
for i, doc in enumerate(tfidf_array):
    print(f"\nDocument {i+1} Top Keywords:")
    
    word_scores = list(zip(feature_names, doc))
    
    # Sort by highest TF-IDF score
    sorted_words = sorted(word_scores, key=lambda x: x[1], reverse=True)
    
    # Show top 3 words
    for word, score in sorted_words[:3]:
        print(f"{word} : {round(score, 3)}")