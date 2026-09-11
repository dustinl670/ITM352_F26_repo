def say_hello():
    print("Hello, world!")

def greet(name):
    print(f"Hello, {name}!")

greet("Dustin")

def introduce(name, hometown, age):
    print(f"My name is {name}, I am {age} years old, and I am from {hometown}.")

introduce("Dustin", "Saipan", 21)

def greet_user(name="friend"):
    print(f"Hello, {name}!")

greet_user("Dustin")
greet_user()  # This will use the default value "friend"

def add(first_number, second_number):
    return first_number + second_number

result = add(5, 3)
print(result)  # Output: 8

def calculate_total(price, tax_rate=0.04):
    return price + (price * tax_rate)

print(calculate_total(100))  # Uses default tax rate of 0.04
print(calculate_total(100, 0.08))  # Uses specified tax rate of 0.08