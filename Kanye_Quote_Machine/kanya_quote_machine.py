import requests
from tkinter import *

#-------------------- API CALL --------------------#

def get_kanye_quote():
    response = requests.get('https://api.kanye.rest')
    response.raise_for_status
    data = response.json()
    kanye_quote = data['quote']
    canvas.itemconfig(kanye_text, text=kanye_quote)

#-------------------- UI SETUP --------------------#

window = Tk()
window.title("Kanye Says...")
window.config(padx=25, pady=25)

canvas = Canvas(width=350, height=475, highlightthickness=0)
background_image = PhotoImage(file=".\\Kanye_Quote_Machine\\background.png")
canvas.create_image(175, 225, image=background_image)
kanye_text = canvas.create_text(175, 215, width=190, text='', fill='white', font=("Arial", 20, "bold"))
canvas.grid(column=0, row=0)

kanye_image = PhotoImage(file=".\\Kanye_Quote_Machine\\kanye.png")
kanye_button = Button(image=kanye_image, command=get_kanye_quote)
kanye_button.grid(column=0, row=1)

window.mainloop()
