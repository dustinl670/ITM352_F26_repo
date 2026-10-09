
print("Starting loops tutorial...")
# Count from 0 up to, but not including, 5
for number in range(5):
    print(number)  # 0, 1, 2, 3, 4

# Start at 1 and stop before 6
for number in range(1, 6):
    print(number)  # 1, 2, 3, 4, 5

# Count by 2s
for number in range(0, 11, 2):
    print(number)  # 0, 2, 4, 6, 8, 10

# Count backward by 1
for number in range(5, 0, -1):
    print(number)  # 5, 4, 3, 2, 1

# Create a list of numbers from 1 to 5
numbers = list(range(1, 6))
print(numbers)  # [1, 2, 3, 4, 5]

print("Starting ranging loops tutorial...")
# ...existing code...

# Ranging loops.

# 1. Looping through a list directly
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  # apple, banana, cherry (one per line)

# 2. Looping through a list with index using enumerate()
for index, fruit in enumerate(fruits):
    print(index, fruit)  # 0 apple / 1 banana / 2 cherry

# 3. Looping through a list using range() and index access
for i in range(len(fruits)):
    print(i, fruits[i])  # 0 apple / 1 banana / 2 cherry

# 4. Looping through a string (character by character)
word = "hello"
for letter in word:
    print(letter)  # h, e, l, l, o (one per line)

# 5. Looping through a string with index
for index, letter in enumerate(word):
    print(index, letter)  # 0 h / 1 e / 2 l / 3 l / 4 o

# 6. Looping through dictionary keys
student = {"name": "Dustin", "age": 23, "major": "MIS"}
for key in student:
    print(key)  # name, age, major (one per line)

# 7. Looping through dictionary values
for value in student.values():
    print(value)  # Dustin, 23, MIS (one per line)

# 8. Looping through dictionary key-value pairs
for key, value in student.items():
    print(key, "->", value)  # name -> Dustin / age -> 23 / major -> MIS

print("Starting break and continue tutorial...")
# ...existing code...

# Break and continue.

# 1. break: stop the loop early when a condition is met
for number in range(10):
    if number == 5:
        break
    print(number)  # 0, 1, 2, 3, 4

# 2. continue: skip an iteration, but keep looping
for number in range(10):
    if number % 2 == 0:
        continue
    print(number)  # 1, 3, 5, 7, 9 (odd numbers only)

# 3. break: search for an item and stop once found
fruits = ["apple", "banana", "cherry"]
target = "banana"
for fruit in fruits:
    if fruit == target:
        print(f"Found {target}!")
        break
else:
    print(f"{target} not found.")

# 4. continue: skip invalid data while processing a list
scores = [85, -1, 92, -1, 78]
for score in scores:
    if score < 0:
        continue
    print("Valid score:", score)  # 85, 92, 78

# 5. break inside a while loop (user input validation)
while True:
    command = input("Type 'exit' to stop: ")
    if command == "exit":
        break
    print("You typed:", command)

# 6. continue inside a while loop
count = 0
while count < 10:
    count += 1
    if count % 3 == 0:
        continue
    print(count)  # 1, 2, 4, 5, 7, 8, 10 (skips multiples of 3)

print("Starting nested loops tutorial...")
# ...existing code...

# Nested loops.

# 1. Basic nested loop
for outer in range(3):
    for inner in range(2):
        print(outer, inner)
        # 0 0
        # 0 1
        # 1 0
        # 1 1
        # 2 0
        # 2 1

# 2. Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
        # 1 x 1 = 1
        # 1 x 2 = 2
        # 1 x 3 = 3
        # 2 x 1 = 2
        # 2 x 2 = 4
        # 2 x 3 = 6
        # 3 x 1 = 3
        # 3 x 2 = 6
        # 3 x 3 = 9

# 3. Printing a grid/pattern
for row in range(3):
    for col in range(5):
        print("*", end="")
    print()  # move to next line
# ***** (row 0)
# ***** (row 1)
# ***** (row 2)

# 4. Nested loop over two lists (all pair combinations)
colors = ["red", "green"]
sizes = ["S", "M", "L"]
for color in colors:
    for size in sizes:
        print(f"{color} - {size}")
        # red - S
        # red - M
        # red - L
        # green - S
        # green - M
        # green - L

# 5. Nested loop over a list of lists (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for value in row:
        print(value, end=" ")
    print()
# 1 2 3
# 4 5 6
# 7 8 9

# 6. Using break in a nested loop (only breaks the inner loop)
for i in range(3):
    for j in range(3):
        if j == 1:
            break
        print(i, j)
        # 0 0
        # 1 0
        # 2 0

print("Starting list comprehensions tutorial...")
# ...existing code...

# List comprehensions.

# 1. Regular for loop
squares = []
for number in range(5):
    squares.append(number ** 2)
print(squares)  # [0, 1, 4, 9, 16]

# Equivalent list comprehension
squares = [number ** 2 for number in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# 2. For loop with a condition
evens = []
for number in range(10):
    if number % 2 == 0:
        evens.append(number)
print(evens)  # [0, 2, 4, 6, 8]

# Equivalent list comprehension
evens = [number for number in range(10) if number % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]

# 3. For loop that transforms strings
fruits = ["apple", "banana", "cherry"]
upper_fruits = []
for fruit in fruits:
    upper_fruits.append(fruit.upper())
print(upper_fruits)  # ['APPLE', 'BANANA', 'CHERRY']

# Equivalent list comprehension
upper_fruits = [fruit.upper() for fruit in fruits]
print(upper_fruits)  # ['APPLE', 'BANANA', 'CHERRY']

# 4. For loop with if-else (conditional expression)
labels = []
for number in range(5):
    if number % 2 == 0:
        labels.append("even")
    else:
        labels.append("odd")
print(labels)  # ['even', 'odd', 'even', 'odd', 'even']

# Equivalent list comprehension
labels = ["even" if number % 2 == 0 else "odd" for number in range(5)]
print(labels)  # ['even', 'odd', 'even', 'odd', 'even']

# 5. Nested for loop
pairs = []
for x in range(2):
    for y in range(2):
        pairs.append((x, y))
print(pairs)  # [(0, 0), (0, 1), (1, 0), (1, 1)]

# Equivalent list comprehension
pairs = [(x, y) for x in range(2) for y in range(2)]
print(pairs)  # [(0, 0), (0, 1), (1, 0), (1, 1)]

print("Starting advanced iteration techniques tutorial...")
# ...existing code...

# Advanced iteration techniques.

# 1. enumerate() - get index and value together
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
    # 0 apple
    # 1 banana
    # 2 cherry

# enumerate() with a custom start value
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
    # 1 apple
    # 2 banana
    # 3 cherry

# 2. zip() - iterate over multiple lists in parallel
names = ["Alice", "Bob", "Charlie"]
ages = [20, 22, 19]
for name, age in zip(names, ages):
    print(name, age)
    # Alice 20
    # Bob 22
    # Charlie 19

# zip() with three lists
majors = ["CS", "MIS", "Biology"]
for name, age, major in zip(names, ages, majors):
    print(name, age, major)
    # Alice 20 CS
    # Bob 22 MIS
    # Charlie 19 Biology

# zip() stops at the shortest list
short_list = [1, 2]
long_list = [10, 20, 30, 40]
for a, b in zip(short_list, long_list):
    print(a, b)
    # 1 10
    # 2 20

# 3. reversed() - iterate in reverse order
for fruit in reversed(fruits):
    print(fruit)
    # cherry
    # banana
    # apple

# reversed() with range()
for number in reversed(range(5)):
    print(number)
    # 4 3 2 1 0

# 4. Iterating with indices using range(len(...))
for i in range(len(fruits)):
    print(i, fruits[i])
    # 0 apple
    # 1 banana
    # 2 cherry

# 5. Combining enumerate() and zip()
for index, (name, age) in enumerate(zip(names, ages)):
    print(index, name, age)
    # 0 Alice 20
    # 1 Bob 22
    # 2 Charlie 19

# 6. Using zip() to build a dictionary
student_ages = dict(zip(names, ages))
print(student_ages)  # {'Alice': 20, 'Bob': 22, 'Charlie': 19}

# 7. Reversed enumerate (reverse list, keep original indices in mind)
for index, fruit in reversed(list(enumerate(fruits))):
    print(index, fruit)
    # 2 cherry
    # 1 banana
    # 0 apple

