import math
#Validations Key is a string , (Key Must be a Number), (Key must have size greater than 1) ,(key must be unique, ["1234" is valid] ["1223" is not valid] )
# columnar_transposition_encrypt(msg, key) -->> key is a string, you insert a number
# columnar_transposition_decrypt(cipher, key)
def columnar_transposition_encrypt(msg, key):
    cipher = ""
    k_indx = 0
    msg = msg.replace(" ", "")
    msg_len = float(len(msg))
    msg_lst = list(msg)
    key_lst = sorted(list(key))
    col = len(key)
    row = int(math.ceil(msg_len / col))
    fill_null = int((row * col) - msg_len)
    msg_lst.extend(' ' * fill_null)
    matrix = [msg_lst[i: i + col] for i in range(0, len(msg_lst), col)]

    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        cipher += ''.join([row[curr_idx] for row in matrix])
        k_indx += 1

    return cipher


def columnar_transposition_decrypt(cipher, key):

    k_indx = 0
    msg_indx = 0
    msg_len = float(len(cipher))
    msg_lst = list(cipher)

    # Calculate column of the matrix
    col = len(key)

    # Calculate maximum row of the matrix
    row = int(math.ceil(msg_len / col))

    # Convert key into list and sort
    # alphabetically so we can access
    # each character by its alphabetical position.
    key_lst = sorted(list(key))

    # Create an empty matrix to
    # store deciphered message
    dec_cipher = []
    for _ in range(row):
        dec_cipher += [[None] * col]

    # Arrange the matrix column wise according
    # to permutation order by adding into new matrix
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])

        for j in range(row):
            dec_cipher[j][curr_idx] = msg_lst[msg_indx]
            msg_indx += 1
        k_indx += 1

    # Convert decrypted msg matrix into a string
    try:
        msg = ''.join(sum(dec_cipher, []))
    except TypeError:
        raise TypeError("This program cannot handle repeating words.")

    null_count = msg.count(' ')

    if null_count > 0:
        msg = msg[: -null_count]
    return msg
#
# print(columnar_transposition_encrypt("OOO", "1234"))
# print(columnar_transposition_decrypt(columnar_transposition_encrypt("Hello", "1234"), "1234"))
