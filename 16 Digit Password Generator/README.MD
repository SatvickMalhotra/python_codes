# Random Password Generator🕵️‍♂️

## Introduction🤔🤔🤔🤔🤔🤔🤔
This is a simple Python script to generate random passwords. It creates passwords with a mix of uppercase letters, lowercase letters, digits, and special characters.

## Usage🗝🗝🗝🗝🗝🗝
To use the script, simply run it in a Python environment. It will prompt you for the number of passwords you want to generate and the platform for which you need the passwords. After entering this information, it will display the generated passwords along with their corresponding numbers.

## Requirements🗝
- Python 3.x

## How It Works
1. The script defines a function `generate_password()` to create a random password.
2. Inside this function, it defines sets of uppercase letters, lowercase letters, digits, and special characters using the `string` module.
3. It initializes an empty string `password` to store the generated password.
4. It selects the first character of the password as an uppercase letter.
5. It iterates through the rest of the required length (15 characters) and alternates between adding digits and lowercase letters.
6. Finally, it adds two special characters at the end of the password.
7. The main function `main()` prompts the user for the number of passwords and the platform, then generates and displays the passwords.

## Example🧐🧐🧐🧐
```python
How many passwords do you want? 3
For which platform do you need the passwords? Email

3 passwords for Email are:
------------------------------
| Password Number | Password        |
------------------------------
|      1          | S6jD5v#z@a9B!5d |
|      2          | E8pR9t#y@h6O!5w |
|      3          | W7rT2m#x@i4A!3z |
------------------------------
