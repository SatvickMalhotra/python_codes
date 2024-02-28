import random
import string

def generate_password():
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation

    password = ''

    # First character (index 0): Uppercase letter
    password += random.choice(uppercase_letters)

    # Iterate through the rest of the required length 
    for i in range(1, 16):
        if i % 2 == 0:  # Even index: Number
            password += random.choice(digits)
        else:           # Odd index: Lowercase letter
            password += random.choice(lowercase_letters)

    # Last two characters: Special characters
    password += random.choice(special_chars)
    password += random.choice(special_chars)

    return password

def main():
    num_passwords = int(input("How many passwords do you want? "))
    platform = input("For which platform do you need the passwords? ")

    print(f"\n{num_passwords} passwords for {platform} are:")
    print("-" * 30)  # Table separator
    print("| Password Number | Password        |")
    print("-" * 30)

    for i in range(num_passwords):
        password = generate_password()
        print(f"|      {i + 1}          | {password} |")
    print("-" * 30)

if __name__ == "__main__":
    main()
