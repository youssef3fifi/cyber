def ceaser_encryption(PlainText , Key):

    Key = int(Key)
    CipherText = ""
    for char in PlainText:
        if char.islower():
            c = (ord(char) - ord('a') + Key) % 26 + ord('a')
            CipherText += chr(c)
        elif char.isupper():
            c = (ord(char) - ord('A') + Key) % 26 + ord('A')
            CipherText += chr(c)
        else:
            CipherText += char

    return CipherText
def ceaser_decryption(cipherText , Key):
    Key = int(Key)
    PlainText = ""
    for char in cipherText:
        if char.islower():
            c = (ord(char) - ord('a') - Key) % 26 + ord('a')
            PlainText += chr(c)
        elif char.isupper():
            c = (ord(char) - ord('A') - Key) % 26 + ord('A')
            PlainText += chr(c)
        else:
            PlainText += char

    return PlainText