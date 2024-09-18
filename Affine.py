def encryption_affine_cipher(plaintext, a, b):
    all_letter = "abcdefghijklmnopqrstuvwxyz"
    encryption = ""
    plaintext = plaintext.lower()

    for char in plaintext:
        if char != ' ':
            c = ((a * all_letter.find(char)) + b) % 26
            encryption += all_letter[c]
        else:
            encryption += ' '

    return encryption


def decryption_affine_cipher(ciphertext, a, b):
    all_letter = "abcdefghijklmnopqrstuvwxyz"
    decryption = ""
    ciphertext = ciphertext.lower()

    a_inverse = -1
    for i in range(26):
        if (a * i) % 26 == 1:
            a_inverse = i
            break

    for char in ciphertext:
        if char != ' ':
            c = (a_inverse * (all_letter.find(char) - b + 26)) % 26
            decryption += all_letter[c]
        else:
            decryption += ' '

    return decryption


# def main():
#     print("if need encryption by Affine cipher enter 1 else if need decryption by Affine cipher enter 2:")
#     weneed = int(input())
#     if weneed == 1:
#         plaintext = input("Enter plaintext: ")
#         a = int(input("Enter value of a: "))
#         b = int(input("Enter value of b: "))
#         print(encryption_affine_cipher(plaintext, a, b))
#     elif weneed == 2:
#         ciphertext = input("Enter ciphertext: ")
#         a = int(input("Enter value of a: "))
#         b = int(input("Enter value of b: "))
#         print(decryption_affine_cipher(ciphertext, a, b))
#
#
# if __name__ == "__main__":
#     main()
def place(x, y, width, height):
    return None