# Dictionary of 5 students
student = {
    101: {"name": "Rahul", "department": "CSE", "marks": 85},
    102: {"name": "Asif", "department": "CSE", "marks": 92},
    103: {"name": "Wasif", "department": "IT", "marks": 78},
    104: {"name": "Arindam", "department": "ECE", "marks": 88},
    105: {"name": "Mominul", "department": "CSE", "marks": 95}
}

# 1. Sort dictionary according to marks (High to Low)
sorted_student = dict(
    sorted(student.items(), key=lambda x: x[1]["marks"], reverse=True)
)

print("1. Students sorted by marks (High to Low):")
for roll, details in sorted_student.items():
    print(roll, details)


# 2. Print the record of student with highest marks
highest_student = max(student.items(), key=lambda x: x[1]["marks"])

print("\n2. Student with highest marks:")
print("Roll No:", highest_student[0])
print("Details:", highest_student[1])


# 3. Find average marks
average_marks = sum(
    map(lambda x: x["marks"], student.values())
) / len(student)

print("\n3. Average Marks:", average_marks)


# 4. Print students who scored more than average marks
above_average = dict(
    filter(lambda x: x[1]["marks"] > average_marks, student.items())
)

print("\n4. Students scoring more than average marks:")
for roll, details in above_average.items():
    print(roll, details)