def encryption_vigenere_cipher(plaintext, key):
    all_letters = "abcdefghijklmnopqrstuvwxyz"
    encryption = ""
    plaintext = plaintext.lower()

    key = key.lower()

    oldkey1 = len(plaintext) // len(key)
    oldkey2 = len(plaintext) / len(key)
    if oldkey2 > oldkey1:
        oldkey1 += 1

    key *= oldkey1

    j = 0
    for i in range(len(plaintext)):
        if plaintext[i] != ' ':
            number_of_letter_in_message = all_letters.find(plaintext[i])
            number_of_letter_in_key = all_letters.find(key[j])
            number_of_letter_in_encryption = (number_of_letter_in_message + number_of_letter_in_key) % 26
            encryption += all_letters[number_of_letter_in_encryption]
            j += 1
        else:
            encryption += ' '
    return encryption


def decryption_vigenere_cipher(ciphertext, key):
    all_letters = "abcdefghijklmnopqrstuvwxyz"
    decryption = ""
    ciphertext = ciphertext.lower()
    key = key.lower()

    oldkey1 = len(ciphertext) // len(key)
    oldkey2 = len(ciphertext) / len(key)
    if oldkey2 > oldkey1:
        oldkey1 += 1

    key *= oldkey1

    j = 0
    for i in range(len(ciphertext)):
        if ciphertext[i] != ' ':
            number_of_letter_in_message = all_letters.find(ciphertext[i])
            number_of_letter_in_key = all_letters.find(key[j])
            if (number_of_letter_in_message - number_of_letter_in_key) < 0:
                number_of_letter_in_decryption = (number_of_letter_in_message - number_of_letter_in_key) + 26
                decryption += all_letters[number_of_letter_in_decryption]
            else:
                number_of_letter_in_decryption = (number_of_letter_in_message - number_of_letter_in_key) % 26
                decryption += all_letters[number_of_letter_in_decryption]
            j += 1
        else:
            decryption += ' '
    return decryption

#
# def main():
#     weneed = int(input())
#     if weneed == 1:
#         plaintext = input()
#         key = input()
#         print(encryption_vigenere_cipher(plaintext, key))
#     elif weneed == 2:
#         ciphertext = input()
#         key = input()
#         print(decryption_vigenere_cipher(ciphertext, key))
#
#
# if __name__ == "__main__":
#     main()
