# Open a file and read its contents.

with open("namelist.txt", "r") as file_object:
    contents = file_object.read()
    print(contents)
    content_lists = contents.split("\n")
    print("Number of names:", len(content_lists))
    for name in content_lists:
        print(name)

file_object.closed