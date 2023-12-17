from tkinter import *
import customtkinter as ctk
import secrets
import string
import pyperclip

# Creating window
root = ctk.CTk()
root.title("Crypt Warden")
root.geometry("800x500")

# Crypt Warden Icon relative path, icon needs to be in same workspace or set absolute path
try:
    root.iconbitmap("cwardenico.ico")
except: TclError

# Disable resizing window
root.resizable(width=False, height=False)

# Darkmode default off 
switch_theme_var = ctk.StringVar(value="off")

# Darkmode switch function
def switch_event():
    current_mode = switch_theme_var.get()
    print("switch toggled, dark mode:", current_mode)
    
    if current_mode == "on":
        ctk.set_appearance_mode("dark")
    else:
        ctk.set_appearance_mode("light")

# Switch to set darkmode on/off using switch_theme_var 
switch_theme = ctk.CTkSwitch(
    master=root, text="Darkmode", command=switch_event,
    variable=switch_theme_var, onvalue="on", offvalue="off"
)
switch_theme.place(x=50, y=400)

# Title Label
label = ctk.CTkLabel(root, text="Crypt Warden", font=('Arial', 22))
label.pack(pady=20)  

# Quit Button
btn_quit = ctk.CTkButton(root, text="Quit", command=root.destroy)
btn_quit.place(x=600, y=400)

# Label for slider
length_label = ctk.CTkLabel(root, text="Selected password length: 20")
length_label.place(x=300, y=350)

# Function for slider length changing value dynamically
def slider_length(value):
    length_label.configure(text=f"Selected password length: {int(value)}")    
    update_password()

# Slider setup enabling password from 6 up to 36 characters
slider_quant = ctk.CTkSlider(master=root, from_=4, to=36, command=slider_length)
slider_quant.place(x=300, y=300)
slider_quant.configure(height=20)

# Update password and get on/off value from each variable, 
def update_password():
    length = int(slider_quant.get())
    include_numbers = box_num_var.get()
    include_symbols = box_sym_var.get()
    include_lowercase = box_low_var.get()
    include_uppercase = box_upp_var.get()

    characters = ""
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase

    try:
        # Randomly generates charachter sets into string
        password = ''.join(secrets.choice(characters) for i in range(length))
        password_label.configure(text=f"{password}")
        return password
    # Index error will occur when no box is checked due to empty password
    except: IndexError

# Variables that keep track of checkbox states (True/False)
box_num_var = ctk.BooleanVar()
box_sym_var = ctk.BooleanVar()
box_low_var = ctk.BooleanVar()
box_upp_var = ctk.BooleanVar()

# Label for generated password
password_label = ctk.CTkLabel(root,text="",font=('Arial', 25))
password_label.pack()

generated_pw_label = ctk.CTkLabel(root,text="Generated password" )
generated_pw_label.pack(pady=20)

# Checkboxes for character sets
box_low = ctk.CTkCheckBox(master=root, text="Include Lowercase", variable=box_low_var, command=update_password)
box_low.place(x=600, y=250)

box_num = ctk.CTkCheckBox(master=root, text="Include Numbers", variable=box_num_var, command=update_password)
box_num.place(x=600, y=150)

box_sym = ctk.CTkCheckBox(master=root, text="Include Symbols", variable=box_sym_var, command=update_password)
box_sym.place(x=600, y=200)

box_upp = ctk.CTkCheckBox(master=root, text="Include Uppercase", variable=box_upp_var, command=update_password)
box_upp.place(x=600, y=300)


# Function to copy password to clipboard
def pw_copy():
    password = update_password()
    pyperclip.copy(password)
    print("copied password to clipboard")

# Button to copy password
btn_copy = ctk.CTkButton(master=root, text='Copy Password', command=pw_copy)
btn_copy.place(x=330, y=250)

root.mainloop()