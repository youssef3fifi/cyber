import numpy as np

# encryptHill2x2(text, keyMatrix)   -->> you can insert the keymatrix in two ways -- first way("7 8 11 11") -- second way("hill")
# decryptHill2x2(ciphertext, keyMatrix)

def charToNum(char):
    return ord(char.lower()) - ord('a')

def numToChar(num, is_upper):
    char = chr(num % 26 + ord('a'))
    if is_upper:
        return char.upper()
    else:
        return char

def multiplyAndConvert(pair, keyMatrix):
    pairNums = np.array([[charToNum(char)] for char in pair])
    resultNums = np.dot(keyMatrix, pairNums).ravel() % 26
    return ''.join(numToChar(num, char.isupper()) for num, char in zip(resultNums, pair))

def encryptHill2x2(text, keyMatrix):
    if keyMatrix.replace(' ', '').isdigit():
        # Split the string into a list of numbers
        numbers = list(map(int, keyMatrix.split()))
        # Arrange the numbers into a 2D numpy array
        keyMatrix = np.array(numbers).reshape(-1, 2)
    elif keyMatrix.isalpha():
        keyMatrix = key_matrix(keyMatrix)

    space_indices = [i for i, char in enumerate(text) if char == ' ']
    text = text.replace(' ', '')
    pairs = [text[i:i+2] for i in range(0, len(text), 2)]
    cipher = ''.join(multiplyAndConvert(pair, keyMatrix) for pair in pairs)
    for index in space_indices:
        cipher = cipher[:index] + ' ' + cipher[index:]
    return cipher


#----------------------------------------------------------------

def key_matrix(key):
    key_values = [ord(char) - ord('a') for char in key]
    matrix = np.array([[key_values[0], key_values[1]], [key_values[2], key_values[3]]])
    if np.linalg.det(matrix) == 0:
        print("Invalid Key")
        exit()

    return matrix


def inverse_matrix(matrix):
    det = int(round(np.linalg.det(matrix)))
    inv_det = pow(det, -1, 26)
    adjoint_matrix = np.array([[matrix[1][1], -matrix[0][1]], [-matrix[1][0], matrix[0][0]]])
    inverse = (inv_det * adjoint_matrix) % 26
    return inverse


def decryptHill2x2(ciphertext, keyMatrix):
    if isinstance(keyMatrix, str):
        if keyMatrix.replace(' ', '').isdigit():
            # Split the string into a list of numbers
            numbers = list(map(int, keyMatrix.split()))
            # Arrange the numbers into a 2D numpy array
            keyMatrix = np.array(numbers).reshape(-1, 2)
        elif keyMatrix.isalpha():
            keyMatrix = key_matrix(keyMatrix)

    space_indices = [i for i, char in enumerate(ciphertext) if char == ' ']
    ciphertext = ciphertext.replace(' ', '')
    inv_key = inverse_matrix(keyMatrix)
    ciphertext_values = [ord(char.lower()) - ord('a') for char in ciphertext]
    plaintext = ""
    for i in range(0, len(ciphertext_values), 2):
        block = np.array([[ciphertext_values[i]], [ciphertext_values[i + 1]]])
        decrypted_block = np.dot(inv_key, block) % 26
        for value, original_char in zip(decrypted_block, ciphertext[i:i+2]):
            plaintext += numToChar(value[0], original_char.isupper())
    for index in space_indices:
        plaintext = plaintext[:index] + ' ' + plaintext[index:]
    return plaintext

# print(encryptHill2x2("Short example", "7 8 11 11"))
# print(decryptHill2x2("Apadj tftwlfj", "hill"))