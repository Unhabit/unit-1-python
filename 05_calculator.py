def calculator():
    print("Calculator!!")
    
    # Input validation for numbers
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            break
        except ValueError:
            print("Error: Please enter a valid number.")
    
    while True:
        try:
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Error: Please enter a valid number.")
    
    # Display available operations
    print("\nSelect operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Floor Division")
    print("6. Exponential")
    print("7. Remainder")
    
    # Input validation for operation choice
    while True:
        try:
            choice = int(input("Choose an operation (1-7): "))
            if choice not in range(1, 8):
                print("Error: Invalid operation. Please choose a number between 1 and 7.")
            else:
                break
        except ValueError:
            print("Error: Invalid input. Please enter a number between 1 and 7.")
    
    # Perform the operation based on user choice
    if choice == 1:
        # Addition
        result = num1 + num2
        print(f"Result: {result}")
    elif choice == 2:
        # Subtraction
        result = num1 - num2
        print(f"Result: {result}")
    elif choice == 3:
        # Multiplication
        result = num1 * num2
        print(f"Result: {result}")
    elif choice == 4:
        # Division
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"Result: {result}")
    elif choice == 5:
        # Floor Division
        if num2 == 0:
            print("Error: Floor division by zero is not allowed.")
        else:
            result = num1 // num2
            print(f"Result: {result}")
    elif choice == 6:
        # Exponential
        result = num1 ** num2
        print(f"Result: {result}")
    elif choice == 7:
        # Remainder
        if num2 == 0:
            print("Error: Remainder operation by zero is not allowed.")
        else:
            result = num1 % num2
            print(f"Result: {result}")


calculator()
