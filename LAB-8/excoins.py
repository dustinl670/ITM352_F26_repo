

Amount = round(0.87 * 100) # in cents.
num_quarter = 25
num_dime = 10
num_nickel = 5
num_penny = 1
num_quarters = int(Amount // num_quarter)
Amount -= num_quarters * num_quarter

num_dimes = int(Amount // num_dime)
Amount -= num_dimes * num_dime

num_nickels = int(Amount // num_nickel)
Amount -= num_nickels * num_nickel

num_pennies = int(Amount // num_penny)
Amount -= num_pennies * num_penny

print(f"Quarters: {num_quarters}")
print(f"Dimes: {num_dimes}")
print(f"Nickels: {num_nickels}")
print(f"Pennies: {num_pennies}")

