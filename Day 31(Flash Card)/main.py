import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
FONT = ("Ariel", 30, "italic")
BOLD_FONT = ("Ariel", 30, "bold")
timer = None


word = pandas.read_csv("./data/french_words.csv")
word = pandas.DataFrame(word).to_dict(orient="records")
word_to_learn = word
window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.minsize(height=526, width=800)
card_back = PhotoImage(file="./images/card_back.png")
card_front = PhotoImage(file="./images/card_front.png")
right_ans = PhotoImage(file="./images/right.png")
wrong_ans = PhotoImage(file="./images/wrong.png")


# ==============================================================================================
# FUNCTIONS
# ==============================================================================================
def flip(card):
    canvas.itemconfig(title, text="ENGLISH", fill="white")
    canvas.itemconfig(word_card, text=card['English'], fill="white")
    canvas.itemconfig(front_img, image=card_back)
    window.after_cancel(timer)

def rand_word():
    global timer
    card = random.choice(word_to_learn)
    canvas.itemconfig(title, text="FRENCH", fill="black")
    canvas.itemconfig(word_card, text=card['French'], fill='black')
    canvas.itemconfig(front_img, image=card_front)
    timer = window.after(3000, flip, card)
    if right_ans:
        word_to_learn.remove(card)
    file = pandas.DataFrame(word_to_learn)
    file.to_csv("word_to_learn.csv")



# ==============================================================================================
# CANVAS
# ==============================================================================================


canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = canvas.create_image(410, 270, image=card_front)
title = canvas.create_text(400, 150, text="Title", font=FONT)
word_card = canvas.create_text(400, 263, text="Word", font=BOLD_FONT)
canvas.grid(row=0, column=0, columnspan=2)

# ==============================================================================================
# BUTTONS
# ==============================================================================================

right_but = Button(image=right_ans, highlightthickness=0, bg=BACKGROUND_COLOR, command=rand_word)
right_but.grid(row=1, column=0)
wrong_but = Button(image=wrong_ans, highlightthickness=0, bg=BACKGROUND_COLOR, command=rand_word)
wrong_but.grid(row=1, column=1)


# ==============================================================================================
# LABELS
# ==============================================================================================








window.mainloop()