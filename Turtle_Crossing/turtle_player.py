from turtle import Turtle

class TurtlePlayer(Turtle):
    def __init__(self, start_pos):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("green")
        self.goto(start_pos)
        self.setheading(90)
        
    def go_up(self):
        self.setheading(90)
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        self.setheading(270)
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
        
    def go_left(self):
        self.setheading(180)
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def go_right(self):
        self.setheading(0)
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())
        
    def reset_turtle(self):
        self.goto(0, -230)