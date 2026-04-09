'''
28th Feb

Assignment Name : Storytelling with Graphs
Description : Create bar chart, pie chart, histogram and write a short data story explaining trends..
'''
import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset
data = {
    "Student": ["A", "B", "C", "D", "E"],
    "Marks": [85, 90, 78, 92, 88]
}

df = pd.DataFrame(data)

# Bar Chart
plt.bar(df["Student"], df["Marks"])
plt.title("Student Marks - Bar Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# Pie Chart
plt.pie(df["Marks"], labels=df["Student"], autopct='%1.1f%%')
plt.title("Marks Distribution - Pie Chart")
plt.show()

# Histogram
plt.hist(df["Marks"], bins=5)
plt.title("Marks Distribution - Histogram")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()



''' 
Data Story

The graphs show the distribution of marks among five students. The bar chart clearly compares individual student performance, 
where student D has the highest marks while student C has the lowest. The pie chart illustrates the proportion of marks contributed by each student, 
showing that the differences are relatively small but still noticeable. The histogram displays how the marks are distributed within the range, 
indicating that most students scored between 80 and 95. Overall, the data suggests that the class performance is strong with most students achieving high marks.
'''
