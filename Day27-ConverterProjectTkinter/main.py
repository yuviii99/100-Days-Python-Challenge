from tkinter import *


def calculate():
    kms = float(mile_entry.get())
    kms *= 1.6
    kms = round(kms)
    km_label.config(text=f"{kms}")


window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=300, height=150)
window.config(padx=40, pady=35)

# Entry for miles
mile_entry = Entry(width=7)
mile_entry.grid(row=0, column=1)

# Label for miles
mile_label = Label(text="miles")
mile_label.grid(row=0, column=2)

# Label
disp_label = Label(text="is equal to")
disp_label.grid(row=1, column=0)

# KM Display
km_label = Label(text="0")
km_label.grid(row=1, column=1)

# KM Label
km_label1 = Label(text="km")
km_label1.grid(row=1, column=2)

# Button
button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)


window.mainloop()
