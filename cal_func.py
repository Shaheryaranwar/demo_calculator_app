def do_addition(num1, num2):
    return num1 + num2

def do_subtraction(num1, num2):
    return num1 - num2

def do_multiply(num1, num2):
    return num1 * num2

def do_divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        raise ValueError("Cannot divide by zero")
