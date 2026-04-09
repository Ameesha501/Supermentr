import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

text = "I am learning NLP and it is very exciting!!!"

# 1. Original text
print("Original:", text)

# 2. Lowercase
text = text.lower()
print("Lowercase:", text)

# 3. Remove punctuation
text = re.sub(r'[^a-z\s]', '', text)
print("No punctuation:", text)

# 4. Tokenization (split)
words = text.split()
print("Tokens:", words)

# 5. Remove stopwords
words = [w for w in words if w not in stopwords.words('english')]
print("After stopword removal:", words)

# 6. Stemming
ps = PorterStemmer()
words = [ps.stem(w) for w in words]
print("After stemming:", words)