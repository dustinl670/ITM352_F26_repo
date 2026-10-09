

list_values = [["dustin", 23, 95, "student", "monster"],
               ["lopera", 29, 54, 42, "professor", "funny", "clown"]]

number_of_elements = len(list_values)
print(f"The list contains {number_of_elements} elements.")

if number_of_elements < 5:
    print("The list has fewer than 5 elements.")
elif number_of_elements <= 10:
    print("The list has between 5 and 10 elements.")
else:
    print("The list has more than 10 elements.")