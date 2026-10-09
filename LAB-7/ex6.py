data = ("hello", 10, "goodbye", 3, "goodnight", 5)

string_count = 0

for item in data:
    if type(item) == str:
        string_count += 1

print("There are", string_count, "strings in the data.")

new_item = input("Enter an item to add to the tuple: ")
try:
    data.append(new_item)
except AttributeError:
    data_list = list(data)
    data_list.append(new_item)
    data = tuple(data_list)

print("Tuple with the new item:", data)