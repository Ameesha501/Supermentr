''' 
10th March

Spam Classifier Thinking

The goal of this assignment is to design a spam detection system that can automatically classify messages or emails as spam or not spam. The system analyzes features such as keywords, message length, links, sender information, and promotional content. It requires a dataset containing both spam and normal messages so that the model can learn patterns and make predictions. However, errors can occur, such as important messages being marked as spam (false positives) or spam messages appearing in the inbox (false negatives). Hence, choosing the right features and using quality data is important to improve the accuracy of the spam classifier.
'''
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Step 1: Create a sample mall dataset
data = {
    "Annual_Income": [15, 16, 17, 18, 60, 62, 65, 68, 120, 125, 130, 135],
    "Spending_Score": [39, 81, 6, 77, 40, 42, 43, 41, 90, 92, 95, 94]
}

df = pd.DataFrame(data)

# Step 2: Select features for clustering
X = df[["Annual_Income", "Spending_Score"]]

# Step 3: Apply K-Means
kmeans = KMeans(n_clusters=3, random_state=0)
df["Cluster"] = kmeans.fit_predict(X)

# Step 4: Plot the clusters
plt.scatter(df["Annual_Income"], df["Spending_Score"], c=df["Cluster"])
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation using K-Means")
plt.show()

# Step 5: View grouped customers
print(df)

