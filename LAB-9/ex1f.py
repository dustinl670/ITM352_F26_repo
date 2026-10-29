# Open namelist.txt and read its contents.
# Append a new name at the end of the file.

import os

filename = "namelist.txt"

# Only open the file if it exists and is readable
if os.path.exists(filename) and os.access(filename, os.R_OK):
    print(f"File size: {os.path.getsize(filename)} bytes")
    print(f"Writable: {os.access(filename, os.W_OK)}")

    with open(filename, "r") as file_object:
        content_list = file_object.readlines()
        print(content_list)

    with open(filename, "a") as file_object:
        print("Appending a new name to the file...")
        file_object.write("Lopera, Dustin\n")
else:
    print(f"{filename} does not exist or is not readable.")