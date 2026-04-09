import string
import nltk

nltk.download('stopwords')

from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

# Function to clean text
def clean_text(text):
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Remove stopwords
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]
    
    return " ".join(filtered_words)


user_input = input("Enter a sentence: ")

# Clean the input
result = clean_text(user_input)

# Output
print("\nOriginal Text :", user_input)
print("Cleaned Text  :", result)