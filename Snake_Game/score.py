import turtle as t

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Score(t.Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.score = 0
        self.color("white")
        self.speed("fastest")
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.clear()
        self.color("red")
        self.goto(0, 0)
        self.write(f"GAME OVER. FINAL SCORE: {self.score}", align=ALIGNMENT, font=FONT)