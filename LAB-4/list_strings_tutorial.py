fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print("Starting list:", fruits)

fruits.append("grape")
print("After appending 'grape':", fruits)

fruits.insert(2, "kiwi")
print("After inserting 'kiwi' at index 2:", fruits)

fruits.remove("banana")
print("After removing 'banana':", fruits)

removed_fruit = fruits.pop(3)
print("Removed: ", removed_fruit)
print("After pop", fruits)

numbers = [5, 2, 4, 3, 1]
numbers.sort()
print("After sorting:", numbers)

numbers.reverse()
print("Reversed Numbers:", numbers)

print("Number of fruits:", len(fruits))

# Practice with scores

scores = [88, 92, 79, 95, 85]

scores.append(88)
scores.insert(0, 90)
scores.remove(79)
last_score = scores.pop()
scores.sort()

print("Scores:", scores)
print ("Removed score:", last_score)
print("Number of scores:", len(scores))

numberslice = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(numberslice[0])  # Output: 1
print(numberslice[5])  # Output: 6

# Negative Indexing, working backwards from the end of the list.
print(numberslice[-1])  # Output: 20
print(numberslice[-5])  # Output: 16

# Slicing, getting a portion of the list.
print(numberslice[0:5])  # Output: [1, 2, 3, 4, 5]

# Beginning from index.
print(numberslice[:5])  # Output: [1, 2, 3, 4, 5]

# Ending from index.
print(numberslice[5:])  # Output: [6, 7, 8, 9, 10...]

# Copy the entire list.
print(numberslice[:])  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Slicing with steps.
print(numberslice[::2])  # Output: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(numberslice[1::2])  # Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Reversing a list using slicing.
print(numberslice[::-1])  # Output: [20, 19, 18, 17, 16, 15, 14, 13, 12, 11...]

# Negative Slicing
print(numberslice[-5:-1])  # Output: [16, 17, 18, 19]

# ***String fundamentals.
first_name = "Dustin"
message = 'Welcome to Python'

# Concatenation
full_name = first_name + " " + "Lopera"
print(full_name)

# Repetition.
print("Ha" * 3)  # Output: HaHaHa

# upper(): converts all characters in a string to uppercase.
print(first_name.upper())  # Output: DUSTIN

# lower(): converts all characters in a string to lowercase.
print(first_name.lower())  # Output: dustin

# strip(): removes any leading and trailing whitespace from a string.
greeting = "   Hello, world!   "
print(greeting.strip())  # Output: Hello, world!

# split(): splits a string into a list where each word is a list item.
sentence = "Python is fun"
words = sentence.split()
print(words)  # Output: ['Python', 'is', 'fun']

# split() with a separator.
date = "2026-09-16"
date_parts = date.split("-")
print(date_parts)  # Output: ['2026', '09', '16']

# f-strings: insert values into strings.
age = 21
print(f"My name is {first_name} and I am {age} years old.")

# formatting (utilizing age and name variables from above)
gpa = 3.75

# Formatting using %
old_style = "My name is %s and I am %d years old with a GPA of %.2f." % (first_name, age, gpa)
print(old_style)

# .format() method
format_method = "My name is {} and I am {} years old with a GPA of {:.2f}.".format(first_name, age, gpa)
print(format_method)

# f-string method
f_string = f"My name is {first_name} and I am {age} years old with a GPA of {gpa:.2f}."
print(f_string)

# Formatting calculations with an f-string
price = 19.99
quantity = 3
print(f"The total cost for {quantity} items at ${price:.2f} each is ${price * quantity:.2f}.")

# ***Advanced String Operations.
text = "Python programming is fun!"

# Finding substrings
print(text.find("programming")) # Starting index
print("Python" in text) # True
print("Java" not in text) # True

# Replacing Text
new_text = text.replace("fun", "powerful")
print(new_text)

# Checking String properties
number_text = "2026"
word_text = "Python"
mixed_text = "Python2026"

print(number_text.isdigit()) # True
print(word_text.isalpha()) # True
print(mixed_text.isalnum()) # True

# String Slicing
print(text[0:6]) # Python
print(text[:6]) # Python
print(text[7:18]) # programming
print(text[-3:]) # un!
print(text[::-1]) # reverses the string

# Additional Checks
print(text.startswith("Python"))  # True
print(text.endswith("fun"))       # False "fun!"
print(text.lower().count("i"))    # Number of lowercase i characters

# Lists and strings working together

# Convert a string into a list of words
sentence = "Python lists and strings"
words = sentence.split()
print(words)  # ['Python', 'lists', 'and', 'strings']

# Convert a string into a list of characters
letters = list("Python")
print(letters)  # ['P', 'y', 't', 'h', 'o', 'n']

# Join a list of strings into one string
joined_sentence = " ".join(words)
print(joined_sentence)

# Join with a different separator
csv_data = ",".join(words)
print(csv_data)

# Work with a list of strings
names = ["alice", "bob", "charlie"]

# Modify each string
capitalized_names = [name.title() for name in names]
print(capitalized_names)

# Filter strings by length
long_names = [name for name in names if len(name) > 3]
print(long_names)

# Build a sentence from list items
greeting = "Hello, " + ", ".join(capitalized_names) + "!"
print(greeting)

# Tuples: Ordered collections, similar to lists, but they are immutable/cannot be changed after creation.
# Tuples use parentheses.
coordinates = (21.3, -157.8)
print(coordinates)

# Accesing tuple elements.
print (coordinates[0])
print(coordinates[-1]) # Cannot be edited, coordinates[0] = 22 -> # TypeError

# Mutability of lists.
colors = ["red", "blue"]
colors.append("green")
print(colors)

# Tuple unpacking
student = ("Dustin", 21, 3.75)
name, age, gpa = student
print(name)
print(age)
print(gpa)

# Tuples can be used for fixed data.
rgb_red = (255, 0, 0)
print(rgb_red)

# Tuples can be dictionary keys while lists cannot.
locations = {
(21.3, -157.8): "Honolulu",
(40.7, -74.0): "New York"
}

print(locations[(21.3, -157.8)])

# Useful tuple operations
numberstwo = (4, 2, 4, 7 ,4)
print(len(numbers))
print(numbers.count(4))
print(numbers.index(3))
