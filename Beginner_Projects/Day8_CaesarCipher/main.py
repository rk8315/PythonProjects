import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
end_program = False

def caesar(user_text, shift_amount, direction_type):
    output_text = ""
    if direction_type.lower() == "decode":
        shift_amount *= -1
    for character in user_text:
        if character in alphabet:
            position = alphabet.index(character)
            new_position = position + shift_amount
            output_text += alphabet[new_position]
        else:
            output_text += character
    print(f"The {direction_type}d text is: {output_text}")

def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]
    print(f"The decoded text is {plain_text}")

print(art.logo)

while not end_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26

    caesar(user_text=text, shift_amount=shift, direction_type=direction)

    restart = input("Go again? no / yes : ")
    if restart.lower() == "no":
        end_program = True
        print("Ending Program")