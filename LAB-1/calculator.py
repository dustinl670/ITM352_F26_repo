def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


while True:
    try:
        print("\nCalculator Menu")
        print("Available operations: +, -, *, /")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose an operation: ")

        if operation not in operations:
            print("Invalid operation. Please choose +, -, *, or /.")
            continue

        result = operations[operation](num1, num2)

        if result.is_integer():
            print(f"Result: {int(result)}")
        else:
            print(f"Result: {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except ZeroDivisionError as e:
        print(e)

    again = input("Do you want to perform another calculation? (y/n): ")
    if again.lower() != 'y':
        break
