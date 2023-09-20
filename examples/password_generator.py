import random
import string

def generate_password(length):
    """
    Generate a random password of specified length
    """
    # Define the possible characters to use in the password
    chars = string.ascii_letters + string.digits + string.punctuation

    # Use random.choices() to generate a list of length "length" from the character set
    password = ''.join(random.choices(chars, k=length))

    return password

while True:
    print("Enter '1' to generate a new password")
    print("Enter '2' to exit")

    choice = input("Enter choice: ")

    if choice == '1':
        length = int(input("Enter password length: "))
        password = generate_password(length)
        print("Your password is:", password)

    elif choice == '2':
        break

    else:
        print("Invalid input")

