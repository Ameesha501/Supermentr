import PyPDF2
from collections import Counter

file_path = input("Enter PDF file path: ")

with open(file_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

print(text)

words = text.split()
print("Total Words:", len(words))
print("Total Characters:", len(text))

print("Top 5 Words:", Counter(words).most_common(5))