from tkinter import *

def conversion_math():
    miles_num = user_input.get()
    km_num = float(miles_num) * 1.609344
    num_km_label.config(text=f"{km_num:.2f}")

window = Tk()
window.title("Mile to Km Converter")
# window.minsize(height=100, width=300)

user_input = Entry(width=15)
user_input.insert(0, "0")
user_input.grid(column=1, row=0, padx=10, pady=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0, padx=10, pady=0)

equal_to_label = Label(text="is equal to")
equal_to_label.grid(column=0, row=1, padx=10, pady=0)

num_km_label = Label(text="0")
num_km_label.grid(column=1, row=1, padx=10, pady=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1, padx=10, pady=0)

calc_button = Button(text="Calculate", command=conversion_math)
calc_button.grid(column=1, row=2, padx=10, pady=0)

window.mainloop()