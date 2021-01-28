#!/usr/bin/env python
import tkinter


# Button
def button_clicked():
    # print("I got clicked")
    # my_label["text"] = "Button got Clicked"
    my_label.config(text=user_input.get())


window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))

# by default back centers at top of screen
# https://docs.python.org/3/library/tkinter.html#the-packer
# http://tcl.tk/man/tcl8.6/TkCmd/pack.htm

# my_label["text"] = "New Text"
# my_label.config(text="newer text")
# my_label.pack()
# my_label.place(x=100, y=200)
my_label.config(padx=50, pady=50)
my_label.grid(column=0, row=0)


button = tkinter.Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

new_button = tkinter.Button(text="New Click Me", command=button_clicked)
new_button.grid(column=2, row=0)

# Entry
user_input = tkinter.Entry(width=10)
# user_input.pack()
user_input.grid(column=3, row=2)

window.mainloop()
