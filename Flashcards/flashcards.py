from tkinter import *
from csv import *

BACKGROUND_COLOR = "#B1DDC6"

#----------------------- FUNCTIONS -----------------------#
def get_new_word():
    global row_num
    with open('.\\Flashcards\\french_words.csv', newline='') as csvfile:
        word_reader = reader(csvfile, delimiter=',')
        # canvas.itemconfig(canvas_word_text, text=f"{wtf}")
# TODO: Figure out how to increment by one word in the list when you press the button
#----------------------- UI SETUP -----------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady= 50, bg=BACKGROUND_COLOR)

canvas = Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file=".\\Flashcards\\card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas_title_text = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
canvas_word_text = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(column=0, columnspan=2, row=0)

correct_img = PhotoImage(file=".\\Flashcards\\right.png")
correct_button = Button(image=correct_img, highlightthickness=0, relief="flat", command=get_new_word)
correct_button.grid(column=1, row=1)

wrong_img = PhotoImage(file=".\\Flashcards\\wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, relief="flat")
wrong_button.grid(column=0, row=1)

window.mainloop()