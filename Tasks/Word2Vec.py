from gensim.models import Word2Vec

# Small dataset (college topic)
data = [
    ["college","life","is","fun"],
    ["students","study","in","college"],
    ["friends","make","life","happy"],
    ["college","has","events","and","festivals"],
    ["students","write","exams"],
    ["teachers","help","students"],
    ["library","is","quiet"],
    ["sports","are","important"],
    ["canteen","food","is","tasty"],
    ["students","do","projects"],
    ["group","study","helps"],
    ["hostel","life","is","independent"],
    ["students","learn","new","skills"],
    ["college","campus","is","big"],
    ["time","management","is","important"]
]

# Train model
model = Word2Vec(data, vector_size=20, window=2, min_count=1)

# Vector of a word
print("Vector for 'college':")
print(model.wv["college"])

# Similar words
print("\nSimilar words to 'college':")
print(model.wv.most_similar("college", topn=5))