import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        use_upper = upper_var.get()
        use_lower = lower_var.get()
        use_digits = digits_var.get()
        use_special = special_var.get()

        if length <= 0:
            messagebox.showerror("Error", "Password length must be greater than 0.")
            return

        char_pool = ''
        password = []

        if use_upper:
            char_pool += string.ascii_uppercase
            password.append(random.choice(string.ascii_uppercase))
        if use_lower:
            char_pool += string.ascii_lowercase
            password.append(random.choice(string.ascii_lowercase))
        if use_digits:
            char_pool += string.digits
            password.append(random.choice(string.digits))
        if use_special:
            char_pool += string.punctuation
            password.append(random.choice(string.punctuation))

        if not char_pool:
            messagebox.showerror("Error", "Select at least one character type.")
            return

        # Fill the rest of the password
        while len(password) < length:
            password.append(random.choice(char_pool))

        random.shuffle(password)
        result_entry.delete(0, tk.END)
        result_entry.insert(0, ''.join(password))
    except ValueError:
        messagebox.showerror("Error", "Invalid password length.")

# Create GUI window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.resizable(False, False)

# Widgets
tk.Label(root, text="Password Length:", font=('Arial', 12)).pack(pady=5)
length_entry = tk.Entry(root, width=10, font=('Arial', 12))
length_entry.pack()

upper_var = tk.BooleanVar()
lower_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
special_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Uppercase Letters", variable=upper_var).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Lowercase Letters", variable=lower_var).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Numbers", variable=digits_var).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Special Characters", variable=special_var).pack(anchor='w', padx=20)

tk.Button(root, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white", font=('Arial', 12)).pack(pady=15)

tk.Label(root, text="Generated Password:", font=('Arial', 12)).pack()
result_entry = tk.Entry(root, width=30, font=('Arial', 12))
result_entry.pack(pady=5)

# Run the GUI
root.mainloop()
