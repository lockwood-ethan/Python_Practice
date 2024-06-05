import turtle as t
import random as r

is_race_on = False
screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-50, -20, 10, 40, 70, 100]
all_turtles = []

for pos, color in enumerate(colors):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[pos])
    new_turtle.goto(-230, y_positions[pos])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lose. The {winning_color} turtle won the race.")
        rand_distance = r.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
