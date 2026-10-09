# Determine a movie price. The rules are:
# The normal price is $14
# If someone is 65 or older, they pay $8.
# If it is Tuesday, the price is $10.
# If it is a matinee, the price is $5 for seniors and $8 otherwise
# Name: Dustin Lopera
# Date: September 25, 2026

age = 102
day = "tuesday"
matinee = True

price = 14

if day == "tuesday":
    price = 10
if age >= 65:
    price = 8
if matinee:
    if age >= 65:
        price = 5
    else:
        price = 8

print("Day:", day)
print("Matinee:", matinee)

if age >= 65:
    print("Senior discount applied.")
else:
    print("No senior discount applied.")

print("Ticket price is $", format(price, "0.2f"))