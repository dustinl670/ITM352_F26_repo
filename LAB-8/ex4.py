


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

def GCD(num1, num2):
    for divisor in range(min(num1, num2) + 1, 1, -1):
        if num1 % divisor == 0 and num2 % divisor == 0:
            return divisor
        else:
            continue

print("The GCD of", num1, "and", num2, "is", GCD(num1, num2))