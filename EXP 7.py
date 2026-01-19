#Nadir Shaikh
#UIN - 251P086
print("Nadir Shaikh")
print("UIN - 251P086")
students = { 
101: {"name": "John", "grade": "A", "attendance": 90},102: {"name": "Alice", "grade": "B", "attendance": 85},  
103: {"name": "Bob", "grade": "A", "attendance": 95} }
students[104] = {"name": "Charlie", "grade": "B", "attendance": 80} 
print(students)
students[101]["grade"] = "A+"
print(students)
for student_id, details in students.items(): 
 print(f"ID: {student_id}, Name: {details['name']}, Grade: {details['grade']}, Attendance: {details['attendance']}%")
print(students.keys())
print(students.values())
print(students.items())

