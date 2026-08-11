marks = [65, 78, 82, 55, 90, 72, 68, 85, 95, 60,
         75, 88, 92, 70, 64, 80, 58, 87, 73, 69]

# 1. Find average
average = sum(marks) / len(marks)
print("Average marks =", average)

# 2. Count students scoring more than average
count = 0

for i in marks:
    if i > average:
        count = count + 1

print("Students scoring more than average =", count)

# 3. Find maximum score
maximum = max(marks)

print("Maximum score =", maximum)
print("Student index/position:")

for i in range(len(marks)):
    if marks[i] == maximum:
        print(i)