import turtle as t
import random
import colorgram

t.colormode(255)

# colors = colorgram.extract("Hirst_Painting\\image.jpg", 30)

tim = t.Turtle()
tim.shape("turtle")
tim.pensize(2)
tim.speed(0)

'''Blank color list to add extracted RGB tuples'''
# color_list = []

'''Extract RGB tuples from image of Hirst painting and add to list'''
# for pos, i in enumerate(colors):
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     color_tuple = (r, g, b)
#     color_list.append(color_tuple)

'''Copy/paste rgb tuples after extraction, remove background colors, this way we dont have to extract colors every time the program runs'''
color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

def hirst(width=10, height=10):
    y = -240
    for i in range(height):
        tim.penup()
        y += 40
        tim.goto(-200, y)
        for j in range(width):
            tim.dot(20, random.choice(color_list))
            tim.forward(40)
    tim.pendown()
    
hirst()

def spirograph():
    heading = 0
    while heading <= 360:
        tim.pencolor(random.choice(color_list))
        tim.setheading(heading)
        tim.circle(120)
        heading += 20

spirograph()

def random_walk(num_steps):
    i = 0
    directions = [0, 90, 180, 270]
    while i <= num_steps:
        tim.pencolor(random.choice(color_list))
        tim.forward(30)
        tim.setheading(random.choice(directions))
        i += 1

random_walk(200)

def pattern_walk():
    for i in range(3, 11):
        tim.pencolor(random.choice(color_list))
        divisor = 1
        while divisor <= i:
            tim.forward(100)
            tim.right(360 / i)
            divisor += 1

pattern_walk()

screen = t.Screen()
screen.exitonclick()