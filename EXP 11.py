#Name : Nadir Shaikh
#UIN : 251P086
print("Name: Nadir Shaikh,UIN: 251P086 ")

def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b == 0:
        return "Cannot divide by zero"
    return a/b

print("\nChoose an operation to perform:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Divison")
 
choice = input("Enter 1,2,3 or 4:")

num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

if choice =="1":
    result = add(num1,num2)
    print("Addition result is:",result)

elif choice =="2":
    result = subtract(num1,num2)
    print("Subtraction result is:",result)

elif choice =="3":
    result = multiply(num1,num2)
    print("Multiplication result is:",result)

elif choice =="4":
    result = divide(num1,num2)
    print("Division result is:",result)

else:
    print("Invalid choice")
