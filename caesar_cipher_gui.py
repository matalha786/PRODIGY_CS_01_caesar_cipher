import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def encrypt_message():
    try:
        message = entry_message_encrypt.get()
        shift = int(entry_shift_encrypt.get())
        encrypted = caesar_cipher(message, shift, 'encrypt')
        entry_result_encrypt.delete(0, tk.END)
        entry_result_encrypt.insert(0, encrypted)
        global previous_encrypted
        previous_encrypted = encrypted
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer")

def decrypt_message():
    try:
        shift = int(entry_shift_decrypt.get())
        if previous_encrypted:
            decrypt_previous = messagebox.askyesno("Decrypt Previous", "Do you want to decrypt the previous encrypted message?")
            if decrypt_previous:
                decrypted = caesar_cipher(previous_encrypted, shift, 'decrypt')
                entry_result_decrypt.delete(0, tk.END)
                entry_result_decrypt.insert(0, decrypted)
            else:
                message = entry_message_decrypt.get()
                decrypted = caesar_cipher(message, shift, 'decrypt')
                entry_result_decrypt.delete(0, tk.END)
                entry_result_decrypt.insert(0, decrypted)
        else:
            message = entry_message_decrypt.get()
            decrypted = caesar_cipher(message, shift, 'decrypt')
            entry_result_decrypt.delete(0, tk.END)
            entry_result_decrypt.insert(0, decrypted)
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer")

def exit_program():
    root.destroy()

# Initialize the main window
root = tk.Tk()
root.title("Caesar Cipher Program")

# Configure grid to make the window scalable
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)
root.rowconfigure(6, weight=1)
root.rowconfigure(7, weight=1)
root.rowconfigure(8, weight=1)
root.rowconfigure(9, weight=1)

# Initialize the previous_encrypted variable
previous_encrypted = None

# Encryption section
label_message_encrypt = tk.Label(root, text="Enter your message to encrypt:")
label_message_encrypt.grid(row=0, column=0, sticky="nsew", padx=10, pady=5)

entry_message_encrypt = tk.Entry(root, width=50)
entry_message_encrypt.grid(row=0, column=1, sticky="nsew", padx=10, pady=5)

label_shift_encrypt = tk.Label(root, text="Enter shift value for encryption:")
label_shift_encrypt.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)

entry_shift_encrypt = tk.Entry(root, width=10)
entry_shift_encrypt.grid(row=1, column=1, sticky="nsew", padx=10, pady=5)

button_encrypt = tk.Button(root, text="Encrypt", command=encrypt_message)
button_encrypt.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=10, pady=5)

label_result_encrypt = tk.Label(root, text="Encrypted Result:")
label_result_encrypt.grid(row=3, column=0, sticky="nsew", padx=10, pady=5)

entry_result_encrypt = tk.Entry(root, width=50)
entry_result_encrypt.grid(row=3, column=1, sticky="nsew", padx=10, pady=5)

# Decryption section
label_message_decrypt = tk.Label(root, text="Enter your message to decrypt:")
label_message_decrypt.grid(row=4, column=0, sticky="nsew", padx=10, pady=5)

entry_message_decrypt = tk.Entry(root, width=50)
entry_message_decrypt.grid(row=4, column=1, sticky="nsew", padx=10, pady=5)

label_shift_decrypt = tk.Label(root, text="Enter shift value for decryption:")
label_shift_decrypt.grid(row=5, column=0, sticky="nsew", padx=10, pady=5)

entry_shift_decrypt = tk.Entry(root, width=10)
entry_shift_decrypt.grid(row=5, column=1, sticky="nsew", padx=10, pady=5)

button_decrypt = tk.Button(root, text="Decrypt", command=decrypt_message)
button_decrypt.grid(row=6, column=0, columnspan=2, sticky="nsew", padx=10, pady=5)

label_result_decrypt = tk.Label(root, text="Decrypted Result:")
label_result_decrypt.grid(row=7, column=0, sticky="nsew", padx=10, pady=5)

entry_result_decrypt = tk.Entry(root, width=50)
entry_result_decrypt.grid(row=7, column=1, sticky="nsew", padx=10, pady=5)

# Exit button
button_exit = tk.Button(root, text="Exit", command=exit_program)
button_exit.grid(row=8, column=0, columnspan=2, sticky="nsew", padx=10, pady=5)

# Run the main loop
root.mainloop()
