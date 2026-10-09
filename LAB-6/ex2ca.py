test_cases = [
    ["apple", 23, True, 2.5],  # 4 elements: fewer than 5
    ["apple", 23, True, 2.5, "blue"],  # 5 elements: within range
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],  # 10 elements: within range
    ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"],  # 11 elements: more than 10
]

for list_values in test_cases:
    number_of_elements = len(list_values)
    print(f"\nTesting a list with {number_of_elements} elements:")

    if number_of_elements < 5:
        print("The list has fewer than 5 elements.")
    elif number_of_elements <= 10:
        print("The list has between 5 and 10 elements, inclusive.")
    else:
        print("The list has more than 10 elements.")