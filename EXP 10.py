#Nadir Shaikh
#UIN - 251P086
print("Nadir Shaikh")
print("UIN - 251P086")

def is_prime(n): 
 if n <= 1: 
  return False 
 for i in range(2, n): 
  if n % i == 0: 
   return False 
  return True 
number = int(input("Enter a number to check if it's prime: ")) 
if is_prime(number): 
 print(f"{number} is a prime number.") 
else: 
 print(f"{number} is not a prime number.")


