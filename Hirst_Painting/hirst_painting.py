import turtle as t
import random as r
from color_list import colors

def random_walk(num_steps):
    i = 0
    directions = [0, 90, 180, 270]
    while i <= num_steps:
        tim.pencolor(r.choice(color_list))
        tim.forward(30)
        tim.setheading(r.choice(directions))
        i += 1

color_list = colors
tim = t.Turtle()
tim.shape("turtle")
tim.color("DeepPink")
tim.pensize(10)
tim.speed(0)
# for i in range(3, 11):
#     tim.pencolor(r.choice(color_list))
#     divisor = 1
#     while divisor <= i:
#         tim.forward(100)
#         tim.right(360 / i)
#         divisor += 1

random_walk(r.choice(range(10, 101)))

screen = t.Screen()
screen.exitonclick()