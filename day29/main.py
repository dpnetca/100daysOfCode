#!/usr/bin/env python

import tkinter as tk
from tkinter import messagebox
from random import randint, choice, shuffle

# import pyperclip

from components import letters, numbers, symbols

FONT = ("Arial", 10, "normal")
DEFAULT_USER = "fake@dpnet.ca"


# ---------------------------- PASSWORD GENERATOR -------------------- #
def generate_password():
    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list.extend([choice(symbols) for _ in range(randint(2, 4))])
    password_list.extend([choice(numbers) for _ in range(randint(2, 4))])
    shuffle(password_list)
    password = "".join(password_list)

    # Pyperclip does now work in my test environment:
    # (Ubuntu 20.04 in WSL2 w/ XFCE via xRDP)
    # [Errno 2] No such file or directory: 'clip.exe'
    # pyperclip.copy(password)

    password_input.delete(0, tk.END)
    password_input.insert(tk.END, password)


# ---------------------------- SAVE PASSWORD ------------------------- #
def save_password():
    site = site_input.get()
    email = user_input.get()
    password = password_input.get()

    if site == "" or email == "" or password == "":
        messagebox.showerror(
            title="Oops", message="Please don't leave any fields empty!"
        )
        return None

    is_ok = messagebox.askokcancel(
        title=site,
        message=(
            f"Details entered:\n\n"
            f"Email: {email}\n"
            f"Password: {password}\n\n"
            "Ok to save?"
        ),
    )
    if is_ok:
        with open("data.txt", "a") as f:
            f.write(f"{site} | {email} | {password}\n")

        site_input.delete(0, tk.END)
        password_input.delete(0, tk.END)
        user_input.delete(0, tk.END)
        user_input.insert(tk.END, DEFAULT_USER)


# ---------------------------- UI SETUP ------------------------------ #

window = tk.Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")


# ROW 0
logo_png = tk.PhotoImage(file="logo.png")
canvas = tk.Canvas(height=200, width=200)
canvas.create_image(100, 100, image=logo_png)
canvas.grid(row=0, column=0, columnspan=3)

# ROW 1
site_label = tk.Label(text="Website:")
site_label.grid(row=1, column=0)

site_input = tk.Entry(width=35)
site_input.grid(row=1, column=1, columnspan=2)
site_input.focus()

# ROW 2
user_label = tk.Label(text="Emai/Username:")
user_label.grid(row=2, column=0)

user_input = tk.Entry(width=35)
user_input.grid(row=2, column=1, columnspan=2)
user_input.insert(tk.END, DEFAULT_USER)

# ROW 3
password_label = tk.Label(text="Password:")
password_label.grid(row=3, column=0)

password_input = tk.Entry(width=18)
password_input.grid(row=3, column=1)

generate_button = tk.Button(
    text="Generate Password", command=generate_password, padx=2, pady=2
)
generate_button.grid(row=3, column=2)

# ROW 4
add_button = tk.Button(
    text="Add", command=save_password, width=35, padx=2, pady=2
)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
