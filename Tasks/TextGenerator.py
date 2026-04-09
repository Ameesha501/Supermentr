import random

# Sample training text
text = """
machine learning is fun and powerful
learning models can generate smart predictions
text generation using simple logic is interesting
artificial intelligence is the future of technology
"""

# Convert text into words
words = text.lower().split()

# Build bigram model
model = {}
for i in range(len(words) - 1):
    word = words[i]
    next_word = words[i + 1]
    
    if word not in model:
        model[word] = []
    
    model[word].append(next_word)

# -------- USER INPUT --------
user_input = input("Enter a starting sentence: ").strip().lower()

# If user enters nothing
if user_input == "":
    print("Please enter some text!")
else:
    input_words = user_input.split()
    current_word = input_words[-1]

    # Generate sentence up to 10 words
    generated = input_words.copy()

    while len(generated) < 10:
        if current_word in model:
            next_word = random.choice(model[current_word])
        else:
            next_word = random.choice(words)
        
        generated.append(next_word)
        current_word = next_word

    print("\nGenerated Sentence:")
    print(" ".join(generated[:10]))