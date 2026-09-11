# This program prompts the user to enter a string and then calculates and displays the length of that string.
# Name: Dustin Lopera
# Date: September 4, 2026

user_string = input("Please enter a password: ")

while len(user_string) > 8:
	print("Your password cannot be more than 8 characters.")
	user_string = input("Please enter a password: ")

string_length = len(user_string)

print("You entered:", user_string)
print("The length of the string is:", string_length)
