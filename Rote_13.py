def encrypt(Plaintext):
    translated = ''
    for char in Plaintext:
        if char.isalpha():
            if char.isupper():
                translated += chr(((ord(char) - 65 + 13) % 26) + 65)
            elif char.islower():
                translated += chr(((ord(char) - 97 + 13) % 26) + 97)
        else:
            translated += char
    return translated

def decrypt(cipher_text):
    decrypted = ''
    for char in cipher_text:
        if char.isalpha():
            if char.isupper():
                decrypted += chr(((ord(char) - 65 - 13) % 26) + 65)
            elif char.islower():
                decrypted += chr(((ord(char) - 97 - 13) % 26) + 97)
        else:
            decrypted += char
    return decrypted

# def main():
#     choice = input("Enter 'e' to encrypt or 'd' to decrypt: ")
#
#     if choice == 'e':
#         message = input("Enter your plain text: ")
#         cipher_text = encrypt(message)
#         print("Cipher text:", cipher_text)
#     elif choice == 'd':
#         cipher_text = input("Enter your cipher text: ")
#         decrypted_text = decrypt(cipher_text)
#         print("Decrypted text:", decrypted_text)
#     else:
#         print("Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt.")
#
# if __name__ == "__main__":
#     main()
