# Working on conditional statements, or how Python makes decisions based on conditions.

# Age example.
print("What is your age? ")
age = int(input())
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# if condition: # runs if condition is true.
# elif another_condition: # runs if the previous condition is false and this condition is true.
# else: # runs if all previous conditions are false.

# Example with if, elif, and else.

score = 85
if score >= 90:
    print("You got an A.")
elif score >= 80:
    print("You got a B.")
elif score >= 70:
    print("You got a C.")
elif score >= 60:
    print("You got a D.")
else:
    print("You got an F.")

# Choice input elif.

choice = input("Enter your choice (1 for cheeseburger, 2 for hamburger, 3 for fries): ")
if choice == "1":
    print("You chose cheeseburger.")
elif choice == "2":
    print("You chose hamburger.")
elif choice == "3":
    print("You chose fries.")
else:
    print("Invalid choice.")

# Nested if statements are if statements inside other if statements. They are used when there's a domino effect of decisions.
age = int(input("Enter your age: "))
id = input("Do you have an ID? (yes/no): ")
if age >= 18:
    print("You're clubbing age.")
    if id == "yes":
        print("You can now enter the club.")
    else:
        print("You cannot enter the club without an ID.")
else:
    print("You are not old enough to enter the club.")

# End of nested if example.

# Conditionals are used with containers to check whether something exists, is empty, or matches expected data.

items = ["milk", "bread", "eggs"]

if "milk" in items:
    print("Milk is in the list.")
else:
    print("Milk is not in the list.")

if items:
    print("The list is not empty.")
else:
    print("The list is empty.")

name = input("Enter your name: ")
if "D" in name:
    print("Your name contains the letter D.")
if name.startswith("E"):
    print("Your name starts with the letter E.")
if name.isalpha():
    print("Your name contains only letters.")
else:
    print("Your name contains non-letter characters.")

# Using dictionaries:

student = {
    "name": "Dustin",
    "age": 23,
    "major": "Management Information Systems"
}

if "name" in student:
    print("The key 'name' exists in the student dictionary.")
if student.get("age") >= 18:
    print("The student is an adult.")
if student:
    print("The student dictionary is not empty.")
else:
    print("The student dictionary is empty.")

# Data validation example.

user_input = input("Enter a username: ")

if user_input and user_input.isalpha():
    print("Valid username.")
else:
    print("Invalid username. Only letters are allowed.")

# Combining conditions.

cart = ["milk", "bread"]

if "milk" in cart and len(cart) >= 2:
    print("You have at least 2 items including milk.")