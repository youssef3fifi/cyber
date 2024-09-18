#rail_fence_encrypt(plaintext, rails), rail must be integer
#rail_fence_decrypt(plaintext, rails), rail must be integer
def rail_fence_encrypt(plaintext, rails):
    rails = int(rails)
    fence = [[] for _ in range(rails)]  # Create a list of empty lists to represent the fence
    rail = 0
    direction = 1  # Direction of movement along the rails (down or up)
    space_indices = [i for i, char in enumerate(plaintext) if char == ' ']  # Store the indices of spaces

    # Fill the fence with characters from the plaintext
    for char in plaintext:
        if char == ' ':
            continue
        fence[rail].append(char)
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction *= -1  # Change direction when reaching the top or bottom rail

    # Flatten the fence and concatenate the characters
    encrypted_text = ''.join(char for rail in fence for char in rail)

    # Add the spaces back into the encrypted text
    for index in space_indices:
        encrypted_text = encrypted_text[:index] + ' ' + encrypted_text[index:]

    return encrypted_text

def rail_fence_decrypt(ciphertext, rails):
    rails = int(rails)
    fence = [['' for _ in ciphertext] for _ in range(rails)]  # Create an empty fence matrix
    rail = 0
    direction = 1
    space_indices = [i for i, char in enumerate(ciphertext) if char == ' ']  # Store the indices of spaces

    # Remove spaces from ciphertext
    ciphertext = ciphertext.replace(' ', '')

    # Fill the fence matrix with placeholders for characters
    for i in range(len(ciphertext)):
        fence[rail][i] = '*'
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction *= -1

    # Fill the fence matrix with ciphertext characters
    index = 0
    for i in range(rails):
        for j in range(len(ciphertext)):
            if fence[i][j] == '*':
                fence[i][j] = ciphertext[index]
                index += 1

    # Read the characters from the fence matrix to retrieve the plaintext
    rail = 0
    direction = 1
    decrypted_text = ''
    for i in range(len(ciphertext)):
        decrypted_text += fence[rail][i]
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction *= -1

    # Add the spaces back into the decrypted text
    for index in space_indices:
        decrypted_text = decrypted_text[:index] + ' ' + decrypted_text[index:]

    return decrypted_text
# print(rail_fence_encrypt("HELLO WOrLD", 3))
# print(rail_fence_decrypt(rail_fence_encrypt("HELLO WOrLD", 3), 3))