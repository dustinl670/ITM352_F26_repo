# Open namelist.txt and read its contents.
# Append a new name at the end of the file.

with open("namelist.txt", "r") as file_object:
    content_list = file_object.readlines()
    print(content_list)

with open("namelist.txt", "a") as file_object:
    print("Appending a new name to the file...")
    file_object.write("Lopera, Dustin\n")