import turtle as t

tim = t.Turtle()
screen = t.Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_clockwise():
    tim.right(10)

def turn_unclockwise():
    tim.left(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    

screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="a", fun=turn_unclockwise)
screen.onkeypress(key="d", fun=turn_clockwise)
screen.onkey(key="space", fun=clear)
screen.exitonclick()