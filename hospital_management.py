# Hospital Management System

# 1. Patient Registration using Dictionary

patients = {}

patient_id = input("Enter Patient ID: ")
name = input("Enter Patient Name: ")
age = int(input("Enter Age: "))
phone = input("Enter Phone Number: ")

patients[patient_id] = {
    "Name": name,
    "Age": age,
    "Phone": phone
}

print("\nPatient Registered Successfully!")


# 2. Appointment Scheduling using List

appointments = []

doctor_name = input("Enter Doctor Name: ")
date = input("Enter Appointment Date: ")
time = input("Enter Appointment Time: ")

appointments.append([patient_id, name, doctor_name, date, time])

print("Appointment Scheduled Successfully!")


# 3. Medical Records using File Handling

disease = input("Enter Disease: ")
medicine = input("Enter Medicine: ")

with open("medical_records.txt", "a") as file:
    file.write("Patient ID: " + patient_id + "\n")
    file.write("Patient Name: " + name + "\n")
    file.write("Disease: " + disease + "\n")
    file.write("Medicine: " + medicine + "\n")

print("Medical Record Saved Successfully!")


# 4. Doctor Information using Tuple

doctor = ("Dr. Rahul", "Cardiologist", "9876543210")

print("\nDoctor Name:", doctor[0])
print("Specialization:", doctor[1])
print("Phone:", doctor[2])


# 5. Billing System using Class and Object

class Billing:

    def __init__(self, name, consultation, medicine, room):
        self.name = name
        self.consultation = consultation
        self.medicine = medicine
        self.room = room

    def total_bill(self):
        return self.consultation + self.medicine + self.room

    def display_bill(self):
        print("\nPatient Name:", self.name)
        print("Consultation Fee:", self.consultation)
        print("Medicine Cost:", self.medicine)
        print("Room Charge:", self.room)
        print("Total Bill:", self.total_bill())


bill = Billing(name, 500, 1000, 1500)

bill.display_bill()


# 6. Report Generation using File Handling

with open("hospital_report.txt", "w") as file:

    file.write("HOSPITAL REPORT\n")
    file.write("Patient ID: " + patient_id + "\n")
    file.write("Patient Name: " + name + "\n")
    file.write("Age: " + str(age) + "\n")
    file.write("Doctor: " + doctor_name + "\n")
    file.write("Disease: " + disease + "\n")
    file.write("Medicine: " + medicine + "\n")
    file.write("Total Bill: " + str(bill.total_bill()) + "\n")

print("\nHospital Report Generated Successfully!")