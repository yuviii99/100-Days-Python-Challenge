import tkinter
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter = random.randint(8, 10)
    number = random.randint(2, 4)
    symbol = random.randint(2, 5)

    password_letters = [random.choice(letters) for _ in range(letter)]
    password_numbers = [random.choice(numbers) for _ in range(number)]
    password_symbols = [random.choice(symbols) for _ in range(symbol)]
    final_password = password_symbols + password_letters + password_numbers
    random.shuffle(final_password)
    pwd = "".join(final_password)
    pyperclip.copy(pwd)
    pwd_entry.delete(0, 'end')
    pwd_entry.insert(0, pwd)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_entry.get()
    email = email_entry.get()
    password = pwd_entry.get()
    new_data = {website: {
        "email": email,
        "password": password
    }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, 'end')
            pwd_entry.delete(0, 'end')
            website_entry.focus()
            messagebox.showinfo(title="Success", message="Your message has been saved!")


# ---------------------------- SEARCH ------------------------------- #
def search():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="File Not Found", message="No Data File Found")
    else:
        try:
            result = data[website]
        except KeyError:
            messagebox.showinfo(title="Error", message="No details for the website exists!")
        else:
            email = result["email"]
            password = result["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = tkinter.Canvas(height=200, width=200)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = tkinter.Label(text="Website:", font=("Arial", 12, "normal"))
website_label.grid(row=1, column=0)

website_entry = tkinter.Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

search_button = tkinter.Button(text="Search", width=15, command=search)
search_button.grid(row=1, column=2)

email_label = tkinter.Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_entry = tkinter.Entry(width=36)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "XYZ@email.com")

pwd_label = tkinter.Label(text="Password:")
pwd_label.grid(row=3, column=0)

pwd_entry = tkinter.Entry(width=21)
pwd_entry.grid(row=3, column=1)

pwd_button = tkinter.Button(text="Generate Password", command=generate_password)
pwd_button.grid(row=3, column=2)

add_button = tkinter.Button(text="Add", width=36, command=add_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
