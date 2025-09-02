# Student Classification System
# Get student information
student_name = input("Enter student name: ")
gpa = float(input("Enter GPA (0.0-4.0): "))
credit_hours = int(input("Enter credit hours: "))

# TODO your code here
if gpa >= 3.8 and credit_hours >=12:
    dean_list = True
if gpa >= 3.5 and credit_hours >= 12:
    honor_role = True
if gpa >= 2.0:
    good_standing = True
if gpa <= 2.0:
    probation = True

classification = (dean_list==True) and (honor_role==True) and (good_standing==True) and (probation==True)

# Display results
print(f"\nStudent: {student_name}")
print(f"GPA: {gpa}")
print(f"Credit Hours: {credit_hours}")
print(f"Classification: {classification}")