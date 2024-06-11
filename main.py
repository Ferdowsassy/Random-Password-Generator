import tkinter as tk
import random
import string


# Create the main window
root = tk.Tk()
# Set the title of the window
root.title("Random Password Generator")
# Set the dimensions of the window
root.geometry("400x300")


# Title label
label = tk.Label(root, text="Password Generator")
label.config(font=('Helvetica', 14))
label.pack(pady=10)

# Password length label and entry
label_length = tk.Label(root, text="Password Length:")
label_length.pack(pady=5)

entry_length = tk.Entry(root)
entry_length.pack(pady=5)

# Options for including characters
var_uppercase = tk.BooleanVar()
var_numbers = tk.BooleanVar()
var_special = tk.BooleanVar()

checkbox_uppercase = tk.Checkbutton(
    root, text='Include Uppercase Letters', variable=var_uppercase
)
checkbox_uppercase.pack(pady=2)

checkbox_numbers =tk.Checkbutton(
    root, text='Include Numbers', variable=var_numbers
)
checkbox_numbers.pack(pady=2)

checkbox_special = tk.Checkbutton(
    root, text='Include Special Characters', variable=var_special
)
checkbox_special.pack(pady=2)

# Entry to display the generated password
entry_password = tk.Entry(root, width=30)
entry_password.pack(pady=5)

# Function to generate the password
def generate_password():
    length = int(entry_length.get())
    characters = string.ascii_lowercase
    if var_uppercase.get():
        characters += string.ascii_uppercase
    if var_numbers.get():
        characters += string.digits
    if var_special.get():
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)


# Generate button
generate_button = tk.Button(
    root, text="Generate Password", command=generate_password
)
generate_button.pack(pady=20)



# Run the main loop
root.mainloop()
