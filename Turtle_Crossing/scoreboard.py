from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.goto(-300, 225)
        self.write(f'Level: {self.level}', align="center", font=("Courier", 16, "normal"))
        
    def update_score(self):
        self.level += 1
        self.clear()
        self.write(f'Level: {self.level}', align="center", font=("Courier", 16, "normal"))