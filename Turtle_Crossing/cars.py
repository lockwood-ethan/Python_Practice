from turtle import Turtle

class Car(Turtle):
    def __init__(self, start_pos):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(start_pos)
        
    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())