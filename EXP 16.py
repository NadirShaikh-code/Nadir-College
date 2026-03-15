# Name: Nadir Shaikh
# UIN : 251P086
print("Name:Nadir Shaikh,UIN: Nadir Shaikh")

import re

email = input("Enter Email ID: ")
mobile = input("Enter Mobile Number: ")

email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
mobile_pattern = r'^[6-9]\d{9}$'

if re.fullmatch(email_pattern,email):
    print("Valid Email ID")

else:
    print("Invalid Email ID")

if re.fullmatch(mobile_pattern,mobile):
    print("Valid Mobile Number")

else:
    print("Invalid Mobile Number")

    