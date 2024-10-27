import tkinter as tk
from tkinter import ttk, messagebox

def caesar_cipher(text, key, method):
    edited_code = []
    for char in text:
        if method == "decrypt":
            c = ord(char) - key
        elif method == "crypt":
            c = ord(char) + key
        edited_code.append(chr(c))
    return "".join(edited_code)

def process_cipher(method):
    your_caesar_code = input_text.get()
    try:
        caesar_key = int(key_input.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer key.")
        return

    result = caesar_cipher(your_caesar_code, caesar_key, method)
    result_label.config(text=f"Result: {result}")
    copy_button.pack(pady=5)

def copy_to_clipboard():
    result = result_label.cget("text").replace("Result: ", "")
    root.clipboard_clear()
    root.clipboard_append(result)
    messagebox.showinfo("Copied", "Result copied to clipboard!")

root = tk.Tk()
root.title("Caesar Cipher")
root.configure(bg="#2D2D2D")

style = ttk.Style()
style.configure("TLabel", font=("Arial", 12), background="#2D2D2D", foreground="#EAEAEA")
style.configure("TEntry", font=("Arial", 12), padding=5)
style.configure("TButton", font=("Arial", 12, 'bold'), padding=10, background="#007BFF", borderwidth=1)
style.map("TButton", background=[('active', '#007BFF'), ('!active', '#007BFF')])

input_label = ttk.Label(root, text="Enter your Caesar code:")
input_label.pack(pady=(20, 5))
input_text = ttk.Entry(root, width=40)
input_text.pack(pady=(0, 15))

key_label = ttk.Label(root, text="Enter key:")
key_label.pack(pady=(0, 5))
key_input = ttk.Entry(root, width=10)
key_input.pack(pady=(0, 15))

crypt_button = ttk.Button(root, text="Crypt", command=lambda: process_cipher("crypt"))
crypt_button.pack(pady=5)

decrypt_button = ttk.Button(root, text="Decrypt", command=lambda: process_cipher("decrypt"))
decrypt_button.pack(pady=(0, 15))

copy_button = ttk.Button(root, text="Copy Result", command=copy_to_clipboard)
copy_button.pack(pady=5)
copy_button.pack_forget()

result_label = ttk.Label(root, text="Result: ", font=("Arial", 12, 'bold'))
result_label.pack(pady=(20, 5))

root.mainloop()
