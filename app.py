from cal_func import do_addition, do_subtraction, do_multiply, do_divide

def main():
    print(
        "Welcome to the Calculator!\n"
        "Please choose an operation:\n"
        "1. Addition (+)\n"
        "2. Subtraction (-)\n"
        "3. Multiplication (*)\n"
        "4. Division (/)"
    )

    # Get the user’s choice and numbers
    choice = input("Enter your choice (1, 2, 3, or 4): ")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Perform the calculation based on the user’s choice
    try:
        if choice == '1':
            result = do_addition(num1, num2)
        elif choice == '2':
            result = do_subtraction(num1, num2)
        elif choice == '3':
            result = do_multiply(num1, num2)
        elif choice == '4':
            result = do_divide(num1, num2)
        else:
            print("Invalid choice! Please select a valid operation.")
            return  # Exit the function if the choice is invalid
    except ValueError as e:
        print(f"Error: {e}")
        return  # Exit if division by zero or other error occurs

    # Print the result if a valid calculation was made
    print("Result:", result)

if __name__ == "__main__":
    main()
