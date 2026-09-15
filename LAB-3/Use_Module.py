import HandyMath
from HandyMath import max, min

# Get two numbers from the user for the HandyMath calculations.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Display results calculated for functions from the HandyMath module.
print("Midpoint of", num1, "and", num2, "is:", HandyMath.midpoint(num1, num2))
print("Square root of", num1, "is:", HandyMath.sqrt(num1))
print(num1, "raised to the power of", num2, "is:", HandyMath.exp(num1, num2))
print("Maximum of", num1, "and", num2, "is:", max(num1, num2))
print("Minimum of", num1, "and", num2, "is:", min(num1, num2))