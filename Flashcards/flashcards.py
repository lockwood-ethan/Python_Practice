from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

#----------------------- FUNCTIONS -----------------------#

#----------------------- UI SETUP -----------------------#
window = Tk()
window.title("Flashy")
window.config(padx=100, pady= 50, bg=BACKGROUND_COLOR)
window.geometry('1000x800')

canvas = Canvas(window, width=800, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file=".\\Flashcards\\card_front.png")
canvas.create_image(400, 300, image=card_front_img)
canvas_title_text = canvas.create_text(400, 175, text="Title", font=("Arial", 35, "italic"))
canvas_word_text = canvas.create_text(400, 300, text="Word", font=("Arial", 50, "bold"))
canvas.grid(column=0, columnspan=2, row=0)

correct_img = PhotoImage(file=".\\Flashcards\\right.png")
correct_button = Button(image=correct_img, highlightthickness=0, relief="flat")
correct_button.grid(column=1, row=1)

wrong_img = PhotoImage(file=".\\Flashcards\\wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, relief="flat")
wrong_button.grid(column=0, row=1)

window.mainloop()