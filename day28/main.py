#!/usr/bin/env python

import tkinter

# ---------------------------- CONSTANTS ---------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"
reps = 0
timer = None


# --------------- TIMER RESET -------------------------- #
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")


# ---------------------------- TIMER MECHANISM ---------------------- #
def start_timer():
    global reps
    reps += 1
    if reps == 8:
        timer_label.config(text="Break", fg=RED)
        countdown(LONG_BREAK_MIN * 60)
        reps = 0
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        countdown(SHORT_BREAK_MIN * 60)
    else:
        timer_label.config(text="Work", fg=GREEN)
        countdown(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------ #
def countdown(count):
    global timer
    minutes = count // 60
    seconds = count % 60
    canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        checks = reps // 2
        check_label.config(text=CHECK_MARK * checks)


# ---------------------------- UI SETUP ----------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


tomato_png = tkinter.PhotoImage(file="tomato.png")

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_png)
timer_text = canvas.create_text(
    100, 140, text="00:00", fill="white", font=(FONT_NAME, 25, "bold")
)
canvas.grid(column=1, row=1)

timer_label = tkinter.Label(
    text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold")
)
timer_label.grid(column=1, row=0)


start_button = tkinter.Button(
    text="start", command=start_timer, bg="white", highlightthickness=0
)
start_button.grid(column=0, row=3)

reset_button = tkinter.Button(
    text="reset", command=reset_timer, bg="white", highlightthickness=0
)
reset_button.grid(column=3, row=3)

check_label = tkinter.Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 24, "bold"))
check_label.grid(column=1, row=4)

window.mainloop()
