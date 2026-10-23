# Read the entire file using readlines().

with open("namelist.txt", "r") as file_object:
    names = file_object.readlines()
    print("The number of names is:", len(names))
    for name in names:
        print(name.strip())