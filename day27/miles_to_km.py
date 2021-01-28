#!/usr/bin/env python

import tkinter


def calculate():
    miles = float(miles_input.get())
    km = round(miles * 1.609344, 2)
    km_amount_label.config(text=km)


# Initiate Window
window = tkinter.Tk()
window.title("Miles to Km")
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)

# define input box
miles_input = tkinter.Entry(width=10)
miles_input.insert(tkinter.END, "0")
miles_input.focus()
miles_input.grid(column=1, row=0)

# miles label
miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

# is equal to...
is_equal_label = tkinter.Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

# display calculated km
km_amount_label = tkinter.Label(text="0")
km_amount_label.grid(column=1, row=1)

# km label
km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)

# calculate button
calculate_button = tkinter.Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)

window.mainloop()
