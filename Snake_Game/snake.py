import turtle as t

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
        self.tail = self.snake_body[len(self.snake_body) - 1]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_square = t.Turtle(shape="square")
            new_square.penup()
            new_square.color("white")
            new_square.goto(position)
            self.snake_body.append(new_square)

    def grow_snake(self):
        new_square = t.Turtle(shape="square")
        new_square.penup()
        new_square.color("white")
        new_x = self.tail.xcor()
        new_y = self.tail.ycor()
        new_square.goto(new_x, new_y)
        self.snake_body.append(new_square)
        
    def reset(self):
        for seg in self.snake_body:
            seg.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]
        self.tail = self.snake_body[len(self.snake_body) - 1]

    def move(self):
        for seg in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg - 1].xcor()
            new_y = self.snake_body[seg - 1].ycor()
            self.snake_body[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)