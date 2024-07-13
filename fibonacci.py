def fibonacci(n):
    """
    Compute the nth Fibonacci number using recursion.

    :param n: The position in the Fibonacci sequence.
    :return: The nth Fibonacci number.
    """
    # Base cases
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
if __name__ == "__main__":
    n = 10
    result = fibonacci(n)
    print(f"The {n}th Fibonacci number is: {result}")
