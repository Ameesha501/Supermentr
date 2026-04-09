import pandas as pd

# Read CSV file
df = pd.read_csv("D:/Supermentr/Tasks/14th_FEB/students.csv")

# Handle missing values (fill with 0)
df.fillna(0, inplace=True)

# Add Total column
df["total"] = df["maths"] + df["science"] + df["english"]

# Add Average column
df["average"] = df["total"] / 3

# Top 3 students based on total
top3 = df.sort_values(by="total", ascending=False).head(3)
print("Top 3 Students:\n", top3)

# Department-wise average marks
dept_avg = df.groupby("dept")[["maths", "science", "english"]].mean()
print("\nDepartment-wise Average:\n", dept_avg)

# Students scoring above 75 in all subjects
above_75 = df[
    (df["maths"] > 75) &
    (df["science"] > 75) &
    (df["english"] > 75)
]
print("\nStudents scoring above 75 in all subjects:\n", above_75)