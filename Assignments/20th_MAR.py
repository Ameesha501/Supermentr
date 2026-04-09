# Install (run once in terminal)
# pip install nltk emoji autocorrect

import re
import nltk
import emoji
from autocorrect import Speller

# Download required NLTK data (run once)
nltk.download('stopwords')

from nltk.tokenize import wordpunct_tokenize   # ✅ simple tokenizer
from nltk.corpus import stopwords

# Initialize spell checker and stopwords
spell = Speller(lang='en')
stop_words = set(stopwords.words('english'))

# 20 messy sentences
sentences = [
    "Heyyy brooo 😎 what’s up??",
    "I cant beleive this happend!",
    "LOL that was sooo funny 😂😂",
    "Gonna meet u tmrw 👍",
    "This is amazng!!!",
    "Idk what ur saying 😕",
    "Plzz send me d details ASAP",
    "I luv this song 🎶",
    "Wat r u doing rn?",
    "Soo tired of this 😴",
    "Ths is nt gud",
    "OMG!!! This is lit 🔥",
    "C u soon 😊",
    "Why r u late again???",
    "I am sooo happpy today!!! 😍",
    "He dont knw anything",
    "Pls hlp me wid dis",
    "That movie was awsm 😁",
    "Im feelng sick 🤒",
    "Yaar this is too gud 😅"
]

# Slang dictionary
slang_dict = {
    "u": "you", "tmrw": "tomorrow", "lol": "laughing",
    "idk": "i do not know", "pls": "please", "ur": "your",
    "rn": "right now", "gonna": "going to", "luv": "love",
    "awsm": "awesome", "gud": "good", "wat": "what",
    "r": "are", "c": "see", "d": "the", "wid": "with"
}

# Function to identify issues
def identify_issues(text):
    issues = []
    
    # Check emojis
    if emoji.emoji_count(text) > 0:
        issues.append("Emoji")
    
    # Check repeated letters
    if re.search(r'(.)\1{2,}', text):
        issues.append("Repeated letters")
    
    # Check slang words
    words = re.findall(r'\b\w+\b', text.lower())
    if any(word in slang_dict for word in words):
        issues.append("Slang")
    
    # Check common typos
    if re.search(r'\b(beleive|happend|amazng|happpy|feelng|knw|hlp|ths|nt)\b', text.lower()):
        issues.append("Typo")
    
    return ", ".join(issues)


# Preprocessing function
def preprocess(text):
    # 1. Convert to lowercase
    text = text.lower()
    
    # 2. Remove emojis
    text = emoji.replace_emoji(text, replace='')
    
    # 3. Remove special characters
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # 4. Reduce repeated letters (heyyy → heyy)
    text = re.sub(r'(.)\1{2,}', r'\1\1', text)
    
    # 5. Tokenization (split into words)
    words = wordpunct_tokenize(text)
    
    # 6. Replace slang words
    words = [slang_dict.get(word, word) for word in words]
    
    # 7. Correct spelling
    words = [spell(word) for word in words]
    
    # 8. Remove stopwords (like "is", "the", etc.)
    words = [w for w in words if w not in stop_words]
    
    # 9. Join words back into sentence
    return " ".join(words)


# Process all sentences
for i, sentence in enumerate(sentences, 1):
    print(f"\nSentence {i}: {sentence}")
    print("Issues Identified:", identify_issues(sentence))
    print("Cleaned Text:", preprocess(sentence))