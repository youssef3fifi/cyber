
import random

alphabet = 'abcdefghijklmnopqrstuvwxyz.,! '
key = 'nu.t!iyvxqfl,bcjrodhkaew spzgm'

def makeKey(alphabet):
   alphabet = list(alphabet)
   random.shuffle(alphabet)
   return ''.join(alphabet)

def encrypt(plaintext, key):
    alphabet  = "abcdefghijklmnopqrstuvwxyz"
    keyIndices = [alphabet.index(k.lower()) for k in plaintext]
    return ''.join(key[keyIndex] for keyIndex in keyIndices)

def decrypt(cipher, key):
    alphabet  = "abcdefghijklmnopqrstuvwxyz"
    keyIndices = [key.index(k) for k in cipher]
    return ''.join(alphabet[keyIndex] for keyIndex in keyIndices)
def main():
   choice = input("Enter 'e' to encrypt or 'd' to decrypt: ")

   if choice == 'e':
       message = input("Enter Your Message To Encode: ")
       cipher = encrypt(message, key, alphabet)
       print("Encoded Message: ", cipher)
   elif choice == 'd':
       cipher = input("Enter Your Cipher To Decode: ")
       message = decrypt(cipher, key, alphabet)
       print("Decoded Message: ",message)
   else:
       print("Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt.")

# if __name__ == "__main__":
#    main()






