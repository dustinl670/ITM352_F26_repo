# Ask the user to enter their birth year, and calculate their age based on the current year (2026). Then display a message with their age.
# Name: Dustin Lopera
# Date: September 2, 2026

birth_year = input("Enter your birth year: ")
current_year = 2026
age = current_year - int(birth_year)

print("You entered " + birth_year + ".")
print("Your age is: " + str(age) + ".")
