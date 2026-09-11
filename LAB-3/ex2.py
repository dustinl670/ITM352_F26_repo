# Create a function—call it midpoint —that takes two numbers as input and returns the value halfway between them.
# Name: Dustin Lopera
# Date: September 11, 2026

print ("Please enter two numbers to find the midpoint between them.")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

def midpoint(num1, num2):
    return (num1 + num2) / 2    

print (midpoint(num1, num2))  # Output: 15.0