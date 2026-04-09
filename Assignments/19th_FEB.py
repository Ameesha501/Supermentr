'''19th Feb

Assignment Name : Student Data Manager
Description : Store data for 5 students using dictionaries, print topper, class average, and assign grades.
'''

# Store data of 5 students using dictionary
students = {
    "Ram": 85,
    "Ayra": 92,
    "Aksha": 78,
    "Nehal": 88,
    "Riyan": 95
}

# Find topper
topper = max(students, key=students.get)
print("Topper:", topper, "-", students[topper])

# Calculate class average
average = sum(students.values()) / len(students)
print("Class Average:", average)

# Assign grades
print("\nStudent Grades:")
for name, marks in students.items():
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "F"

    print(name, ":", marks, "- Grade", grade)
    