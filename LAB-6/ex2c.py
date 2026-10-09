list_of_lists = [
    ["dustin", 23, 95, "student", "monster"],
    ["lopera", 29, 54, 42, "professor", "funny", "clown"],
    ["anonymous", 30, 92, "worker"],
]

for list_values in list_of_lists:
    number_of_elements = len(list_values)
    print(f"\nThe list contains {number_of_elements} elements.")

    if number_of_elements < 5:
        print("The list has fewer than 5 elements.")
    elif number_of_elements <= 10:
        print("The list has between 5 and 10 elements, inclusive.")
    else:
        print("The list has more than 10 elements.")

def describe_list(values):
    count = len(values)

    if count < 5:
        return "The list has fewer than 5 elements."
    elif count <= 10:
        return "The list has between 5 and 10 elements, inclusive."
    else:
        return "The list has more than 10 elements."


list_of_lists = [
    ["dustin", 23, 95, "student", "monster"],
    ["lopera", 29, 54, 42, "professor", "funny", "clown"],
    ["anonymous", 30, 92, "worker"],
]

for values in list_of_lists:
    print(f"\nThe list contains {len(values)} elements.")
    print(describe_list(values))