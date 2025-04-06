
from ceaser_art import art
print(art)


def encrypt_decrypt(original_text, shift_amount, encode_decode):
    decode_text = ""
    if encode_decode == "decode":
                shift_amount *= -1

    for letter in original_text:

        if letter not in alphabet:
            decode_text += letter
        else:            
            # Add the index of "text" input to shift
            shifted_position = alphabet.index(letter) + shift_amount

            # To make the index of list not go out of range
            shifted_position %= len(alphabet)
            decode_text += alphabet[shifted_position]    
        

    print(f"Here is the {encode_decode}d: {decode_text}")   


coninue_action = True

while coninue_action:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    encrypt_decrypt(original_text=text, shift_amount=shift, encode_decode=direction)

    redo_action = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if redo_action == "no":
        coninue_action = False
        print("Goodbye")



