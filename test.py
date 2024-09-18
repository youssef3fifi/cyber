import string
from collections import OrderedDict
from tkinter import messagebox


def prepare_key(key):
    """Prepares the key for the Playfair cipher by removing duplicate letters and padding with 'X' if necessary."""
    key = key.upper().replace('J', 'I')  # Replace 'J' with 'I' to handle the Playfair grid
    key_without_duplicates = "".join(OrderedDict.fromkeys(key))
    alphabet = string.ascii_uppercase.replace('J', '')  # Use the alphabet without 'J'
    for letter in alphabet:
        if letter not in key_without_duplicates:
            key_without_duplicates += letter
    return key_without_duplicates


def generate_playfair_grid(key):
    """Generates the Playfair grid from the given key."""
    key = prepare_key(key)
    grid = [key[i:i + 5] for i in range(0, 25, 5)]
    return grid


def find_letter_location(grid, letter):
    """Finds the row and column of a letter in the Playfair grid."""
    for i, row in enumerate(grid):
        if letter in row:
            return i, row.index(letter)
    raise ValueError(f"Letter '{letter}' not found in the Playfair grid.")


def encrypt_playfair(text, key):
    """Encrypts the plaintext using the Playfair cipher."""
    # Check if any of the fields are empty
    if not text.strip() or not key.strip():
        messagebox.showerror("Error", "Please fill in both text and key fields.")
        return

    # Check if the key contains any numbers
    if any(char.isdigit() for char in key):
        messagebox.showerror("Error", "Key cannot contain numbers.")
        return

    text = text.upper().replace('J', 'I')  # Replace 'J' with 'I' to handle the Playfair grid
    grid = generate_playfair_grid(key)
    ciphertext = ""
    i = 0
    while i < len(text):
        pair = text[i:i + 2]
        if len(pair) < 2:  # If the pair has only one letter, add a filler letter 'X'
            pair += 'X'
            i -= 1  # Move back one step to handle the second letter
        elif pair[0] == pair[1]:  # If both letters are the same, insert a filler 'X'
            pair = pair[0] + 'X'
            i -= 1  # Move back one step to handle the second letter
        row1, col1 = find_letter_location(grid, pair[0])
        row2, col2 = find_letter_location(grid, pair[1])
        if row1 == row2:  # If the letters are in the same row
            ciphertext += grid[row1][(col1 + 1) % 5] + grid[row2][(col2 + 1) % 5]
        elif col1 == col2:  # If the letters are in the same column
            ciphertext += grid[(row1 + 1) % 5][col1] + grid[(row2 + 1) % 5][col2]
        else:  # If the letters form a rectangle in the grid
            ciphertext += grid[row1][col2] + grid[row2][col1]
        i += 2
    return f"Encrypted text using with key {key}: {ciphertext}"


def decrypt_playfair(text, key):
    """Decrypts the ciphertext using the Playfair cipher."""
    # Check if any of the fields are empty
    if not text.strip() or not key.strip():
        messagebox.showerror("Error", "Please fill in both text and key fields.")
        return

    # Check if the key contains any numbers
    if any(char.isdigit() for char in key):
        messagebox.showerror("Error", "Key cannot contain numbers.")
        return
    grid = generate_playfair_grid(key)
    plaintext = ""
    i = 0
    while i < len(text):
        pair = text[i:i + 2]
        row1, col1 = find_letter_location(grid, pair[0].upper())  # Convert letters to uppercase
        row2, col2 = find_letter_location(grid, pair[1].upper())  # Convert letters to uppercase
        if row1 == row2:  # If the letters are in the same row
            plaintext += grid[row1][(col1 - 1) % 5] + grid[row2][(col2 - 1) % 5]
        elif col1 == col2:  # If the letters are in the same column
            plaintext += grid[(row1 - 1) % 5][col1] + grid[(row2 - 1) % 5][col2]
        else:  # If the letters form a rectangle in the grid
            plaintext += grid[row1][col2] + grid[row2][col1]
        i += 2
    plaintext = plaintext.replace('X', '')  # Remove 'X' characters from the plaintext
    return f"Decrypted text using  with key {key}: {plaintext}"