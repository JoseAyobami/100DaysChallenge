alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode':\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#  TODO-1: Create a function called 'encrypt' that takes original_text and shift_amount as 2 inputs
def encrypt(original_text, shift_amount):
    cipher_text = ""

    for letters in original_text:
        shifted_position = alphabet.index(letters) + shift_amount
         
        shifted_position %= len(alphabet) 
        cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded: {cipher_text}")    


# encrypt(original_text=text, shift_amount=shift)

def decode(original_text, shift_amount):
    decrypt_code = ""

    for letter in original_text:
        shifted_position = alphabet.index(letter) - shift_amount

        shifted_position %= len(alphabet)
        decrypt_code += alphabet[shifted_position]
    print(f"Here is the encoded: {decrypt_code}")    


decode(original_text=text, shift_amount=shift)