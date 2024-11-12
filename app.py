# main program
from cal_func import do_addition, do_subtraction, do_multiply, do_divide
from square import do_square

def main():
    print(
        "Welcome to the Calculator!\n"
        "Please choose an operation:\n"
        "1. Addition (+)\n"
        "2. Subtraction (-)\n"
        "3. Multiplication (*)\n"
        "4. Division (/)\n"
        "5. Square (**) (calculates squares of both numbers)"
    )

    # Get the user’s choice and numbers
    choice = input("Enter your choice (1, 2, 3, 4, or 5): ")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Perform the calculation based on the user’s choice
    try:
        if choice == '1':
            result = do_addition(num1, num2)
            print("Result:", result)
        elif choice == '2':
            result = do_subtraction(num1, num2)
            print("Result:", result)
        elif choice == '3':
            result = do_multiply(num1, num2)
            print("Result:", result)
        elif choice == '4':
            result = do_divide(num1, num2)
            print("Result:", result)
        elif choice == '5':
            result1, result2 = do_square(num1, num2)
            print(f"Square of {num1} is {result1}")
            print(f"Square of {num2} is {result2}")
        else:
            print("Invalid choice! Please select a valid operation.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
