# This program prompts the user to enter a value between 1 and 100, then calculates and displays the square of that value.
# Name: Dustin Lopera
# Date: September 2, 2026

value_entered = input("Please enter a value between 1 and 100: ")
value_as_integer = int(value_entered)

ValueSquared = value_as_integer ** 2

print("You entered:", value_as_integer)
print(f"The square of {value_as_integer} is {ValueSquared}.")

print(f"You entered: {value_as_integer}, and the square of that value is {ValueSquared}.")
