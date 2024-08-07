import turtle as t

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Score(t.Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.score = 0
        with open("./Snake_Game/data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.speed("fastest")
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("./Snake_Game/data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_score()