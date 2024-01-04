import tkinter as tk
import random # For copying to clipboard

# Character sets for password generation
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_+-=[]{}|;':\",.<>/?"

def generate_password():
    password_length = int(length_entry.get())
    characters = ""
    if letters_var.get():
        characters += letters
    if numbers_var.get():
        characters += numbers
    if symbols_var.get():
        characters += symbols

    password = "".join(random.sample(characters, password_length))
    password_label.config(text="Generated password: " + password)
    pyperclip.copy(password)  # Copy password to clipboard

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create labels and entries for password length and character choices
length_label = tk.Label(root, text="Password length:")
length_label.grid(row=0, column=0)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1)

letters_var = tk.IntVar()
letters_checkbox = tk.Checkbutton(root, text="Include letters", variable=letters_var)
letters_checkbox.grid(row=1, column=0)

numbers_var = tk.IntVar()
numbers_checkbox = tk.Checkbutton(root, text="Include numbers", variable=numbers_var)
numbers_checkbox.grid(row=2, column=0)

symbols_var = tk.IntVar()
symbols_checkbox = tk.Checkbutton(root, text="Include symbols", variable=symbols_var)
symbols_checkbox.grid(row=3, column=0)

# Create a button to generate the password
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=4, column=0, columnspan=2)

# Create a label to display the generated password
password_label = tk.Label(root, text="")
password_label.grid(row=5, column=0, columnspan=2)

# Run the main loop
root.mainloop()