

emotions = ("surprised", "sad", "fear", "happy")

is_it_true = emotions[-1] == "happy" and len(emotions) > 3 # == checks if the thing on the left is equal to the thing on the right and returns True or False.
print(is_it_true)
print(emotions[-1] == "happy" and len(emotions) > 3)

if emotions[-1] == "happy" and len(emotions) > 3:
    print("Yes!")
else:
    print("No!")