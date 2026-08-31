# 2D array: 5 students, 3 subjects
marks = [
    [50, 85, 80],   # Student 0
    [60, 95, 35],   # Student 1
    [70, 90, 85],   # Student 2
    [85, 55, 65],   # Student 3
    [45, 95, 35]    # Student 4
]

# 1. Find maximum marks

print("1. Maximum marks:")
maximum = max(max(row) for row in marks)
print("Maximum marks:", maximum)

# 2. Find minimum marks
print("2. Minimum marks:")
minimum = min(min(row) for row in marks)
print("Minimum marks:", minimum)

# 3. Find average marks
print("3. Average marks:")
total = sum(sum(row) for row in marks)
average = total / (5 * 3)
print("Average marks:", average)

# 4. Find student ID who scored maximum marks in subject 1
# Subject 1 means index 1 (second subject)

print("4. Student ID who scored maximum marks in subject 1:")
max_marks_sub1 = marks[0][1]
student_id = 0

for i in range(1, 5):
    if marks[i][1] > max_marks_sub1:
        max_marks_sub1 = marks[i][1]
        student_id = i

print("Maximum marks in Subject 1:", max_marks_sub1)
print("Student ID:", student_id)

# 5. find maximum marks subject wise
print("5. Maximum marks subject wise:")
for j in range(3):
    subject_max = marks[0][j]
    for i in range(1,5):
        if marks[i][j]>subject_max:
            subject_max=marks[i][j]
    print("Subject", j, ":", subject_max)

# 6. find average marks subject wise
print("6. Average marks subject wise:")
for j in range(3):
    subject_total=0
    for i in range(5):
        subject_total=subject_total+marks[i][j]
        subject_average=subject_total/5
    print("subject",j,":",subject_average)

# 7. add 10 marks for all students who scored less than 50 in subject(1)
print("7. Add 10 marks for all students who scored less than 50 in subject(1):")
count=0
for i in range(5):
    if marks[i][1]<50:
        marks[i][1]=marks[i][1]+10
    print("student",i,"marks in subject 1:",marks[i][1])
print("number of students who scored less than 50 in subject(1):",count)
# 8. find out number of students score more than 80 in subject(2)

print("8. Number of students who scored more than 80 in subject(2):")
count=0
for i in range(5):
    if marks[i][2]>80:
        count=count+1
print("number of students more than 80 in subject 2:",count)

# 9.find out the minimum marks of student(2)
print("9. Minimum marks of student(2):")
student_2_min=min(marks[2])
print("minimum marks of student(2):",student_2_min) 

# 10.find out the maximum marks of student(4)

print("10. Maximum marks of student(4):")
student_4_max=max(marks[4])
print("maximum marks of student(4):",student_4_max)