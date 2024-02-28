import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def Easy_Password_Generator():
    password = ""

    for letter in range(0, letters_count):
        random_letter = random.choice(letters)
        password += random_letter
    for symbol in range(0, symbols_count):
        random_symbol = random.choice(symbols)
        password += random_symbol
    for number in range(0, numbers_count):
        random_number = random.choice(numbers)
        password += random_number

    print(f"Your password using the easy-mode is: {password}")

def Hard_Password_Generator():
    password_list = []
    password = ""

    for letter in range(0, letters_count):
        random_letter = random.choice(letters)
        password_list += random_letter
    for symbol in range(0, symbols_count):
        random_symbol = random.choice(symbols)
        password_list += random_symbol
    for number in range(0, numbers_count):
        random_number = random.choice(numbers)
        password_list += random_number

    random.shuffle(password_list)
    
    for char in password_list:
        password += char

    print(f"Your password using the hard-mode is: {password}")

print("Welcome to the PyPassword Generator!")
letters_count = int(input("How many letters would you like in the password?\n"))
symbols_count = int(input("How many symbols would you like?\n"))
numbers_count = int(input("How many numbers would you like?\n"))

Easy_Password_Generator()
Hard_Password_Generator()