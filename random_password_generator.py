import random
import string


def generate_password(length, upper_case, lower_case, numbers, special_chars):
    characters = ""
    if upper_case:
        characters += string.ascii_uppercase
    if lower_case:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    password = "".join(random.choice(characters) for _ in range(length))
    return password


length = int(input("Enter the desired length of the password: "))
upper_case = input("Include upper case letters? (y/n) ").lower() == "y"
lower_case = input("Include lower case letters? (y/n) ").lower() == "y"
numbers = input("Include numbers? (y/n) ").lower() == "y"
special_chars = input("Include special characters? (y/n) ").lower() == "y"


print("Generated password:", generate_password(length, upper_case, lower_case, numbers, special_chars))