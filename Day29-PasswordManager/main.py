import tkinter
from tkinter import messagebox
import random
import pyperclip


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

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty!")
        return

    is_ok = messagebox.askyesno(title=website, message=f"These are the details entered by you: \nWebsite: {website}\n"
                                                       f"Email: {email}\nPassword: {password}")
    if is_ok:
        f = open("data.txt", "a")
        f.write(f"{website} | {email} | {password}\n")
        f.close()
        website_entry.delete(0, 'end')
        pwd_entry.delete(0, 'end')
        website_entry.focus()
        messagebox.showinfo(title="Success", message="Your message has been saved!")


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

website_entry = tkinter.Entry(width=36)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

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
