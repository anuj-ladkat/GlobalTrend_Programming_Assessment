import time
import functools

def measure_time(func):
    """
    A decorator function to measure the execution time of a function and log it.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' took {execution_time:.6f} seconds to execute.")
        return result
    return wrapper

# Example: Applying the decorator to a function that performs a computationally expensive task
@measure_time
def compute_fibonacci(n):
    """
    A function to compute the nth Fibonacci number (recursively).
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return compute_fibonacci(n - 1) + compute_fibonacci(n - 2)

# Example usage
if __name__ == "__main__":
    n = 10
    result = compute_fibonacci(n)
    print(f"The {n}th Fibonacci number is: {result}")
