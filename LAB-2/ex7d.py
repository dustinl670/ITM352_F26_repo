# This program prompts the user to enter a temperature in Fahrenheit and then converts it to Celsius.
# Create the conversion as a function.
# Name: Dustin Lopera
# Date: September 4, 2026

def f_to_c(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    rounded_celsius = round(celsius, 2)
    return rounded_celsius

fahrenheight_input = input("Please enter a temperature in Fahrenheit: ")
fahrenheight_float = float(fahrenheight_input)

celsius_value = f_to_c(fahrenheight_float)

print("You entered:", fahrenheight_float)
print("The temperature in Celsius is:", celsius_value)