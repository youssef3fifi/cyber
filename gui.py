import string
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog, messagebox
from tkinter.font import Font

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame0")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
import Ceaser
import Row_Col
import Affine
import Rote_13
import playfair
import Rail_Fence
import substitution
import vigenere
import RSA
import hill
###########################################################################################################
def download(type):
    if type == "Encrypt":
        message = entry_1.get()
    else:
        message = entry_3.get()
    if message is not None:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")],
                                                 title=f"Save {type} Message As")

        if file_path:
            # Write the encrypted message to the chosen file
            with open(file_path, "w") as file:
                file.write(message)

            messagebox.showinfo("Download", "Your Encrypted Message is Downloaded Successfully.")
        else:
            messagebox.showinfo("Download", "Download Cancelled.")
def add_content(type):
    # Ask the user to choose the file

    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")], title="Choose File")

    if file_path:
        # Open the selected file and read its content
        with open(file_path, "r") as file:
            file_content = file.read()

        # Insert the file content into the entry widget
        if type == "Encrypt":
            entry_1.delete("0", "end")
            entry_1.insert("0", file_content)
        else:
            entry_3.delete("0", "end")
            entry_3.insert("0", file_content)

        messagebox.showinfo("File Loaded", "Content from the selected file has been loaded.")
    else:
        messagebox.showinfo("No File Selected", "No file selected. Operation cancelled.")
def get_A_And_B(Key_Text_Box):
    key_str = Key_Text_Box.get()  # Get the key value as a string
    # Split the text by comma and space
    numbers = key_str.split(',')

    # If there are not exactly two numbers, return None
    if len(numbers) != 2:
        return None, None

    # Extract and convert the numbers to integers
    num1 = int(numbers[0])
    num2 = int(numbers[1])

    return num1, num2
######################################################################################################
global CipherAlgorithm
CipherAlgorithm = ""
def setAlgorithm(type):
    global CipherAlgorithm
    CipherAlgorithm = type
    messagebox.showinfo("Cipher Algorithm", "Your Cipher Algorithm is set to " + type + ".")
    global entry_2  # Declare entry_2 as a global variable
    if "entry_2" in globals():
        entry_2.destroy()  # Destroy entry_2 if it exists

    if CipherAlgorithm != "Root13":
        entry_2 = Entry(
            bd=0,
            bg="#27272A",
            fg="green",
            highlightthickness=0,
            font=("Inter Semibold", 20 * -1)
        )
        entry_2.place(
            x=133.0,
            y=466.0,
            width=652.0,
            height=43.0
        )
    else:
        pass  # Do nothing if CipherAlgorithm is "Root13"
def GetEncryptionAlgorithm():
    global CipherAlgorithm

    if CipherAlgorithm == "Ceaser":
        ceaser_encryption()
    elif CipherAlgorithm == "Row-Col":
        Row_col_encryption()
    elif CipherAlgorithm == "Root13":
        Root13_encryption()
    elif CipherAlgorithm == "playfair":
        playfair_encryption()
    elif CipherAlgorithm == "realfence":
        Railfence_encryption()
    elif CipherAlgorithm == "subistitution":
        subistitution_encryption()
    elif CipherAlgorithm == "Affine":
        Affine_encryption()
    elif CipherAlgorithm == "vigenere":
        vigenere_encryption()
    elif CipherAlgorithm == "Hill":
        hill_encryption()
    elif CipherAlgorithm == "RSA":
        rsa_encryption()
    else:
        messagebox.showinfo("Error", "please choose cipher")
def GetDecryptionAlgorithm():
    global CipherAlgorithm

    if CipherAlgorithm == "Ceaser":
        ceaser_decryption()
    elif CipherAlgorithm == "Row-Col":
        Row_col_decryption()
    elif CipherAlgorithm == "Root13":
        Root13_decryption()
    elif CipherAlgorithm == "playfair":
        playfair_decryption()
    elif CipherAlgorithm == "realfence":
        Railfence_decryption()
    elif CipherAlgorithm == "subistitution":
        subistitution_decryption()
    elif CipherAlgorithm == "Affine":
        Affine_decryption()
    elif CipherAlgorithm == "vigenere":
        vigenere_decryption()
    elif CipherAlgorithm == "Hill":
        hill_decryption()
    elif CipherAlgorithm == "RSA":
        rsa_decryption()
    else:
        messagebox.showinfo("Error", "please choose cipher")
#####################################################################################################
def GetPlaintext():
    plaintext = entry_1.get()
    if not plaintext.strip():
        error_message = "Please enter some text."
        print(error_message)
        messagebox.showerror("Error", error_message)
        return None
    elif not ''.join(c for c in plaintext if c not in (' ', '\n','\r')).isalpha():
        error_message = "Please enter only alphabetic characters (excluding spaces and end-of-line characters)."
        print(error_message)
        messagebox.showerror("Error", error_message)
        return None
    else:
        return plaintext
    return entry_1.get()
def GetKey():
    key_str = entry_2.get()
    try:
        if CipherAlgorithm == "Ceaser":
            key = int(key_str)  # For Cipher, key is an integer
        elif CipherAlgorithm == "realfence":
            key_str = int(key_str)
            if key_str <= 1:
                messagebox.showerror("Error", "Key should be higher than 1")
            else:
                key = int(key_str)  # For Cipher, key is an integer
        elif CipherAlgorithm == "Row-Col":
            if len(set(key_str.replace(" ","")))!=len(key_str.replace(" ","")):
                messagebox.showerror("Error", "Key should not repeted.")
            else:

             key = key_str
        elif CipherAlgorithm == "playfair"  or CipherAlgorithm == "AES":
            if not key_str.strip():
                messagebox.showerror("Error", "Key should not be empty.")
            elif any(char.isdigit() for char in key_str):
                messagebox.showerror("Error", "Key should not contain numbers.")
            else:
                key = key_str
        elif CipherAlgorithm == "subistitution":
            if set(key_str.lower()) != set(string.ascii_lowercase) or len(key_str) != 26:
                messagebox.showerror("Error", "Key must contain all alphabets.")
            else:
                key = key_str
        elif CipherAlgorithm == "vigenere":
            if not key_str.isalpha():
                messagebox.showerror("Error", "Key must be alphabetic only")
                return None
            else:
                key = key_str
        elif CipherAlgorithm == "DES" or CipherAlgorithm == "Hill":
            if CipherAlgorithm == "Hill":
                if len(key_str.replace(" ", "")) != 4:
                    messagebox.showerror("Error", "Key must consist of 4 numbers only")
                    return None
            key = key_str
        elif CipherAlgorithm == "Affine" or CipherAlgorithm == "RSA":
            Lhalf = ""
            Rhalf = ""
            i = 0
            key_str = key_str.replace(" ", "")
            for c in key_str:
                if c == ',': break
                i += 1
            Lhalf = key_str[0:i]
            Rhalf = key_str[i + 1:]
            flag = False
            print(key_str)
            if any((not char.isdigit()) for char in Lhalf) or any((not char.isdigit()) for char in Rhalf) or len(
                    Lhalf) == 0 or len(Rhalf) == 0:
                messagebox.showerror("Error", "Enter a and b seperated by comma")
            else:
                key = key_str
        else:
            raise ValueError("Unsupported cipher type.")
        return key
    except ValueError:
        error_message = "Invalid key value."
        print(error_message)  # Print error message in the console
        messagebox.showerror("Error", error_message)  # Show error message in a pop-up window
def GetCiphertext():
    plaintext = entry_3.get()
    if not plaintext.strip():
        error_message = "Please enter some text."
        print(error_message)
        messagebox.showerror("Error", error_message)
        return None
    elif not ''.join(c for c in plaintext if c not in (' ', '\n', '\r')).isalpha():
        error_message = "Please enter only alphabetic characters (excluding spaces and end-of-line characters)."
        print(error_message)
        messagebox.showerror("Error", error_message)
        return None
    elif CipherAlgorithm == "playfair" and (len(plaintext)&1):
        error_message = "Cipher can't be odd"
        print(error_message)
        messagebox.showerror("Error", error_message)
    else:
        return plaintext
    return entry_3.get()
######################################################################################################
def ceaser_encryption():
    plainText = GetPlaintext()
    Key =  GetKey()
    ciphertext = Ceaser.ceaser_encryption(plainText, Key )
    entry_3.delete(0,"end")
    entry_3.insert(0,ciphertext)
def ceaser_decryption():
    cipherText = GetCiphertext()
    Key =  GetKey()
    plainText = Ceaser.ceaser_decryption(cipherText,Key)
    entry_1.delete(0, "end")
    entry_1.insert(0, plainText)
####################################################################################################
def Row_col_encryption():
    plainText = GetPlaintext()
    Key =  GetKey()
    ciphertext = Row_Col.columnar_transposition_encrypt(plainText,Key)
    entry_3.delete(0, "end")
    entry_3.insert(0, ciphertext)
def Row_col_decryption():
    cipherText = GetCiphertext()
    Key =  GetKey()
    plainText = Row_Col.columnar_transposition_decrypt(cipherText,Key)
    entry_1.delete(0, "end")
    entry_1.insert(0, plainText)
#####################################################################################################
def Root13_encryption():
    plaintext = GetPlaintext()
    ciphertext =Rote_13.encrypt(plaintext)
    entry_3.delete(0, "end")
    entry_3.insert(0, ciphertext)
def Root13_decryption():
    ciphertext = GetCiphertext()
    plaintext =Rote_13.decrypt(ciphertext)
    entry_1.delete(0, "end")
    entry_1.insert(0, plaintext)
########################################################################################################
def playfair_encryption():
    plainText = GetPlaintext()
    Key =  GetKey()
    ciphertext = playfair.encrypt_playfair(plainText,Key)
    entry_3.delete(0, "end")
    entry_3.insert(0, ciphertext)
def playfair_decryption():
    cipherText = GetCiphertext()
    Key =  GetKey()
    plainText = playfair.decrypt_playfair(cipherText,Key)
    entry_1.delete(0, "end")
    entry_1.insert(0, plainText)
######################################################################################################
def Railfence_encryption():
    plainText = GetPlaintext()
    Key =  GetKey()
    ciphertext = Rail_Fence.rail_fence_encrypt(plainText,Key)
    entry_3.delete(0, "end")
    entry_3.insert(0, ciphertext)
def Railfence_decryption():
    cipherText = GetCiphertext()
    Key =  GetKey()
    plainText = Rail_Fence.rail_fence_decrypt(cipherText,Key)
    entry_1.delete(0, "end")
    entry_1.insert(0, plainText)
#####################################################################################################
def subistitution_encryption():
    plainText = GetPlaintext()
    Key = GetKey()
    ciphertext = substitution.encrypt(plainText,Key
                                      )
    entry_3.delete(0, "end")
    entry_3.insert(0, ciphertext)
def subistitution_decryption():
    cipherText = GetCiphertext()
    Key = GetKey()
    plainText = substitution.decrypt(cipherText,Key)
    entry_1.delete(0, "end")
    entry_1.insert(0, plainText)
######################################################################################################
def Affine_encryption():
    plainText = GetPlaintext()
    a , b = get_A_And_B(entry_2)
    ciphertext = Affine.encryption_affine_cipher(plainText, a , b )
    entry_3.delete(0,"end")
    entry_3.insert(0,ciphertext)
def Affine_decryption():
    cipherText = GetCiphertext()
    a , b = get_A_And_B(entry_2)
    plainText = Affine.decryption_affine_cipher(cipherText, a , b )
    entry_1.delete(0, "end")
    entry_1.insert(0, plainText)
##########################################################################################################
def vigenere_encryption():
    plainText = GetPlaintext()
    Key =  GetKey()
    ciphertext = vigenere.encryption_vigenere_cipher(plainText,Key)
    entry_3.delete(0, "end")
    entry_3.insert(0, ciphertext)
def vigenere_decryption():
    cipherText = GetCiphertext()
    Key =  GetKey()
    plainText = vigenere.decryption_vigenere_cipher(cipherText,Key)
    entry_1.delete(0, "end")
    entry_1.insert(0, plainText)
##########################################################################################################
def hill_encryption():
    plaintext = GetPlaintext()
    Key = GetKey()
    ciphertext = hill.encryptHill2x2(plaintext,Key)
    entry_3.delete(0, "end")
    entry_3.insert(0, ciphertext)
def hill_decryption():
    cipherText = GetCiphertext()
    Key = GetKey()
    plainText = hill.decryptHill2x2(cipherText,Key)
    entry_1.delete(0, "end")
    entry_1.insert(0, plainText)
##########################################################################################################
def rsa_encryption():
    plainText = GetPlaintext()
    a, b = get_A_And_B(entry_2)
    ciphertext = RSA.enc_rsa_algo(plainText,a,b)
    entry_3.delete(0, "end")
    entry_3.insert(0, ciphertext)
def rsa_decryption():
    cipherText = GetCiphertext()
    a , b = get_A_And_B(entry_2)
    plainText = RSA.dec_rsa_algo(cipherText,a,b)
    entry_1.delete(0, "end")
    entry_1.insert(0, plainText)
##########################################################################################################

window = Tk()

window.geometry("1385x820")
window.configure(bg = "#18181B")


canvas = Canvas(
    window,
    bg = "#18181B",
    height = 820,
    width = 1385,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    693.0,
    131.0,
    image=image_image_1
)

canvas.create_rectangle(
    103.0,
    290.0,
    810.0,
    665.0,
    fill="#18181B",
    outline="")

canvas.create_rectangle(
    852.0,
    290.0,
    1267.0,
    665.0,
    fill="#18181B",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("Encrypt.png"))
Encrypt = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: GetEncryptionAlgorithm(),
    background="#18181B",
    relief="flat"
)
Encrypt.place(
    x=691.0,
    y=354.0,
    width=102.0,
    height=41.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("img_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: download("Encrypt"),
    background="#18181B",
    relief="flat"
)
button_2.place(
    x=640.0,
    y=355.0,
    width=40.0,
    height=40.0
)

uploadencryptimage = PhotoImage(
    file=relative_to_assets("img_3.png"))
uploadencrypt = Button(
    image=uploadencryptimage,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_content("Encrypt"),
    background="#18181B",
    relief="flat"
)
uploadencrypt.place(
    x=590.0,
    y=355.0,
    width=40.0,
    height=40.0
)

downloaddecryptimage = PhotoImage(
    file=relative_to_assets("img_2.png"))
downloaddecrypt = Button(
    image=downloaddecryptimage,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: download("Decrypt"),
    background="#18181B",
    relief="flat"
)
downloaddecrypt.place(
    x=640.0,
    y=580.0,
    width=40.0,
    height=40.0
)

uploaddecryptimage = PhotoImage(
    file=relative_to_assets("img_3.png"))
uploaddecrypt = Button(
    image=uploaddecryptimage,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_content(("Decrypt")),
    background="#18181B",
    relief="flat"
)
uploaddecrypt.place(
    x=590.0,
    y=580.0,
    width=40.0,
    height=40.0
)

entry_bg_1 = canvas.create_image(
    379.0,
    376.5,
)
entry_1 = Entry(
    bd=0,
    bg="#27272A",
    fg="green",
    highlightthickness=0,
   font=( "Inter Semibold" , 20 * -1)
)
entry_1.place(
    x=133.0,
    y=354.0,
    width=450.0,
    height=43.0
)

canvas.create_text(
    129.0,
    322.0,
    anchor="nw",
    text="Plain Text",
    fill="#A1A1AA",
    font=("Inter SemiBold", 20 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    459.0,
    488.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#27272A",
    fg="green",
    highlightthickness=0,
    font=("Inter Semibold", 20 * -1)
)
entry_2.place(
    x=133.0,
    y=466.0,
    width=652.0,
    height=43.0
)

canvas.create_text(
    129.0,
    434.0,
    anchor="nw",
    text="Key",
    fill="#A1A1AA",
    font=("Inter SemiBold", 20 * -1)
)

button_image_3 = PhotoImage(
    file=relative_to_assets("Decrypt.png"))
Decrypt = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    background="#18181B",
    command=lambda: GetDecryptionAlgorithm(),
    relief="flat"
)
Decrypt.place(
    x=691.0,
    y=579.0,
    width=102.0,
    height=41.0
)

entry_3 = Entry(
    bd=0,
    bg="#27272A",
    fg="green",
    highlightthickness=0,
    font=("Inter Semibold", 20 * -1)
)
entry_3.place(
    x=133.0,
    y=579.0,
    width=450.0,
    height=43.0
)

canvas.create_text(
    129.0,
    547.0,
    anchor="nw",
    text="Ciphered Text",
    fill="#A1A1AA",
    font=("Inter SemiBold", 20 * -1)
)

canvas.create_text(
    883.0,
    322.0,
    anchor="nw",
    text="Algorithm",
    fill="#A1A1AA",
    font=("Inter SemiBold", 20 * -1)
)

button_image_5 = PhotoImage(
    file=relative_to_assets("ceaser.png"))
ceaser = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    background="#18181B",
    command=lambda: setAlgorithm("Ceaser"),
    relief="flat"
)
ceaser.place(
    x=883.0,
    y=367.0,
    width=74.0,
    height=28.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("Row_col.png"))
Row_col = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    background="#18181B",
    command=lambda: setAlgorithm("Row-Col"),
    relief="flat"
)
Row_col.place(
    x=976.0,
    y=367.0,
    width=74.0,
    height=28.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("Root13.png"))
Root13 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    background="#18181B",
    command=lambda: setAlgorithm("Root13"),
    relief="flat"
)
Root13.place(
    x=1069.0,
    y=367.0,
    width=74.0,
    height=28.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("playfair.png"))
pplayfair = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    background="#18181B",
    command=lambda:setAlgorithm("playfair"),
    relief="flat"
)
pplayfair.place(
    x=1162.0,
    y=367.0,
    width=74.0,
    height=28.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("realfence.png"))
realfence = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    background="#18181B",
    command=lambda: setAlgorithm("realfence"),
    relief="flat"
)
realfence.place(
    x=885.0,
    y=407.0,
    width=74.0,
    height=28.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("subistitution.png"))
subistitution = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    background="#18181B",
    command=lambda:setAlgorithm("subistitution"),
    relief="flat"
)
subistitution.place(
    x=975.0,
    y=407.0,
    width=87.0,
    height=28.0
)

button_image_11 = PhotoImage(
    file=relative_to_assets("Affine.png"))
affine = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    background="#18181B",
    command=lambda: setAlgorithm("Affine"),
    relief="flat"
)
affine.place(
    x=1082.0,
    y=407.0,
    width=51.0,
    height=28.0
)

button_image_12 = PhotoImage(
    file=relative_to_assets("Hill.png"))
Hillbutton = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    background="#18181B",
    command=lambda: setAlgorithm("Hill"),
    relief="flat"
)
Hillbutton.place(
    x=892.0,
    y=447.0,
    width=51.0,
    height=28.0
)

RSA_image = PhotoImage(
    file=relative_to_assets("RSA.png"))
RSAButton = Button(
    image=RSA_image,
    borderwidth=0,
    highlightthickness=0,
    background="#18181B",
    command=lambda: setAlgorithm("RSA"),
    relief="flat"
)
RSAButton.place(
    x=982.0,
    y=447.0,
    width=51.0,
    height=28.0
)

button_image_13 = PhotoImage(
    file=relative_to_assets("vigenere.png"))
vvigenere = Button(
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    background="#18181B",
    command=lambda: setAlgorithm("vigenere"),
    relief="flat"
)
vvigenere.place(
    x=1160.0,
    y=407.0,
    width=75.0,
    height=28.0
)
window.resizable(False, False)
window.mainloop()
