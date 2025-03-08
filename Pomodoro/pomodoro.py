from tkinter import *
import math
#---------------------------- CONSTANTS ----------------------------#
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

#---------------------------- RESET CHECK MARKS ----------------------------#
def reset_check_marks():
    global reps
    mark = ""
    work_sessions = math.floor(reps/2)
    for i in range(work_sessions):
        mark += "✔"
    check_label.config(text=mark)

#---------------------------- TIMER RESET ----------------------------#
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0
    reset_check_marks()
    
#---------------------------- TIMER MECHANISM ----------------------------#
def start_timer():
    global reps
    reps += 1
    work_sec = 1
    short_break_sec = 1
    long_break_sec = 1
    if reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
        reset_check_marks()
        reps = 0
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
        reset_check_marks()
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
        reset_check_marks()

#---------------------------- COUNTDOWN MECHANISM ----------------------------#
def count_down(count):
    global reps
    minutes = math.floor(count / 60)
    seconds = count % 60
    if minutes == 0:
        minutes = "00"
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()

#---------------------------- UI SETUP ----------------------------#
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 40), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="Pomodoro\\tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

check_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15))
check_label.grid(column=1, row=3)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()