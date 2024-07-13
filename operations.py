def perform_operation(num1, num2, operator):
    """
    Perform arithmetic operation based on the provided operator.

     num1: The first number (operand).
     num2: The second number (operand).
     operator: The arithmetic operator as a string ('+', '-', '*', '/').
     The result of the arithmetic operation.
    """
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ValueError("Division by zero is not allowed.")
        return num1 / num2
    else:
        raise ValueError(f"Unsupported operator '{operator}'")

# Example usage
if __name__ == "__main__":
    num1 = 10
    num2 = 5
    operator = '+'
    result = perform_operation(num1, num2, operator)
    print(f"{num1} {operator} {num2} = {result}")

    num1 = 20
    num2 = 4
    operator = '/'
    try:
        result = perform_operation(num1, num2, operator)
        print(f"{num1} {operator} {num2} = {result}")
    except ValueError as e:
        print(e)
