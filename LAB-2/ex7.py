# This program prompts the user to enter a temperature in Fahrenheit and then converts it to Celsius.
# Name: Dustin Lopera
# Date: September 4, 2026

fahrenheight_input = input("Please enter a temperature in Fahrenheit: ")
fahrenheight_float = float(fahrenheight_input)

celsius_value = (fahrenheight_float - 32) * 5/9

celsius_value = round(celsius_value, 2)

print("You entered:", fahrenheight_float)
print("The temperature in Celsius is:", celsius_value)