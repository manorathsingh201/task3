import string
import random

def generate_password(length, use_special_chars=True):
    """
    Generate a random password with the specified length and complexity.
    
    :param length: Length of the password
    :param use_special_chars: Boolean flag to include special characters
    :return: Generated password as a string
    """
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits
    if use_special_chars:
        characters += string.punctuation
    
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator!")

    # Input: Length of the password
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 1:
                print("Password length should be at least 1.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    # Input: Complexity choice
    while True:
        complexity_choice = input("Include special characters (y/n)? ").strip().lower()
        if complexity_choice in ['y', 'n']:
            use_special_chars = complexity_choice == 'y'
            break
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")
    
    # Generate and display the password
    password = generate_password(length, use_special_chars)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
