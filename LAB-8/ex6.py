

usernum = int(input("Enter a number: "))
searchMe  = [2, 5, 7, 11, 15, 22, 27, 30, 34, 41, 55, 57, 58, 60, 77]

def numSearch(usernum, searchMe):
    for i in range(len(searchMe)):
        if searchMe[i] == usernum:
            return True
    return False

print("Is the number in the list?", numSearch(usernum, searchMe))
