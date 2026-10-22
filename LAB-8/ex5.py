


palindrome = "racecar"
isItPalindrome = " "
print(palindrome)

def is_palindrome(palindrome, isItPalindrome):
    for letters in range (len(palindrome), 0, -1):
        if palindrome[letters - 1] != palindrome[len(palindrome) - letters]:
            return False
        else:
            return True

print("Is the word a palindrome?", isItPalindrome)
print(is_palindrome(palindrome, isItPalindrome))