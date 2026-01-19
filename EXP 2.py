print("Nadir Shaikh")
print("251P086")



print("Choose a geometric figure to calculate its area:")
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")

choice = input("Enter 1, 2, or 3: ")

if choice == "1":
    # circle area = π * r^2
    radius = float(input("Enter the radius of the circle: "))
    pi = 3.14159
    area = pi * radius * radius
    print("The area of the circle is:", area)

elif choice == "2":
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print("The area of the rectangle is:", area)

elif choice == "3":
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print("The area of the triangle is:", area)

else:
    print("Invalid choice! Please enter 1, 2, or 3.")

