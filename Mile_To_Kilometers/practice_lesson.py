import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
#Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

# my_label["text"] = "New Text"
# my_label.config(text="New Text")

#Button

def button_clicked():
    my_label.config(text=input.get())

button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

button2 = tkinter.Button(text="Click Me")
button2.grid(column=2, row=0)

#Entry

input = tkinter.Entry(width=10)
input.grid(column=3, row=2)


window.mainloop()

# # def add(*args):
# #     total = 0
# #     for n in args:
# #         total = total + n
# #     print(total)
    
# # add(2, 4, 6, 18)

# def calculate(n, **kwargs):
#     for key, value in kwargs.items():
#         n += kwargs["add"]
#         n *= kwargs["multiply"]
#     print(n)
    
# calculate(2, add=3, multiply=5)

# class Car:
    
#     def __init__(self, **kw):
#         self.make = kw.get("make")
#         self.model = kw.get("model")
        
# my_car = Car(make="Nissan", model="GTR")
# print(my_car.model)