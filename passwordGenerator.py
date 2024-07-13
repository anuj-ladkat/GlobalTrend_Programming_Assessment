import random
import string

def generate_random_password(length):
    """
    Generate a random password with the specified length.

    :param length: Length of the password (default is 12).
    :return: A random password as a string.
    """
    # Define characters for each category
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation  # includes !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

    # Combine all characters
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate a random password using random.choices (Python 3.6+)
    password = ''.join(random.choices(all_characters, k=length))

    return password

# Example usage
if __name__ == "__main__":
    length = int(input("Enter the length of the password: "))
    if(length>0):
        password = generate_random_password(length)
        print(f"Generated Password: {password}")
    else:
        print("Cannot Generate Password, Give length Greater Than Zero")