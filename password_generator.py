import random
import string

def generate_password(length=12, use_special_chars=True):
    # Define character sets for password generation
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation if use_special_chars else ''

    # Combine character sets based on complexity
    if use_special_chars:
        charset = lower_case + upper_case + digits + special_chars
    else:
        charset = lower_case + upper_case + digits

    # Ensure the length of the password is at least 6 characters
    length = max(length, 6)

    # Generate a random password
    password = ''.join(random.choice(charset) for _ in range(length))

    return password

if __name__ == "__main__":
    try:
        length = int(input("Enter the desired password length: "))
        use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
        
        password = generate_password(length, use_special_chars)
        print(f"Generated password: {password}")
    
    except ValueError:
        print("Invalid input. Please enter a valid password length as a number.")
