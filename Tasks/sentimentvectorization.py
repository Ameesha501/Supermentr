# Import libraries
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import pandas as pd

# Dataset
sentences = [
    "I love this movie",
    "This movie is terrible",
    "Amazing acting",
    "Worst film ever"
]

# -----------------------
# 1. Bag of Words (BoW)
# -----------------------
bow = CountVectorizer()
bow_matrix = bow.fit_transform(sentences)

print("Bag of Words Vocabulary:")
print(bow.get_feature_names_out())

print("\nBoW Matrix:")
print(bow_matrix.toarray())

# -----------------------
# 2. TF-IDF
# -----------------------
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(sentences)

print("\nTF-IDF Vocabulary:")
print(tfidf.get_feature_names_out())

print("\nTF-IDF Matrix:")
print(tfidf_matrix.toarray())

# -----------------------
# 3. Visualize using pandas# Import libraries
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import pandas as pd

# Dataset
sentences = [
    "I love this movie",
    "This movie is terrible",
    "Amazing acting",
    "Worst film ever"
]

# -----------------------
# 1. Bag of Words (BoW)
# -----------------------
bow = CountVectorizer()
bow_matrix = bow.fit_transform(sentences)

print("BoW Vocabulary:")
print(bow.get_feature_names_out())

print("\nBoW Matrix:")
print(bow_matrix.toarray())

# Convert to DataFrame (for better view)
bow_df = pd.DataFrame(bow_matrix.toarray(), columns=bow.get_feature_names_out())
print("\nBoW DataFrame:\n", bow_df)

# -----------------------
# 2. TF-IDF
# -----------------------
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(sentences)

print("\nTF-IDF Vocabulary:")
print(tfidf.get_feature_names_out())

print("\nTF-IDF Matrix:")
print(tfidf_matrix.toarray())

# Convert to DataFrame
tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=tfidf.get_feature_names_out())
print("\nTF-IDF DataFrame:\n", tfidf_df)
# -----------------------
df = pd.DataFrame(tfidf_matrix.toarray(), columns=tfidf.get_feature_names_out())
print("\nTF-IDF DataFrame:")
print(df)