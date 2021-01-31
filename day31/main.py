#!/usr/bin/env python

import tkinter as tk
import random
import pandas as pd


BACKGROUND_COLOR = "#B1DDC6"
FROM_LANGUAGE = "French"
TO_LANGUAGE = "English"
GUESS_TIME = 3

flip_timer = 0
word = {}


def display_card():
    """randomly choose a card, display the card, then after guess time
    expired call function to display the answer
    """
    global flip_timer
    global word
    word = random.choice(word_data)
    card_canvas.itemconfig(card_image, image=card_front)
    card_canvas.itemconfig(card_language, text=FROM_LANGUAGE, fill="black")
    card_canvas.itemconfig(card_word, text=word[FROM_LANGUAGE], fill="black")
    flip_timer = window.after(GUESS_TIME * 1000, display_answer)


def display_answer():
    """display the answer"""
    card_canvas.itemconfig(card_image, image=card_back)
    card_canvas.itemconfig(card_language, text=TO_LANGUAGE, fill="white")
    card_canvas.itemconfig(card_word, text=word[TO_LANGUAGE], fill="white")


def wrong_button_press():
    """cancel the card flip timer if it is running and displat new card"""
    window.after_cancel(flip_timer)
    display_card()


def right_button_press():
    """cancel card flip timer if it is running, remove the word from the
    list and save to file, and display next word
    """
    window.after_cancel(flip_timer)
    word_data.remove(word)
    to_learn_df = pd.DataFrame(word_data)
    to_learn_df.to_csv("./data/french_words_to_learn.csv", index=False)
    display_card()


# Pandas overkill for this, could use csv.dictreader, but pandas is assignment
try:
    df = pd.read_csv("./data/french_words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("./data/french_words.csv")

word_data = df.to_dict(orient="records")


# --- SETUP UI --- #

# create window
window = tk.Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# define Images tro be used
card_back = tk.PhotoImage(file="./images/card_back.png")
card_front = tk.PhotoImage(file="./images/card_front.png")
right_png = tk.PhotoImage(file="./images/right.png")
wrong_png = tk.PhotoImage(file="./images/wrong.png")

# create Canvas
card_canvas = tk.Canvas(
    width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0
)
card_image = card_canvas.create_image(400, 263, image=card_front)
card_language = card_canvas.create_text(
    400, 150, text="title", font=("Arial", 40, "italic")
)
card_word = card_canvas.create_text(
    400, 263, text="word", font=("Arial", 60, "bold")
)
card_canvas.grid(row=0, column=0, columnspan=2)

# create right / wrong buttons
wrong_button = tk.Button(
    image=wrong_png,
    highlightthickness=0,
    bd=0,
    bg=BACKGROUND_COLOR,
    command=wrong_button_press,
)
wrong_button.grid(row=1, column=0)
right_button = tk.Button(
    image=right_png,
    highlightthickness=0,
    bd=0,
    bg=BACKGROUND_COLOR,
    command=right_button_press,
)
right_button.grid(row=1, column=1)

# display first card
display_card()

window.mainloop()
