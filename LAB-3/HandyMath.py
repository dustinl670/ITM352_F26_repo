# This module provides handy mathematical functions.

def midpoint(num1, num2):  # Returns the number halfway between two numbers.
    return (num1 + num2) / 2

def sqrt(num):  # Returns the square root of a number.
    return num ** 0.5

def exp(num1, num2):  # Raises the first number to the power of the second number.
    return num1 ** num2

def max(num1, num2):  # Returns the larger of two numbers.
    return num1 if num1 > num2 else num2

def min(num1, num2):  # Returns the smaller of two numbers.
    return num1 if num1 < num2 else num2

    print("Midpoint of 4 and 8:", midpoint(4, 8))
    print("Square root of 16:", sqrt(16))
    print("2 raised to the power of 3:", exp(2, 3))
    print("Maximum of 5 and 10:", max(5, 10))
    print("Minimum of 5 and 10:", min(5, 10))