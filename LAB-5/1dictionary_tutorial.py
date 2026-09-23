# Tutorial on how to create and navigate dictionaries in Python.
# Name: Dustin Lopera
# Date: September 23, 2026

student = {
    "name": "Dustin",
    "age": 23,
    "major": "Management Information Systems"
}

# Adding items
student["year"] = 2026
print(student)

# Updating values.
student["age"] = 21
print(student["age"])

# Removing items.
# removed = student.pop("major")
# print(removed) # Shows what was removed.
# print(student) # Updated dictionary.

# Checking if keys exist in the dictionary.
print("name" in student) # True
print("major" in student) # False

# Getting all of the keys and values.
print(student.keys()) # Name, age, year.
print(student.values()) # Associated values ^^^
print(student.items()) # Keys and their associated values.

# Retrieving a value safely.
print(student.get("name")) # Dustin.
print(student.get("minor", "Not found"))

# Looping:
# Looping through keys.

for key in student:
    print(key)

# Looping through values only.

for value in student.values():
    print(value)

# Looping through key-value pairs.
for key, value in student.items():
    print(key, value)

# Looping through keys and access values using the key.
for key in student:
    print(key, "->", student[key]) # Using ->
    print(f"{key}: {value}") # Using :

print("Separation marker for nested dictionaries.")

# Dictionary of countries with their nested dictionaries.

countries = {
    "USA": {
        "capital": "Washington, D.C.",
        "population": 331000000
    },
    "Canada": {
        "capital": "Ottawa",
        "population": 40000000
    }
}

print(countries["USA"]["capital"])
print(countries["Canada"]["population"])

# Acessing nested values through chaining keys.

country = countries["USA"]
print(country["capital"])

# Adding new nested entries.

countries["France"] = {
    "capital": "Paris",
    "population": 68000000
}

print(countries["France"]["capital"])

# Updating nested values.

countries["Canada"]["population"] = 41000000
print(countries["Canada"]["population"])

# Looping through nested dictionaries.

for country, info in countries.items():
    print(country, "->", info["capital"], info["population"])

# Nested dictionaries use lists, as well.

students = {
    "Dustin": {
        "classes": ["ITM352", "BUS 310", "BUS 311", "BUS 312", "BUS 313"],
        "gpa": 3.5
    }
}

print(students["Dustin"]["classes"])
print(students["Dustin"]["classes"][0])

# Also, there are lists with dictionaries.

people = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 22}
]

print(people[0]["name"])

print("This is a separation marker for practical real-world uses of dictionaries.")

# Counting items.

sentence = "apple banana apple orange banana apple"
words = sentence.split()

word_counts = {}

for word in words: # Identifies word frequencies, vote tallies, and inventory counts.
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(word_counts) 

# Grouping data.

studentm = [
    {"name": "Alice", "major": "CS"},
    {"name": "Bob", "major": "CS"},
    {"name": "Charlie", "major": "MIS"},
    {"name": "Diana", "major": "CS"}
]

major_groups = {}

for student in studentm: # Can organize customer bases, employees by department, transactions by category.
    major = student["major"]
    if major not in major_groups:
        major_groups[major] = []
    major_groups[major].append(student["name"])

print(major_groups)

# Configuration settings.

config = { # Good for user preferences, database settings, and app bhvr options.
    "debug": True,
    "max_connections": 100,
    "timeout": 30,
    "theme": "dark"
}

print(config["theme"]) # dark
print(config.get("timeout")) # 30

# Data lookup:

products = { # Good for looking up student records by ID and record retrieval from databases.
    "A101": {"name": "Keyboard", "price": 45.99},
    "B202": {"name": "Mouse", "price": 22.50},
    "C303": {"name": "Monitor", "price": 199.99}
}

product_id = "B202"
print(products[product_id]["name"])  # Mouse
print(products[product_id]["price"])  # 22.5