"""
Task 2 - Password Generator
CodSoft Python Programming Internship

Generates a strong random password based on the length and
complexity chosen by the user.
"""

import random
import string


def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    char_pool = ""

    if use_letters:
        char_pool += string.ascii_letters
    if use_numbers:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation

    if not char_pool:
        return None

    password = "".join(random.choice(char_pool) for _ in range(length))
    return password


def main():
    print("===== PASSWORD GENERATOR =====")

    try:
        length = int(input("Enter desired password length: "))
        if length <= 0:
            print("Length must be a positive number.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    print("\nChoose complexity (y/n):")
    use_letters = input("Include letters? (y/n): ").strip().lower() == "y"
    use_numbers = input("Include numbers? (y/n): ").strip().lower() == "y"
    use_symbols = input("Include symbols? (y/n): ").strip().lower() == "y"

    if not (use_letters or use_numbers or use_symbols):
        print("You must select at least one character type.")
        return

    password = generate_password(length, use_letters, use_numbers, use_symbols)
    print(f"\nGenerated Password: {password}")


if __name__ == "__main__":
    main()
