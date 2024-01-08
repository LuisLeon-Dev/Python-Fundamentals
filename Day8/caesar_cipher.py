from alphabet import alphabet

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text_to_encrypt, shift_number):
    encrypted_text = ""
    for char in text_to_encrypt:
        position = alphabet.index(char)
        new_position = position + shift_number
        new_char = alphabet[new_position]
        encrypted_text += new_char
    return print(encrypted_text)


encrypt(text_to_encrypt=text, shift_number=shift)
