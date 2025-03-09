from tkinter import *
from tkinter import messagebox
import random
import string

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    password = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for n in range(12)])
    password_entry.insert(0, password)
    password_entry.clipboard_clear()
    password_entry.clipboard_append(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:    
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("Password_Manager\\data.txt", "a") as data:
                data.write(f"{website} | {email} | {password}\n")
            password_entry.delete(0, END)
            website_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_img = PhotoImage(file="Password_Manager\\logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", bg="white")
website_label.grid(column=0, row=1, pady=2)

website_entry = Entry(width=52, relief="solid")
website_entry.grid(column=1, columnspan=2, row=1, pady=2)
website_entry.focus()

email_label = Label(text="Email/Username:", bg="white")
email_label.grid(column=0, row=2, pady=2)

email_entry = Entry(width=52, relief="solid")
email_entry.grid(column=1, columnspan=2, row=2, pady=2)
email_entry.insert(0, "lockwood.ethan@yahoo.com")

password_label = Label(text="Password:", bg="white")
password_label.grid(column=0, row=3, pady=2)

password_entry = Entry(width=34, relief="solid")
password_entry.grid(column=1, row=3, pady=2)

gen_password_button = Button(text="Generate Password", width=14, relief="groove", command=generate_password)
gen_password_button.grid(column=2, row=3, pady=2)

add_button = Button(text="Add", width=44, relief="groove", command=add_password)
add_button.grid(column=1, columnspan=2, row=4, pady=2)

window.mainloop()