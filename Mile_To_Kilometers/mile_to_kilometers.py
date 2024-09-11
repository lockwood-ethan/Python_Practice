# import tkinter

# window = tkinter.Tk()
# window.title("My first GUI Program")
# window.minsize(width=500, height=300)

# # Label
# my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "italic"))
# my_label.pack(side="left")



# window.mainloop()

def add(*args):
    sum = 0
    for n in args:
        sum = n + sum
    return sum

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["mulitiply"]

calculate(2, add=3, multiply=5)