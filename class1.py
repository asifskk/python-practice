class Student:
    # Constructor
    def __init__(self, name, department, roll):
        self.name = name
        self.department = department
        self.roll = roll

    # Display student record
    def show(self):
        print("Name:", self.name)
        print("Department:", self.department)
        print("Roll No:", self.roll)

# Create 5 student objects
s1 = Student("Rahul", "CSE", 101)
s2 = Student("Asif", "ECE", 102)
s3 = Student("Wasif", "CSE", 103)
s4 = Student("Arindam", "IT", 104)
s5 = Student("Mominul", "ME", 105)