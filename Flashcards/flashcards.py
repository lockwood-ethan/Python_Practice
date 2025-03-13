from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv(".\\Flashcards\\words_to_learn.csv")
    to_learn = data.to_dict(orient="records")
except FileNotFoundError:
    data = pandas.read_csv(".\\Flashcards\\french_words.csv")
    to_learn = data.to_dict(orient="records")

current_card = {}

#----------------------- FUNCTIONS -----------------------#
def remove_known_word():
    global current_card, to_learn
    to_learn.remove(current_card)
    data = pandas.DataFrame.from_records(to_learn)
    data.to_csv(path_or_buf=".\\Flashcards\\words_to_learn.csv", mode="w", index=False)
    next_card()

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(canvas_title_text, text="French", fill="black")
    canvas.itemconfig(canvas_word_text, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)
    
def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(canvas_title_text, text="English", fill="white")
    canvas.itemconfig(canvas_word_text, text=current_card["English"], fill="white")

#----------------------- UI SETUP -----------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady= 50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file=".\\Flashcards\\card_front.png")
card_back_img = PhotoImage(file=".\\Flashcards\\card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)
canvas_title_text = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
canvas_word_text = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, columnspan=2, row=0)

correct_img = PhotoImage(file=".\\Flashcards\\right.png")
correct_button = Button(image=correct_img, highlightthickness=0, relief="flat", command=remove_known_word)
correct_button.grid(column=1, row=1)

wrong_img = PhotoImage(file=".\\Flashcards\\wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, relief="flat", command=next_card)
wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()