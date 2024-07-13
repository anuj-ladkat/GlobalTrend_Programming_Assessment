def divide_numbers(dividend, divisor):
    """
    Divide two numbers and handle the case where the divisor is zero.
    dividend: The number to be divided (numerator).
    divisor: The number to divide by (denominator).
     The result of the division if divisor is not zero,
             otherwise return a custom error message.
    """
    try:
        result = dividend / divisor
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    else:
        return result

# Example usage
if __name__ == "__main__":
    num1 = 10
    num2 = 0
    result = divide_numbers(num1, num2)
    print(result)
